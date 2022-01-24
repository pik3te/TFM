import requests
import hashlib
import os

apikey = open("../../vtoken", "r").read().rstrip('\n')



for filename in os.listdir("files"):
    open(os.path.join("files", filename),'rb') as f:
        text = f.read()
        md5Hash = hashlib.md5(f)
        md5Hashed = md5Hash.hexdigest()
        print(vtrequest(md5Hashed))

def vtrequest(md5hashed):
    headers = {
        "Accept":"application/json",
        "x-apikey":apikey,
    }
    url = "https://www.virustotal.com/api/v3/files/"+md5hashed
    response = request.resquest("GET", url, headers = headers)
    return response





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
