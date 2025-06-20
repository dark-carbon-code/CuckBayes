# 🧠 CuckBayes™

> The world's first Bayesian-powered archetype classifier.  
> Now featuring Signal integration, prank payloads, and official certification from the most prestigious fictional universities in cybersecurity.

![CuckBayes Icon](assets/cuckbayes.png)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

---

## 🤖 What is CuckBayes?
**CuckBayes™** is a parody command-line application that classifies users into archetypes based on lifestyle, technology habits, and OT/IT cybersecurity affinities. Your answers are fed into a Bayesian scoring engine that produces a final classification:

- 🔒 **Cuckman** — Signal-using, chair-watching, ICS-overwhelmed softshells  
- 💪 **Alphaman** — Grid-hardening, OT-pentesting, protein-shaking dominators

You'll receive:
- A CuckScore™ with Probability
- Dynamic emoji meter visualization
- Optional Signal group broadcast
- Customized prank payloads for both archetypes
- And (if you're a Cuckman)... certified degrees from:
  - SANZ Technology Institute (GCUCK Certification)
  - Signal State University (B.S. in Cuckology)

---

## 🧰 Features
- ✅ Interactive CLI quiz (with `rich` and `InquirerPy`)
- 🎓 Auto-generated certification PNGs with your name
- 📡 Optional Signal CLI messaging to preconfigured group
- 💣 Prank payloads for **both** Cuckman and Alphaman results
- 🧠 Bayesian logic-based scoring system
- 🖼️ Mascots, icons, and certificate templates included
- 📂 Cross-platform file opening of generated certs
- 🪖 Malware-themed jokes recognizable to OT/IT cybersecurity pros

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Windows, macOS, or Linux
- Optional (for Signal integration): `signal-cli`

### Clone the repo
```bash
git clone https://github.com/dark-carbon-code/CuckBayes.git
cd CuckBayes
````

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Use

Run the main CLI:

```bash
python cuckbayes_cli.py
```

You’ll be prompted to:

1. Enter your name
2. Answer a series of lifestyle/cybersecurity questions
3. Receive final classification (Cuckman or Alphaman)
4. Trigger prank payloads and Signal broadcast
5. (If Cuckman) Generate and auto-open two personalized PNG certificates

---

## 📁 Project Structure

```
CuckBayes/
├── assets/                  # Mascots, icons, certificate templates
├── cli/                     # CLI logic & outputs
│   ├── archetype_builder.py
│   ├── banner.py
│   └── output.py
├── model/                   # Prediction logic (Bayesian)
│   └── predictor.py
├── scripts/                 # Pranks + Signal integration
│   ├── prank_payloads.py
│   └── send_signal.py
├── utils/                   # Cert gen and messaging
│   ├── certificate_generator.py
│   └── messaging.py
├── generated_certs/        # Output certs
├── requirements.txt
├── cuckbayes_cli.py         # 🔥 Main CLI entry point
└── README.md
```

---

## 🎓 Example Output

```
💪 FINAL VERDICT: ALPHAMAN 💪
🎭 Archetype: Grid Dominator
📊 CuckScore™: 3 / 14
🧠 Cuckability: 9%
📉 Meter: 🟩🟩🟩⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛

🔺 Keep dominating, Alpha. But beware the fedoras.

[CuckBayes Broadcast Alert: Scott Bowman]
Archetype: Grid Dominator
CuckScore: 3/14 | Cuckability: 9%
Verdict: ALPHAMAN

Degree awarded: N/A (Too alpha to enroll)
Signal Activity: Dormant
Chair Status: Thrown into bonfire

Message auto-certified by Signal State University.
This transmission brought to you by CuckBayes™.
```

---

## 📡 Signal Integration (Optional)

To enable Signal broadcast:

1. Install [`signal-cli`](https://github.com/AsamK/signal-cli)
2. Link your number via QR code
3. Update your phone number and group ID in `utils/messaging.py`

---

## 🐳 Docker Support (Coming Soon)

A `Dockerfile` will soon allow you to containerize the app and run it in a secure sandboxed environment with all prank payloads contained.

---

## 📜 License

MIT License. Satirical use only.
Not affiliated with actual certifying bodies or institutions of higher learning.

---

## 🙌 Credits

Built by cyber nerds for cyber nerds.
Inspired by:

* MITRE ATT\&CK adversary names
* Malware, red teaming, and Signal chat chaos
* Bad Bayesian math and great memes

> *"Cuculus Semper Vigilantes" — Signal State University Motto*

