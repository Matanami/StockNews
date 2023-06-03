# Stock News Alert

Stock News Alert is a Python script that retrieves the latest stock price information and news articles for a given stock symbol. If the stock price change exceeds a threshold (5% in this example), it sends an SMS notification to a specified phone number with the stock price change percentage and the headlines and brief descriptions of the top three news articles.

## Prerequisites

- Python 3 installed on your machine
- Required Python packages: `requests` and `twilio`

## Setup

1. Clone the repository:


2. Install the required Python packages:
pip install requests twilio



3. Obtain API keys and credentials:
   - Stock API Key: Get your API key from AlphaVantage and replace `<YOUR_STOCK_API_KEY>` in the script.
   - News API Key: Get your API key from News API and replace `<YOUR_NEWS_API_KEY>` in the script.
   - Twilio Account SID and Auth Token: Create an account on Twilio, obtain your Account SID and Auth Token, and replace `<YOUR_TWILIO_ACCOUNT_SID>` and `<YOUR_TWILIO_AUTH_TOKEN>` in the script.

4. Update phone number information:
   - Replace `<YOUR_TWILIO_PHONE_NUMBER>` with your Twilio phone number.
   - Replace `<YOUR_PHONE_NUMBER>` with your phone number to receive the SMS notifications.

## Usage

To run the script, navigate to the project directory and execute the following command:

python stock_news_alert.py


The script will retrieve the stock price information and news articles for the specified stock symbol (e.g., TSLA) and send an SMS notification if the stock price change exceeds the threshold.

## Customization

- Stock and Company Information: Modify the `STOCK` and `COMPANY_NAME` variables in the script.
- Price Change Threshold: Adjust the `change_threshold` variable in the script.
- Number of News Articles: Modify the `num_articles` variable in the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [AlphaVantage](https://www.alphavantage.co/) - Stock price data API provider
- [News API](https://newsapi.org/) - News articles API provider
- [Twilio](https://www.twilio.com/) - SMS notification service
# StockNews
# StockNews
