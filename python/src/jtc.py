import os
import json
import datetime

c=open("../../demo.csv","w")
t=open("../../json/0.json")

title_text = t.read()
json_title_decoded = json.loads(title_text)
c.write("sha1"+', ')
c.write("type"+', ')
c.write("category"+', ')
for engine in json_title_decoded['data']['attributes']['last_analysis_results']:
    c.write(engine+', ')
c.write ("last_time"+', ')
c.write ("firs_time")
c.write('\n')

for filename in os.listdir("../../json"):
    f=open(os.path.join("../../json", filename),'r')
    text = f.read()
    jsondecoded = json.loads(text)
    c.write(jsondecoded['data']['attributes']['sha1']+', ') 
    c.write(jsondecoded['data']['attributes']['type_description']+', ') 
    c.write(str(jsondecoded['data']['attributes']['size'])+', ') 
    c.write(jsondecoded['data']['attributes']['popular_threat_classification']['popular_threat_category'][0]['value']+', ') 
    c.write(str(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['last_submission_date']))+', ')
    c.write(str(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['first_submission_date']))+', ')
    for engine in jsondecoded['data']['attributes']['last_analysis_results']:
        c.write(jsondecoded['data']['attributes']['last_analysis_results'][engine]['category']+', ')
    c.write('\n')
#    c.write(jsondecoded['data']['attributes']['trid'][1]['file_type']+', ')
#    c.write(jsondecoded['data']['attributes']['reputation']+', ')
#    
#    

c=open("../../demo.csv","r")
print(c.read())
