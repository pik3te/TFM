import os
import json
import datetime


for filename in os.listdir("../../json"):
    f=open(os.path.join("../../json", filename),'r')
    text = f.read()
    jsondecoded = json.loads(text)
    print(jsondecoded['data']['attributes']['sha1'], end = ', ') 
    print(jsondecoded['data']['attributes']['type_description'], end = ', ') 
    print(jsondecoded['data']['attributes']['size'], end = ', ') 
    print(jsondecoded['data']['attributes']['popular_threat_classification']['suggested_threat_label'], end = ', ') 
    for engine in jsondecoded['data']['attributes']['last_analysis_results']:
        print(jsondecoded['data']['attributes']['last_analysis_results'][engine]['category'], end= ', ')
    print(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['last_submission_date']), end= ', ')
    print(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['first_submission_date']), end= ', ')
    print('\n')

#    print(jsondecoded['data']['attributes']['trid'][1]['file_type'], end = ', ')
#    print(jsondecoded['data']['attributes']['reputation'], end = ', ')
#    
#    
