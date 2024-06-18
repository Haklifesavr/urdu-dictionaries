from rest_framework.views import APIView
from rest_framework.response import Response
from .catalog import  all_catalogs
from threading import Thread
from dict_api.oxford_api.queries.oxford_queries import all_queries
from dict_api.translators import google_translate, es_translate

from google.cloud import translate_v2 as translate
from dict_api.translators import google_translate, es_translate
import os

translate_client = translate.Client()

class SynonymsView(APIView):
    filters = 'thesaurus'
    INDEX_NAME = 'oxford_thesaurus_catalog'
    
    def get(self, request):
        try:
            word_id = request.query_params.get('word')
            lang = translate_client.detect_language(word_id)["language"]
            target_lang=request.query_params.get('target_lang')
            
            results = []
            google_res = translate_client.translate(word_id, target_lang)
            translated_res = google_res["translatedText"]
            word_meaning = {'translation': translated_res}
            results.append(word_meaning)
                
            res = all_catalogs.search(word_id, target_lang, INDEX_NAME=self.INDEX_NAME)
            if not res:
                res = all_queries.search_(word_id, lang, target_lang, ENDPOINT='thesaurus', strictMatch='false')
            
            if res != None:
                results.append(res)
                Thread(target=all_catalogs.save, 
                    args=(word_id, target_lang, res, self.filters, self.INDEX_NAME)).start()
                
            if(isinstance(results[1], list)):
                res = results[1][0]
                results = results[0:1]
                results.append(res)
                return Response(results)
            else:
                return Response(results)
        except Exception as e:
            print(e)
            return Response(status=404)
