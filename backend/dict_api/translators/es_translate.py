from .elastic_client import ElasticClient
from rest_framework.response import Response
from rest_framework import status

es_client=ElasticClient()
ES_INDEX="urdu_dictionary_app"
def Parsedictionary(res):
        elasticList=[]
        for Dict in res:
            nDict={}
            words=[]
            meanings=[]
            nDict['dictionary'] = Dict[0]["_source"]['dictionary']
            nDict['lang'] = Dict[0]["_source"]['lang']
            try:
                nDict['pos'] = Dict[0]["_source"]['dictionary']
            except:
                nDict['pos'] = ''
            nDict['priority'] = Dict[0]["_source"]['priority']
            for item in Dict:
                words.append(item["_source"]['word'])
                meanings.append(item["_source"]['meanings'])
            nDict["word"] = words
            nDict["meanings"]=meanings

            #implemented translation for each meaning +
            elasticList.append(nDict)
        return elasticList


def search_ES(searchkw, d):
    try:
        body = get_query(searchkw, d)
        response = es_client.query(index_name=ES_INDEX, query=body)
        hits = response["aggregations"]["message"]["buckets"]
        temp =[]
        for i in hits:
            if i["doc_count"] !=0:
                temp.append(i["hit"]["hits"]["hits"])
        hits = temp
        
        result = Parsedictionary(hits)
        # print(result)
        return result
        
    except Exception as e:
        print(e)
        # return Response(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

def get_query(searchkw, d):
    return {
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": searchkw,
                            "fields": ["word", "word.en", "word.ar"],
                            "type": "most_fields"
                        }
                    },
                    {
                    "terms" : { "dictionary.keyword": [d]}
                    }
                ]
            }
        }
        ,
        "aggs": {
            "message": {
                "filters": {
                    "filters": [
                        {"match": {"priority": 1}},
                        {"match": {"priority": 2}},
                        {"match": {"priority": 3}},
                        {"match": {"priority": 4}},
                        {"match": {"priority": 5}},
                        {"match": {"priority": 6}},
                        {"match": {"priority": 7}},
                        {"match": {"priority": 8}},
                        {"match": {"priority": 9}},
                        {"match": {"priority": 10}},
                        {"match": {"priority": 11}},
                        {"match": {"priority": 12}},
                        {"match": {"priority": 13}},
                        {"match": {"priority": 14}},
                        {"match": {"priority": 15}},
                        {"match": {"priority": 16}},
                        {"match": {"priority": 17}},
                        {"match": {"priority": 18}}
                    ]
                },
                "aggs": {"hit": {"top_hits": {"size": 10}}}
            }
        }
    }


# result = Parsedictionary(hits)

