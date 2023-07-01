import requests
from secretKey import KEY 
import json 


def askGPT(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + KEY ,
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
        data = json.loads(response.text)
        return data['choices'][0]['text']
    except Exception as e:
        print(e)
        return "ERROR OCCURED"