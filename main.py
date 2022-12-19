import requests
import twilio
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCK = "Your API KEY"
API_KEY_NEWS = "Your API KEY"
TWILIO_SID = "You Twilio sid "
TWILIO_AUTH = "Your Twilio Alth Token"

par = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : "TSLA",
    "apikey" : API_KEY_STOCK,

}
#"Time Series (Daily)"]["2022-12-16"]

req = requests.get(STOCK_ENDPOINT, params=par)
req.raise_for_status()
data = req.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]["4. close"]
before_yesterday = data_list[1]["4. close"]

difference = (abs(float(yesterday) - float(before_yesterday)))
diff_percent = round((difference / float(yesterday)) *100,2)




if diff_percent > 4:
    news ={
        "apiKey": API_KEY_NEWS,
        "qInTitle": STOCK_NAME}

    news_respones = requests.get(NEWS_ENDPOINT, params=news)
    news_respones.raise_for_status()
    articles = news_respones.json()["articles"]
    articles_3 = articles[:3]

    formated_3 = [f"{STOCK_NAME}: Change:{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles_3

    client = Clinet(TWILIO_SID, TWILIO_AUTH)
    for article in articles_3:
        message = client.message.create(
            body=article,
            from_="Twilio number",
            to= "Your number"
        )


