import requests
import os 
from rest_framework.response import Response
from google.cloud import translate_v2 as translate
from dotenv import load_dotenv


load_dotenv()
translate_client = translate.Client()

BASE_URL = os.getenv("APP_URL")

def search_(word_id, lang, target_lang, ENDPOINT, strictMatch='true', fields='None'):
    try:    
        if ENDPOINT=='translations':
            if lang == 'en':
                target_lang = 'de'
                
            url = f"{BASE_URL}/{ENDPOINT}/{lang}/{target_lang}/{word_id.lower()}?&strictMatch={strictMatch}"
            res = requests.get(url, headers={"app_id": os.getenv("APP_ID"), 'app_key':  os.getenv("APP_KEY")})

            result_r = res.json()
            translated_word = result_r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["translations"]
            
            translated_results = []
            for word in translated_word:
                translated_results.append(word["text"])
                
                
            lang_detection = translate_client.detect_language(translated_results[0])["language"]

            if lang_detection != 'en':
                translate = translate_client.translate(translated_results, "ur")
                
                translated_results = []
                for translated_words in translate:
                    res = translated_words["translatedText"]
                    translated_results.append(res)
            
            return {
                    "dictionary": "Oxford Dictionary",
                    "lang": lang,
                    "pos": "n.",
                    "priority": 0,
                    "word": [word_id],
                    "meanings": translated_results,
                }

            
        elif ENDPOINT == 'thesaurus':
            islangUrdu = False
            if lang == 'ur' or lang == 'fa':
                language = translate_client.translate(word_id, 'en')
                word_id = language["translatedText"]
                lang = 'en'
                islangUrdu = True

            url = f"{BASE_URL}/{ENDPOINT}/{lang}/{word_id.lower()}?&strictMatch={strictMatch}"
            r = requests.get(url, headers={"app_id": os.getenv("APP_ID"), "app_key": os.getenv("APP_KEY")})

            result_r = r.json()
            synonyms = result_r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]

            words = []
            for synonym in synonyms:
                words.append(synonym["text"])
            
            ###  Translating words in Urdu Language  ####    
            if  islangUrdu == True:    
                translate = translate_client.translate(words, "ur")
                words = []
                for translated_words in translate:
                    res = translated_words["translatedText"]
                    words.append(res)
                
            ###  Translating words in target_lang  ####
            translated_results = translate_client.translate(words, target_lang)
                
            meanings = []
            for output in translated_results:
                result = output["translatedText"]
                meanings.append(result)
                

            return {
                    "dictionary": "Oxford Dictionary",
                    "lang": lang,
                    "pos": "n.",
                    "priority": 0,
                    "synonyms": words,
                    "meanings": meanings,
                }

    except Exception as e:
        return Response("An error occured.", 500)
    

#for accssing elastic search, designing json queries underneath
def search_query(word_id, target_lang=None):
    if target_lang != None:
        return {
            'query': {
                'bool': {
                    'must': [
                        {'term': {'word.keyword': word_id}},
                        {'term': {'target_lang.keyword': target_lang}}
                    ]
                }
            }
        }
    
    return {
        'query': {
            'bool': {
                'must': [
                    {'term': {'word.keyword': word_id}}
                ]
            }
        }
    }
