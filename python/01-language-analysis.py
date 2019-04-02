import os
import requests
from pprint import pprint

subscription_key = os.getenv('AZURE_SUBSCRIPTION_KEY')
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url = text_analytics_base_url + 'languages'

documents = {'documents': [
    {'id': '1', 'text': 'This is a document written in English.'},
    {'id': '2', 'text': 'Este es un document escrito en Español.'},
    {'id': '3', 'text': '这是一个用中文写的文件' }
]}
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()

pprint(languages)




