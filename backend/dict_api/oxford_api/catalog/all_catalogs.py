from elasticsearch import Elasticsearch
from dict_api.oxford_api.queries.oxford_queries import all_queries
import json
import os 
from google.cloud import translate_v2 as translate
from dotenv import load_dotenv

load_dotenv()
translate_client = translate.Client()

ELASTIC = Elasticsearch(
                hosts=os.getenv("ELASTIC_CLOUD_ID"),
                http_auth=(
                    os.getenv("ELASTIC_USERNAME"), 
                    os.getenv("ELASTIC_PASSWORD")
                ),
                http_compress=True
            )


#used for elastic search results
def search(word_id, target_lang, INDEX_NAME):
    # word_id = word_id
    # lang = translate_client.detect_language(word)["language"]

    if INDEX_NAME == 'oxford_translations_catalog':
        # target_lang = request_params.get('target_lang')
        res = ELASTIC.search(all_queries.search_query(word_id, target_lang), INDEX_NAME)
        
    elif INDEX_NAME == 'oxford_thesaurus_catalog':
        # target_lang = request_params.get('target_lang')
        res = ELASTIC.search(all_queries.search_query(word_id, target_lang), INDEX_NAME)
        
    else:
        res = ELASTIC.search(body=all_queries.search_query(word_id), index=INDEX_NAME)

    if res['hits']['total']['value'] > 0:
        first_hit = res['hits']['hits'][0]
        
        return json.loads(first_hit['_source']['response'])
    else:
        return False


def save(word_id, target_lang, response, filters, indexName):
    """Save the word and other parameters like language in ES for future lookups"""
    
    # word_id = request_params.get('word')
    lang = translate_client.detect_language(word_id)["language"]
    # target_lang =request_params.get('target_lang')
    if target_lang :
        doc = {
        'word': word_id,
        'lang': lang,
        'target_lang' : target_lang,
        'filter': filters,
        'response': json.dumps(response)
        }
    else:
        doc = {
            'word': word_id,
            'lang': lang,
            'filter': filters,
            'response': json.dumps(response)
        }
        
    ELASTIC.index(indexName, doc)

    
