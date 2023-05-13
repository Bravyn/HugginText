#this a function to make inferences fro the hugging face t5 model api
import requests
import os
AUTH = os.environ['AUTH']

API_URL = "https://api-inference.huggingface.co/models/t5-base"
headers = {"Authorization": f"Bearer {AUTH}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "translate English to French: hello",
})
print(output[0]['translation_text'])