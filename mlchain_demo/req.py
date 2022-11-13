import requests

url = "http://localhost:8001/call/predict"

payload={}
files=[
  ('x',('Screenshot from 2022-10-16 16-48-40.png', open('/home/tienviper/Pictures/Screenshot from 2022-10-16 16-48-40.png','rb'),'image/png'))
]
headers = {
  'accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
