#this a function to make inferences fro the hugging face t5 model api
import requests

API_URL = "https://api-inference.huggingface.co/models/t5-base"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "translate English to French: hello",
})
print(output)