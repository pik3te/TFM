import requests
import hashlib

apikey = open("../../vtoken", "r").read().rstrip('\n')
file_payload = open("../../dataset/Objective_See/Ventir/Ventir", "rb").read()

md5Hash = hashlib.md5(file_payload)
md5Hashed = md5Hash.hexdigest()

print(md5Hashed)

url = "https://www.virustotal.com/api/v3/files/"+md5Hashed

print(url)

payload = file_payload

headers = {
    "Accept": "application/json",
    "x-apikey": apikey,
}

response = requests.request("GET", url, headers=headers)


print(response.text)
