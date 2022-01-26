import requests
import hashlib
import os
import json
import datetime

apikey = open("../../vtoken", "r").read().rstrip('\n')

def vtrequest(md5hashed):
    headers = {
        "Accept":"application/json",
        "x-apikey":apikey,
    }
    url = "https://www.virustotal.com/api/v3/files/"+md5hashed
    response = requests.request("GET", url, headers = headers)
    return response

for filename in os.listdir("../../dataset"):
    f=open(os.path.join("../../dataset", filename),'rb')
    text = f.read()
    md5Hash = hashlib.md5(text)
    md5Hashed = md5Hash.hexdigest()
    jsondecoded = json.loads(vtrequest(md5Hashed).text)
    print(jsondecoded['data']['attributes']['names'][0], end = ', ') 
#    print(jsondecoded['data']['attributes']['trid'][1]['file_type'], end = ', ')
    print(jsondecoded['data']['attributes']['reputation'], end = ', ')
    print(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['first_submission_date']), end= ', ')
    print(datetime.datetime.fromtimestamp(jsondecoded['data']['attributes']['last_submission_date']), end= ', ')
    print('\n')

# 
# file_payload = open("../../dataset/Objective_See/Ventir/Ventir", "rb").read()
# 
# md5Hash = hashlib.md5(file_payload)
# md5Hashed = md5Hash.hexdigest()
# 
# print(md5Hashed)
# 
# url = "https://www.virustotal.com/api/v3/files/"+md5Hashed
# 
# print(url)
# 
# payload = file_payload
# 
# headers = {
#     "Accept": "application/json",
#     "x-apikey": apikey,
# }
# 
# response = requests.request("GET", url, headers=headers)
# 
# json = open("../../json", "w").write(response.text)
# print(response.text)
