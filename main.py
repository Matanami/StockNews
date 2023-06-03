import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "<YOUR_STOCK_API_KEY>"
NEWS_API_KEY = "<YOUR_NEWS_API_KEY>"
TWILIO_ACCOUNT_SID = "<YOUR_TWILIO_ACCOUNT_SID>"
TWILIO_AUTH_TOKEN = "<YOUR_TWILIO_AUTH_TOKEN>"

STOCK_URL = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_URL = "https://newsapi.org/v2/everything"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

TWILIO_PHONE_NUMBER = "+19166595103"
MY_PHONE_NUMBER = "+9720546589173"

def get_stock_price_change():
    response = requests.get(STOCK_URL, params=stock_parameters)
    data = response.json()
    time_series = data.get("Time Series (Daily)")
    if not time_series:
        print("Error: Failed to retrieve stock data.")
        return None

    daily_prices = list(time_series.values())
    if len(daily_prices) < 2:
        print("Error: Insufficient data to calculate stock price change.")
        return None

    yesterday_close = float(daily_prices[0]["4. close"])
    day_before_yesterday_close = float(daily_prices[1]["4. close"])

    change_percentage = abs((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
    return change_percentage

def get_news_articles():
    response = requests.get(NEWS_URL, params=news_parameters)
    data = response.json()
    articles = data.get("articles")
    if not articles:
        print("Error: Failed to retrieve news articles.")
        return []

    return articles[:3]

def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(f"SMS sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Error: Failed to send SMS. {e}")

def format_sms(stock_change, articles):
    sms = f"{STOCK}: "
    if stock_change > 0:
        sms += "🔺"
    elif stock_change < 0:
        sms += "🔻"
    else:
        sms += "🔘"

    sms += f"{stock_change:.2f}%\n\n"

    for article in articles:
        title = article["title"]
        brief = article["description"]
        sms += f"Headline: {title}\nBrief: {brief}\n\n"

    return sms.strip()

def main():
    stock_change = get_stock_price_change()
    if stock_change is not None and stock_change > 5.0:
        articles = get_news_articles()
        if articles:
            sms_message = format_sms(stock_change, articles)
            send_sms(sms_message)
        else:
            print("No news articles found.")
    else:
        print("Stock price change is less than 5%.")

if __name__ == "__main__":
    main()
