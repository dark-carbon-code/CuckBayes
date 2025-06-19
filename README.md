# 🧠 CuckBayes™

> The world's first Bayesian-powered archetype classifier.  
> Now with Signal integration, prank payloads, and a B.S. in Cuckological Sciences™.

![CuckBayes Icon](assets/CuckBayes.png)

---

## 🤖 What is CuckBayes?

**CuckBayes™** is a satirical command-line application that classifies users as either:
- **🔒 Cuckman** – Signal-using, meme-absorbing, chair-watching types
- **💪 Alphaman** – Dominant, ICS-aligned, emotionally resilient apex predators

This tool leverages your responses to a highly questionable set of lifestyle and cybersecurity questions, and delivers a final verdict — complete with a Score, Probability, Archetype Title, and Signal broadcast to your friends.

---

## 🧰 Features

- ✅ **CLI-based Archetype Quiz** with trait scoring
- 🎨 **Animated ASCII banner intro**
- 📡 **Signal group broadcast integration**
- 💣 **Prank payload triggers** (be careful…)
- 🧠 **Bayesian-style scoring logic**
- 🖼️ **CuckBayes & CuckEyes mascots** in `assets/`

---

## 🖥️ How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/dark-carbon-code/CuckBayes.git
cd CuckBayes
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python cuckbayes_cli.py
```

---

## 🧪 Requirements

* Python 3.10+
* Optional: `signal-cli` (for Signal broadcast to work)

  * Must be installed and linked to a registered phone number
  * On Windows, `scoop install signal-cli` is recommended

---

## 📦 PyInstaller Build (Optional)

To build a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller cuckbayes_cli.py --onefile --icon=assets/CuckBayes.ico --name CuckBayes_v1
```

This will create an executable in the `dist/` folder.

---

## 🧾 Project Structure

```
CuckBayes/
├── cli/                 # CLI modules (banner, output, builder)
├── model/               # Predictor logic
├── scripts/             # Prank payloads, Signal scripts
├── utils/               # Messaging integration
├── assets/              # Project icons & mascots
├── data/                # Sample data (if needed)
├── cuckbayes_cli.py     # 🔥 Entry point
└── requirements.txt
```

---

## 📡 Signal Setup

If you want Signal integration:

1. [Install `signal-cli`](https://github.com/AsamK/signal-cli)
2. Link your number via QR code (see `scripts/gen_qr.py`)
3. Update `utils/messaging.py` with your phone number and group ID

---

## 🎓 Sample Broadcast Output

```
[CuckBayes Broadcast Alert: Scott]
Archetype: Signal-Based Softshell
CuckScore: 9/14 | Probability: 81%
Verdict: CUCKMAN

Degree awarded: B.S. in Cuckological Sciences
Signal Activity: Detected
Chair Status: Confirmed Cuckchair
ICS Cyber Readiness: Moderate

Message auto-certified by Signal State University.
This transmission brought to you by CuckBayes™.
```

---

## 🧠 Authors

* [@dark-carbon-code](https://github.com/dark-carbon-code) — Creator of chaos

---

## 📜 License

This project is licensed under the MIT License. Use responsibly (or don’t).

## 🙈 Disclaimer

This is a parody tool meant for humor, not diagnosis.
Use at your own psychological risk.


