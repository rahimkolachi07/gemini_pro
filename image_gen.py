import requests

url = "https://arimagesynthesizer.p.rapidapi.com/generate"

payload = {
	"prompt": "dolar, yüzde, lira, rezerv, para",
	"id": "12345",
	"width": "768",
	"height": "768",
	"inferenceSteps": "50",
	"guidanceScale": "7.5",
	"img2img_strength": "0.75"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "<REQUIRED>",
	"X-RapidAPI-Host": "arimagesynthesizer.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())