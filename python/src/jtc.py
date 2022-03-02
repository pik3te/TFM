import os
import numpy as np
import json
import datetime
import pandas as pd

output = open("../../demo.json","w")

result = []

for filename in os.listdir("../../json"):
    f = open(os.path.join("../../json", filename),'r')
    text = f.read()
    json_decode = json.loads(text)
    my_dict={}
    my_dict['sha1'] = json_decode.get('data').get('attributes').get('sha1')
    my_dict['type'] = json_decode.get('data').get('attributes').get('type_description')
    my_dict['size'] = json_decode.get('data').get('attributes').get('size')
    my_dict['category'] = json_decode['data']['attributes']['popular_threat_classification']['popular_threat_category'][0]['value']
    my_dict['first_t'] = str(datetime.datetime.fromtimestamp(json_decode.get('data').get('attributes').get('first_submission_date')))
    my_dict['last_t'] = str(datetime.datetime.fromtimestamp(json_decode.get('data').get('attributes').get('last_submission_date')))
    analysis = []
    for engine in json_decode['data']['attributes']['last_analysis_results']:
        analysis_dict = {}
        analysis_dict[engine] = json_decode['data']['attributes']['last_analysis_results'][engine]['category']
        analysis.append(analysis_dict)
    my_dict['analysis'] = analysis
    result.append(my_dict)
    

back_json = json.dumps(result)
output.write(back_json)
df = pd.read_json(back_json)
df.first_t = pd.to_datetime(df.first_t)
df.last_t = pd.to_datetime(df.last_t)
print(df.category.value_counts())
print(df.info())
print(df.groupby(['category', pd.Grouper(key='first_t',axis=0,freq='Y')]).count())
print(df.count())
print(df.groupby(pd.Grouper(key='first_t',axis=0,freq='Y')).count(axis=1))

