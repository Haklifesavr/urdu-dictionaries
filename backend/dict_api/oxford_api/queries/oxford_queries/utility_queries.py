# from oxford_dict.local_config import OXFORD_API_CONFIG
import requests
import os

BASE_URL = os.getenv("APP_URL")

def search_lang_(request_params, ENDPOINT):
    lang = request_params.get('lang')
    url = f"{BASE_URL}/{ENDPOINT}/{lang}"
    
    res = requests.get(url, headers={"app_id": os.getenv("APP_ID"), 'app_key':  os.getenv("APP_KEY")})
    return res


def search_lang_query(lang):
    return {
        'query': {
            'bool': {
                'must': [
                    {'term': {'lang.keyword': lang}}
                ]
            }
        }
    }


def search_lang_and_targetlang_(request_params, ENDPOINT):
    lang = request_params.get('lang')
    target_lang = request_params.get('target_lang')
    url = f"{BASE_URL}/{ENDPOINT}/{lang}/{target_lang}"
    res = requests.get(url, headers={"app_id": os.getenv("APP_ID"), 'app_key':  os.getenv("APP_KEY")})
    return res


def search_lang_and_targetlang_query(lang, target_lang):
    return {
        'query': {
            'bool': {
                'must': [
                    {'term': {'lang.keyword': lang}},
                    {'term': {'target_lang.keyword': target_lang}}
                ]
            }
        }
    }


def search_endpoint_(request_params, ENDPOINT):
    endpoint = request_params.get('endpoint')

    url = f"{BASE_URL}/{ENDPOINT}/{endpoint}"
    res = requests.get(url, headers={"app_id": os.getenv("APP_ID"), 'app_key':  os.getenv("APP_KEY")})
    return res


def search_endpoint_query(endpoint):
    return {
        'query': {
            'bool': {
                'must': [
                    {'term': {'endpoint.keyword': endpoint}}
                ]
            }
        }
    }


def search_languages(request_params):
    ENDPOINT = 'languages'
    url = f"{BASE_URL}/{ENDPOINT}"
    res = requests.get(url, headers={"app_id": os.getenv("APP_ID"), 'app_key':  os.getenv("APP_KEY")})
    return res


def search_languages_query(lang, target_lang):
    return {
        'query': {
            'bool': {
                'must': [
                ]
            }
        }
    }
