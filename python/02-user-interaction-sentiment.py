import os
import requests
from pprint import pprint


def get_sentiment(sentiment):
    subscription_key = os.getenv('AZURE_SUBSCRIPTION_KEY')
    text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    sentiment_api_url = text_analytics_base_url + "sentiment"
    documents = {'documents': [
        {'id': '1', 'language': 'en',
         'text': sentiment}
    ]}
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()

    pprint(sentiments["documents"][0]["score"])
    score = sentiments["documents"][0]["score"]
    if score > .5: # more positive
        return "Your sentiment is more positive :)\n"

    elif score < .5: # more negative
        return "Your sentiment is more negative :(\n"

    elif score == .5:
        return "meh"



while True:
    sentiment = input("Give me your sentiment! \n")
    if sentiment == "":
        break
    else:
        print(get_sentiment(sentiment))
