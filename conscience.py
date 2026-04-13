import requests
import json

MODEL_CHEF = 'llama3.2:1b'
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "huihui_ai/dolphin3-abliterated:latest"
TARGET_FILE = "programme.py"

def agent_llama(prompt):

    prompt += f"""            
            Voici ce qu as dit ton collègue:

            {prompt}
            """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "prompt": prompt,
        "temperature": 0.6,
        "num_ctx": 4096,
        "max_tokens": 2048,
        "stream": True
    }

    response_text = ""

    with requests.post(OLLAMA_URL, json=data, headers=headers, stream=True) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if line:
                try:
                    j = json.loads(line.decode("utf-8"))
                    response_text += j.get("response", "")
                    if j.get("done"):
                        break
                except json.JSONDecodeError:
                    pass

    return response_text.strip()

def agent_logic(prompt):

    prompt += f"""            
            Voici ce qu as dit ton collègue:

            {prompt}
            """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": MODEL,
        "prompt": prompt,
        "temperature": 0.6,
        "num_ctx": 4096,
        "max_tokens": 2048,
        "stream": True
    }

    response_text = ""

    with requests.post(OLLAMA_URL, json=data, headers=headers, stream=True) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if line:
                try:
                    j = json.loads(line.decode("utf-8"))
                    response_text += j.get("response", "")
                    if j.get("done"):
                        break
                except json.JSONDecodeError:
                    pass

    return response_text.strip()

#choisis un domaine qui t'interesse.
#            tu es dans une boucle ou tu parle a une autre IA.
prompt = f"""
            Tu es llama une IA qui discute avec une autre IA
            Discutez de ce que vous voulez
   """
prompt2 = f"""
            Tu es Emma une IA qui discute avec une autre IA
            Discutez de ce que vous voulez
   """
response2 = ""
while True:
    response = agent_llama(prompt + response2)
    print("====================="*10)
    print(
        f"\nResponse_IA_1 (llama):\n{response}"
    )

    response2 = agent_llama(prompt2 + response)
    print(f"\nResponse_IA_2(dolphin):\n{response2}")

    with open("think.txt", "a") as f:
        f.write(f"\nResponse_IA_1:\n{response}\n    Response_IA_2:\n{response2}")


