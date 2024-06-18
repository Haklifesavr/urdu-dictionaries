from elasticsearch import Elasticsearch
# from oxford_dict.local_config import ELASTICSEARCH_CONFIG
from dict_api.oxford_api.queries.oxford_queries import utility_queries
import json
# from .elastic_client import ElasticClient
import os

ELASTIC = Elasticsearch(hosts=os.getenv("ELASTIC_CLOUD_ID"), http_auth=(os.getenv("ELASTIC_USERNAME"), os.getenv("ELASTIC_PASSWORD")),http_compress=True)

ELASTIC = Elasticsearch()
# es_client=ElasticClient()


def search_lang(request_params, INDEX_NAME):
    lang = request_params.get('lang')
    res = ELASTIC.search(utility_queries.search_lang_query(lang), INDEX_NAME)
    
    if res['hits']['total']['value'] > 0:
        first_hit = res['hits']['hits'][0]
        return json.loads(first_hit['_source']['response'])
    else:
        return False


def save_lang(request_params, response, INDEX_NAME):
    """Save the word and other parameters like language in ES for future lookups"""
    lang = request_params.get('lang')
    doc = {
        'lang': lang,
        'response': json.dumps(response)
    }
    ELASTIC.index(INDEX_NAME, doc)


def search_lang_and_targetlang(request_params, INDEX_NAME):
    """Checks whether the given word with the given parameters is saved in ES,
    returns the result if it is, False otherwise"""

    lang = request_params.get('lang')
    target_lang = request_params.get('target_lang')
    res = ELASTIC.search(utility_queries.search_lang_and_targetlang_query(
        lang, target_lang), INDEX_NAME)
    if res['hits']['total']['value'] > 0:
        first_hit = res['hits']['hits'][0]
        return json.loads(first_hit['_source']['response'])
    else:
        return False


def save_lang_and_targetlang(request_params, response, INDEX_NAME):
    """Save the word and other parameters like language in ES for future lookups"""
    lang = request_params.get('lang')
    target_lang = request_params.get('target_lang')
    doc = {
        'lang': lang,
        'target_lang': target_lang,
        'response': json.dumps(response)
    }
    ELASTIC.index(INDEX_NAME, doc)


def search_endpoint(request_params, INDEX_NAME):
    """Checks whether the given word with the given parameters is saved in ES,
    returns the result if it is, False otherwise"""

    endpoint = request_params.get('endpoint')
    res = ELASTIC.search(
        utility_queries.search_endpoint_query(endpoint), INDEX_NAME)
    if res['hits']['total']['value'] > 0:
        first_hit = res['hits']['hits'][0]
        return json.loads(first_hit['_source']['response'])
    else:
        return False


def save_endpoint(request_params, response, INDEX_NAME):
    """Save the word and other parameters like language in ES for future lookups"""
    endpoint = request_params.get('endpoint')
    doc = {
        'endpoint': endpoint,
        'response': json.dumps(response)
    }
    ELASTIC.index(INDEX_NAME, doc)

def search_languages(request_params):
    """Checks whether the given word with the given parameters is saved in ES,
    returns the result if it is, False otherwise"""

    INDEX_NAME = 'oxford_util_languages_catalog'
    lang = request_params.get('lang')
    target_lang = request_params.get('target_lang')
    res = ELASTIC.search(utility_queries.search_languages_query(
        lang, target_lang), INDEX_NAME)
    if res['hits']['total']['value'] > 0:
        first_hit = res['hits']['hits'][0]
        return json.loads(first_hit['_source']['response'])
    else:
        return False


def save_languages(request_params, response):
    """Save the word and other parameters like language in ES for future lookups"""
    INDEX_NAME = 'oxford_util_languages_catalog'
    doc = {
        'response': json.dumps(response)
    }
    ELASTIC.index(INDEX_NAME, doc)
