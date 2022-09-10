import requests
from datetime import datetime, timedelta
import smtplib
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

MY_EMAIL = "sarai.gaylord@ethereal.email"
PASSWORD = os.environ.get("PASSWORD")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
end_date = list(stock_data)[0]
end_price = float(stock_data[end_date]["4. close"])
end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

start_date = end_date - timedelta(days=1)
start_price = float(stock_data[str(start_date)]["4. close"])
stock_difference = round((start_price - end_price) / start_price * 100)

if stock_difference > 1 or stock_difference < -1:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": start_date,
        "to": end_date,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()["articles"]
    articles = news_data[:3]
    messages = [f"Subject:{STOCK} {stock_difference}%\n\n{article['title']}\n" \
                f"{article['description']}" for article in articles]

    for message in messages:
        message = message.encode('utf-8').strip()
        with smtplib.SMTP(host="smtp.ethereal.email", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message)
