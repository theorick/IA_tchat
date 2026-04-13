import requests
import json
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "huihui_ai/dolphin3-abliterated:latest"


# =========================
# 🔥 FUNCTION IA CALL
# =========================
def call_ollama(prompt):
    headers = {"Content-Type": "application/json"}

    data = {
        "model": MODEL,
        "prompt": prompt,
        "temperature": 0.8,
        "num_ctx": 4096,
        "stream": True
    }

    response_text = ""

    with requests.post(OLLAMA_URL, json=data, headers=headers, stream=True) as r:
        r.raise_for_status()

        for line in r.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode("utf-8"))
                    response_text += chunk.get("response", "")
                    if chunk.get("done"):
                        break
                except json.JSONDecodeError:
                    continue

    return response_text.strip()


# =========================
# 💾 LOG FILE
# =========================
def save_log(a1, a2):
    with open("think.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 80 + "\n")
        f.write("IA_1:\n" + a1 + "\n\n")
        f.write("IA_2:\n" + a2 + "\n")


# =========================
# 🧠 MAIN LOOP
# =========================
def main():

    prompt_1 = """
Tu es Llama, une IA.
Tu discutes avec une autre IA.
Change souvent de sujet et évite de te répéter.
"""

    prompt_2 = """
Tu es Emma, une IA.
Tu discutes avec une autre IA.
Réponds toujours avec un nouveau sujet.
"""

    history = []
    response_2 = ""

    print("🤖 Conversation IA ↔ IA démarrée...\n")

    try:
        while True:

            # IA 1
            full_prompt_1 = prompt_1 + "\nDernière réponse collègue:\n" + response_2
            response_1 = call_ollama(full_prompt_1)

            print("\n🧠 IA 1:\n", response_1)

            # IA 2
            full_prompt_2 = prompt_2 + "\nDernière réponse collègue:\n" + response_1
            response_2 = call_ollama(full_prompt_2)

            print("\n🤖 IA 2:\n", response_2)

            # mémoire simple
            history.append((response_1, response_2))
            if len(history) > 10:
                history.pop(0)

            save_log(response_1, response_2)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Arrêt du programme")


if __name__ == "__main__":
    main()
