# 🧠 AI Multi-Agent Conversation (Ollama)

Projet expérimental qui simule une conversation entre deux intelligences artificielles locales utilisant Ollama.

---

# 🤖 Concept

Deux IA discutent ensemble en boucle infinie :

- 🧠 IA 1 : Llama  
- 🤖 IA 2 : Emma (Dolphin)

Chaque IA répond à l’autre, créant une discussion autonome et continue.

---

# ⚙️ Fonctionnement

1. IA 1 génère une réponse
2. IA 2 répond à IA 1
3. Les réponses sont échangées en boucle
4. Tout est sauvegardé dans `think.txt`

---

# 🧰 Technologies utilisées

- Python 3
- requests
- Ollama API (local)
- Modèle : `huihui_ai/dolphin3-abliterated:latest`

---

# 📁 Structure du projet

```text
.
├── main.py
├── requirements.txt
└── think.txt
