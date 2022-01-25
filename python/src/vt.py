import requests
import hashlib
import os
import json

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
    print(jsondecoded)
    print(jsondecoded['data'])
    print(type(jsondecoded['data']))
    print("\n")


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
