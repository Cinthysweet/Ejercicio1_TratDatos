from flask import Flask, Response
import requests
import json
import logging

app = Flask(__name__)


def search_in_yahoo(ticker: str):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = f"https://query1.finance.yahoo.com/v1/finance/search?q={ticker}&lang=en-US&region=US&quotesCount=6&newsCount=2&listsCount=2&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_cie_vespa&enableCb=true&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableResearchReports=true&enableCulturalAssets=true&researchReportsCount=2"
    r= requests.get(url,headers=headers)
    return r.json()
