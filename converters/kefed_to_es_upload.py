#!/usr/bin/env python
"""
kefed_to_es_upload.py

Uploads a KEfED JSON file into an elastic search store.
"""

import argparse
from elasticsearch import Elasticsearch, helpers
import json
import time

cur_sent_id = 0


def decode_json_file(json_file, type):

    with open(args.inputFile) as data_file:
        json_list = json.load(data_file)

    for i, js in enumerate(json_list):
        if(js.get('_type') != type):
            continue
        yield i, js

def run_main(args):

    es = Elasticsearch()

    index_exists = es.indices.exists(index=["kefed"], ignore=404)

    #if (index_exists):
    #    es.indices.delete(index='kefed', ignore=400)

    es.indices.create(index='kefed', ignore=400)

    # Mapping to make the encoding of individual words unique.
    mapping_body = {
        "properties": {
            "modelName": {
                "type": "string",
                "index": "not_analyzed"
            },
            "source": {
                "type": "string",
                "index": "not_analyzed"
            }
        }
    }
    es.indices.put_mapping("model", mapping_body, "kefed")
    es.indices.put_mapping("data", mapping_body, "kefed")

    # NOTE the (...) round brackets. This is for a generator.
    gen = ({
               "_index": "kefed",
               "_type": "model",
               "_id": i,
               "_source": es_d,
           } for i, es_d in decode_json_file(args.inputFile, "KefedModel"))

    helpers.bulk(es, gen)

    # NOTE the (...) round brackets. This is for a generator.
    gen = ({
               "_index": "kefed",
               "_type": "data",
               "_id": i,
               "_source": es_d,
           } for i, es_d in decode_json_file(args.inputFile, "KefedExperiment"))

    helpers.bulk(es, gen)

 # gold_aligned_fh and gold_aligned_fh.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-i', '--inputFile', help='name of KEfED Model to be processed in the repository')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    
    run_main(args)

