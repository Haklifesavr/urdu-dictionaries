def search_query(word, lang, target_lang):
    if target_lang != None:
        return {
            'query': {
                'bool': {
                    'must': [
                        {'term': {'word.keyword': word}},
                        {'term': {'lang.keyword': lang}},
                        {'term': {'target_lang.keyword': target_lang}}
                    ]
                }
            }
        }

    return {
        'query': {
            'bool': {
                'must': [
                    {'term': {'word.keyword': word}},
                    {'term': {'lang.keyword': lang}}
                ]
            }
        }
    }


























# def search_query(word, lang, target_lang):
#     query ={
#         'query': {
#             'bool': {
#                 'must': [
#                     {'term': {'word.keyword': word}},
#                     {'term': {'lang.keyword': lang}}
#                 ]
#             }
#         }
#     }
#     if target_lang != None:
#         query['query']['bool']['must'].append({'term': {'target_lang.keyword': target_lang}})
#     return   query                                       








