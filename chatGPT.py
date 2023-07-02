import requests
import json 
from secret_key import API_KEY 

def askGPT(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
    }

    json_data = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'temperature': 1,
        'max_tokens': 256,
        'top_p': 1,
        'frequency_penalty': 0,
        'presence_penalty': 0,
    }

    try: 
        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
        response_data = json.loads(response.text)
        return response_data['choices'][0]['text']
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return "ERROR OCCURED"