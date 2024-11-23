import requests

url = "http://127.0.0.1:5000/process"
data = {"message": "Tell me about world finance in simple words with some latest stats"}
response = requests.post(url, json=data)

print(response.json())