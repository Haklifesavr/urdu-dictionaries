# import os
# import requests
# from rest_framework.response import Response
# from google.cloud import translate_v2 as translate
# from dotenv import load_dotenv

# load_dotenv()
# translate_client = translate.Client()

# def oxford_translation(searchkw, source_language, target_language):
#     try:
#         url = (
#             os.getenv("APP_URL")
#             + "/translations/"
#             + source_language
#             + "/"
#             + target_language
#             + "/"
#             + searchkw
#         )
        
#         r = requests.get(
#             url,
#             headers={"app_id": os.getenv("APP_ID"), "app_key": os.getenv("APP_KEY")},
#         )
#         result_r = r.json()
#         translated_word = result_r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["translations"]

#         translated_results = []
#         for word in translated_word:
#             translated_results.append(word["text"])
#             print("Result TEST", translated_results)
            
#         return {
#                 "dictionary": "Oxford Dictionary",
#                 "lang": source_language,
#                 "pos": "n.",
#                 "priority": 0,
#                 "word": searchkw,
#                 "meanings": translated_results,
#             }

#     except Exception as e:
#         return Response("An error occured.", 500)
