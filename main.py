#this a function to make inferences fro the hugging face t5 model api
import requests
import os
AUTH = os.environ['AUTH']

API_URL = "https://api-inference.huggingface.co/models/t5-base"
headers = {"Authorization": f"Bearer {AUTH}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_user_input():
  return input("\033[34mWhat would you like translated: \n\n\033[0m")

input = get_user_input()

print("\nTranslating to French, this might take some time...\n")

output = query({
	"inputs": f"translate English to French: {input}",
})

if output[0]['translation_text'] != KeyError:
  print(output[0]['translation_text'])
  print("\n")

else:
  print("There was a problem getting your translation...")
