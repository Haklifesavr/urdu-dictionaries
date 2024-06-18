import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan, bulk
from dotenv import load_dotenv

load_dotenv()

class ElasticClient:
    """
    Provides helpful wrapper methods for document indexing, querying,
    deleting and index creation and deletion.
    Looks for ELASTIC_CLOUD_ID, ELASTIC_USERNAME and ELASTIC_PASSWORD env vars.
    """
    def __init__(self):
        self.es = Elasticsearch(
            hosts=os.getenv("ELASTIC_CLOUD_ID"), 
            http_auth=(
                os.getenv("ELASTIC_USERNAME"),
                os.getenv("ELASTIC_PASSWORD")
            ),
            http_compress=True
        )


    def create_index(self, index_name):
        if input(f"Create {index_name}? (y)") == 'y':
            self.es.indices.create(index_name, ignore=400)

    def insert(self, index_name, document, id=None):
        # TODO: return ok response?
        try:
            self.es.index(
                index = index_name,
                document = document,
                id = id
            )
        except Exception as e:
            print(e)

    def export_docs_in_bulk(self, index_name, docs):
        """docs: list of dictionaries (documents)"""
        def gen_docs(docs):
            for doc in docs:
                doc['_index'] = index_name
                yield doc
                
        print('Uploading documents in bulk to ' + index_name)
        bulk(self.es, gen_docs(docs))
        print('Done')

    def get_by_id(self, index_name, _id):
        return self.es.get(index=index_name, id=_id)
    
    def scroll(self, query, index_name, scroll='5m', size=1000):
        """
        Uses scroll api to return all results that satisfy the query.
        """
        results = []

        for res in scan(self.es, query, index=index_name, scroll=scroll, size=size):
            results.append(res)

        return results

    def query(self, index_name, query, **kwargs):
        results = self.es.search(index=index_name, body=query, **kwargs)
        #self.es.search(indeindex_name, search_query, **kwargs)
        return results

    def partial_update(self, index_name, _id, body):
        """
        Performs partial update
        (adds content of 'body' in the document, rest of _source remains the same)
        """
        self.es.update(index=index_name, id=_id, doc=body)

    def update_by_query(self, index_name, body):
        try:
            self.es.update_by_query(
                index = index_name, 
                body = body
            )
        except Exception as e:
            print(e)

    def delete_by_query(self, index_name, body):
        try:
            self.es.delete_by_query(
                index = index_name,
                body = body
            )
        except Exception as e:
            print(e)

    def delete_index(self, index_name):
        if input(f"Delete the index {index_name}? (type yes)") == 'yes':
            self.es.indices.delete(index=index_name, ignore=[400, 404])

    def delete_docs_in_bulk(self, index_name, ids):

        def gen_data():
            for doc_id in ids:
                yield {
                    "_op_type": "delete",
                    "_index": index_name,
                    "_id": doc_id
                }
        try:
            bulk(self.es, gen_data())
        except Exception as e:
            print(e)



if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    es = ElasticClient()
    query = {
        "match_all": {}
    }
    res = es.query('dms_files', query, size=1, sort={"created_at": {"order": "desc"}})
    print(res)
