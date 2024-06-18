import os
import json
from pickle import DICT
from threading import Thread
from rest_framework.response import Response
from .translators import google_translate, es_translate
from google.cloud import translate_v2 as translate
from rest_framework.views import APIView
from .oxford_api.catalog import  all_catalogs
from dict_api.oxford_api.queries.oxford_queries import all_queries
from rest_framework import status

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds.json"
translate_client = translate.Client()

class search_view(APIView):
    filter = 'translations'
    INDEX_NAME = 'oxford_translations_catalog'
    
    def post(self, request):
        

        word_id = request.POST.get('word')
        lang = translate_client.detect_language(word_id)["language"]

        filters = request.POST.get('filters')
        filters = json.loads(filters)['dic']

        results = []
            
            ## ---- GOOGLE TRANSLATION RESULTS ---- ##
        if 'Google' in filters:
            results.append(google_translate.google_translation(word_id, lang))
        try:    
            ## ---- OXFORD TRANSLATION RESULTS ---- ##
            if 'oxford' in filters:
                res = all_catalogs.search(word_id, lang, INDEX_NAME=self.INDEX_NAME)
                if res:
                    res['word'] = [res['word']]
                
                if not res:
                    res = all_queries.search_(word_id, lang, target_lang='en', ENDPOINT='translations', strictMatch='false')
                    
                if res != None:
                    results.append(res)
                
                    Thread(target=all_catalogs.save,
                            args=(word_id, lang, res, self.filter, self.INDEX_NAME)).start()
    
            for dicts in filters:
                resp = (es_translate.search_ES(word_id, dicts))
                if resp != None:
                    if dicts == "Urdu Seek":
                        results.extend(resp[1:2])
                    else:
                        results.extend(resp)
                
            return Response(results)
        except Exception as e:
            print("EXCEPTION:", e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
