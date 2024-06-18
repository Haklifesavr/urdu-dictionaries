from google.cloud import translate_v2 as translate
from rest_framework.response import Response
import os

# path=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds.json"
translate_client = translate.Client()


def google_translation(searchkw, source_language):
    try:
        if source_language=='ur' or source_language=='fa':
            result = translate_client.translate(searchkw, target_language="en")

        elif source_language=='en':
            result = translate_client.translate(searchkw, target_language="ur")

        translated_results = result["translatedText"]
        return {
                "dictionary": "Google Translation",
                "lang": source_language,
                "pos": "n.",
                "priority": 0,
                "word": [searchkw],
                "meanings": [translated_results],
            }
        

    except Exception as e:
        return Response("An error occured", 500)
