# 🧠 CuckBayes™

> The world's first Bayesian-powered archetype classifier.  
> Now featuring Signal integration, prank payloads, interactive AI narration, and certification from prestigious fictional universities in cybersecurity.

![CuckBayes Icon](assets/cuckbayes.png)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

---

## 🤖 What is CuckBayes?
**CuckBayes™** is a parody command-line application that classifies users into archetypes based on lifestyle, technology habits, and OT/IT cybersecurity affinities. Your answers are fed into a Bayesian scoring engine that produces a final classification:

- 🔒 **Cuckman** — Signal-using, chair-watching, ICS-overwhelmed softshells  
- 💪 **Alphaman** — Grid-hardening, OT-pentesting, protein-shaking dominators

### Now Featuring:
- **🗣️ CuckGPT** — A sarcastic CLI narrator powered by a local Ollama LLM
- **🎶 Theme Music** — Terminal-width intro banner and optional music
- **💣 Prank Payloads** — For both Cuckman and Alphaman types
- **📡 Signal Integration** — For broadcasting results to your group
- **📜 Certification** — Auto-generated PNG certs with fictional degrees

---

## 🧰 Features
- ✅ Interactive CLI quiz (with `rich` and `InquirerPy`)
- 🤖 Real-time AI commentary via `Ollama` and `llama3` or `mistral` model
- 🎓 Auto-generated certification PNGs with your name
- 📡 Optional Signal CLI messaging to preconfigured group
- 💣 Prank payloads for **both** Cuckman and Alphaman results
- 🧠 Bayesian logic-based scoring system
- 🖼️ Mascots, icons, and certificate templates included
- 📂 Cross-platform file opening of generated certs
- 🪖 Malware-themed jokes recognizable to OT/IT cybersecurity pros
- 🎵 Intro theme music powered by `pygame` (optional)

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) (required for CuckGPT responses)
- Optional: `signal-cli` for messaging
- Optional: `pygame` for theme music

### Clone the repo
```bash
git clone https://github.com/dark-carbon-code/CuckBayes.git
cd CuckBayes
````

### Install dependencies

```bash
pip install -r requirements.txt
```

### Pull Ollama model

You must have Ollama installed. Pull a compatible model like `llama3` or `mistral`:

```bash
ollama pull llama3
```

### (Optional) macOS Setup Script

```bash
chmod +x setup_mac.sh
./setup_mac.sh
```

---

## 🧪 How to Use

```bash
python cuckbayes_cli.py
```

You’ll be prompted to:

1. Enter your name
2. Answer a series of lifestyle/cybersecurity questions
3. Watch the intro banner and hear the music (optional)
4. Interact with **CuckGPT** while answering (LLM-powered)
5. Receive final classification (Cuckman or Alphaman)
6. Trigger prank payloads and Signal broadcast
7. (If Cuckman) Generate and auto-open two personalized PNG certificates

---

## 📡 Signal Integration (Optional)

To enable Signal broadcast:

1. Install [`signal-cli`](https://github.com/AsamK/signal-cli)
2. Register your phone via QR code
3. Update phone number and group ID in `utils/messaging.py`

---

## 🐳 Docker Support (Coming Soon)

Containerized version with all dependencies, model, and sandboxing.

---

## 📜 License

MIT License. For parody use only.

---

## 🙌 Credits

Built by cyber nerds for cyber nerds. Inspired by:

* MITRE ATT\&CK & ICS memes
* Cybersecurity war stories
* Internet archetypes and satire
* Bad Bayesian math, great jokes

> *"Cuculus Semper Vigilantes" — Signal State University Motto*




