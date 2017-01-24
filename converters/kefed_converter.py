
from elasticsearch import Elasticsearch, helpers
import pandas as pd
import re

#
# Class to encapsulate functionality of converting from KEfED Models from editor interface
# to ontology-based representations in OBI
#
class KefedConverter(object):

    def __init__(self):
        self.es = Elasticsearch()

    def get_model_from_name(self, model_name):
        resp = self.es.search(index="kefed", doc_type=['model'],
                         body={"query": {
                             "match_phrase": {"modelName": model_name}
                         }})
        try:
            return resp['hits']['hits'][0]['_source']
        except StandardError:
            print("No data found for model " + model_name)
            return None

    def build_robot_spreadsheet(self, model, curator=""):
        headers = ['ID', 'label', 'is already in OBI', 'reviewed', 'review comments', 'reviewer ', 'ROBOT problems', 'has curation status',
                   'tracker items', 'alternative term', 'definition', 'definition source', 'example of usage',
                   'editor note', 'curator note', 'term editor', 'logical type', 'equivalent classes', 'parent classes',
                   'evaluant', 'analyte', 'device', 'reagent', 'input', 'INPUT GROUPING', 'output', 'output is about',
                   'objective', 'associated axioms', 'comment']

        templates = {}
        templates['ID'] = "ID"
        templates['label'] = "A rdfs:label"
        templates['has curation status'] = "AL has curation status"
        templates['alternative term'] = "A alternative term SPLIT = |"
        templates['definition'] = "A definition SPLIT = |"
        templates['definition source'] = "A definition source SPLIT = |"
        templates['example of usage'] = "A example of usage SPLIT = |"
        templates['editor note'] = "A editor note SPLIT = |"
        templates['curator note'] = "A curator note SPLIT = |"
        templates['term editor'] = "A term editor SPLIT = |"
        templates['logical type'] = "CLASS_TYPE"
        templates['parent classes'] = "C %"
        templates['evaluant'] = "C (has_specified_input some (% and 'has role' some 'evaluant role')) and (realizes some ('evaluant role' and ('role of' some %)))"
        templates['analyte'] = "C (has_specified_input some %) and (realizes some ('analyte role' and ('inheres in' some %)))"
        templates['device'] = "C (has_specified_input some %) and (realizes some (function and ('inheres in' some %)))"
        templates['reagent'] = "C (has_specified_input some %) and (realizes some ('reagent role' and ('inheres in' some %)))"
        templates['input'] = "C has_specified_input some %"
        templates['output'] = "C has_specified_output some %"
        templates['output is about'] = "C has_specified_output some ('is about' some %)"
        templates['objective'] = "C achieves_planned_objective some %"
        templates['associated axioms'] = "C %"

        # HOW TO GET THE INDEX OF EACH COLUMN FROM THIS LIST: e.g., headers.index('ID')

        rows = []
        rows.append(templates)

        for n in model['nodes']:

            # Entities
            if (n['spriteid'] == 'Experimental Object'):
                e_hash = self.add_ooevv_element_to_spreadsheet(n,'material entity')
                rows.append(e_hash)

            # Entities
            elif (n['spriteid'] == 'Activity'):
                e_hash = self.add_ooevv_element_to_spreadsheet(n,'planned process')
                rows.append(e_hash)

            # Entities
            if (n['spriteid'] == 'Measurement Specification' or
                        n['spriteid'] == 'Parameter Specification'):
                e_hash = self.add_ooevv_element_to_spreadsheet(n,'measurement datum')
                rows.append(e_hash)

        frame_rows = []
        regex1 = re.compile("[\r\n]")
        regex2 = re.compile("\s+")
        regex3 = re.compile("\s*\-{0,1}\d+$")
        for r in rows:
            frame_row = []
            for i in range(len(headers)):
                h = headers[i]
                e = r.get(h, None)
                if( e is None ):
                    frame_row.append(e)
                elif isinstance(e, basestring):
                    e = regex1.sub(" ", e)
                    e = regex2.sub(" ", e)
                    e = regex3.sub("", e)
                    frame_row.append(e)
                else:
                    frame_row.append(e)
            frame_rows.append(frame_row)

        df = pd.DataFrame(frame_rows, columns=headers)
        return df

    def add_ooevv_element_to_spreadsheet(self, n, parent):
        hash = {}
        ontIds = n['ontologyIds']
        if ontIds is not None and isinstance(ontIds, list) and len(ontIds)>0:
            for ontId in ontIds:
                hash['ID'] = ontId['ontologyIdentifier']
                hash['label'] = ontId['ontologyLocalName']
                hash['is already in OBI'] = True
        else:
            hash['ID'] = "ooevv:" + n['uid']
            hash['label'] = n['nameValue']
            hash['parent classes'] = parent

        return hash

    #
    # TABULATE CONTENTS OF WHOLE REPOSITORY
    #
    def list_all_models(self):
        resp = self.es.search(index="kefed", doc_type=['model'],size=1000,
                        body={
                            "_source": ["modelName","source","description"],
                            "query": {
                                "match_all": {}
                            }
                        })

        models = []
        try:
            for hit in resp['hits']['hits']:
                m = hit['_source']
                m['id'] = hit['_id']
                models.append(hit['_source'])
            return models
        except StandardError:
            print("No models found")
            return None

    def list_all_entities(self):
        entities = []
        for mm in self.list_all_models():
            m = self.get_model_from_name(mm['modelName'])
            for n in m['nodes']:
                if(n['spriteid'] != 'Experimental Object'):
                    continue
                entities.append(n)
        return entities

    def list_all_processes(self):
        processes = []
        for mm in self.list_all_models():
            m = self.get_model_from_name(mm['modelName'])
            for n in m['nodes']:
                if(n['spriteid'] != 'Activity'):
                    continue
                processes.append(n)
        return processes

    def list_all_variables(self):
        variables = []
        for mm in self.list_all_models():
            m = self.get_model_from_name(mm['modelName'])
            for n in m['nodes']:
                if(n['spriteid'] != 'Measurement Specification' and
                    n['spriteid'] != 'Parameter Specification' ):
                    continue
                variables.append(n)
        return variables
