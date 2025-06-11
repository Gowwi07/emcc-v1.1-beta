import requests
import json

def stream_phi3(prompt, callback):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": True
    }

    with requests.post(url, headers=headers, json=payload, stream=True) as response:
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode('utf-8'))
                    if "response" in data:
                        callback(data["response"])
                except json.JSONDecodeError:
                    pass
