import os 

HOSTS = [
    {
        'host': os.environ['ELASTIC_HOST'],
        'port': 9243,
        'use_ssl': True
    }
]

HTTP_AUTH = ('elastic', os.environ['ELASTIC_PASSWORD'])