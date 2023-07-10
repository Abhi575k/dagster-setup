
from dagster import asset
from dagster import AssetIn

from newsapi import NewsApiClient

import os
from dotenv import load_dotenv

load_dotenv()

@asset
def authenticate():
    # Basic Software defined asset
    api = NewsApiClient(api_key='0947e61238ad4260aa7415243ff9710a')
    
    data = api.get_top_headlines(sources='four-four-two')

    return data

@asset
def beautify_data(authenticate):
    # Asset with dependencies
    data = authenticate

    return data['articles']

@asset(ins={"data": AssetIn("beautify_data"), "data2": AssetIn("authenticate")})
def store_data(data, data2):
    # Asset with explicit dependencies
    f = open("data.txt", "w")
    f.write("")
    f.close()
    f = open("data.txt", "a")
    for item in data:
        f.write(item['title'])
        f.write('\n')
    f.close()
    return

@asset(ins={"data": AssetIn("store_data")})
def render_page(data):
    return

@asset(ins={"data": AssetIn("store_data")})
def send_email(data):
    return
