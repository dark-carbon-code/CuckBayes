# utils/cuckgpt_agent.py

import subprocess
import sys
import time
import io
import threading

# Force UTF-8 output to handle emojis (Windows-safe)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def typing_indicator(stop_event):
    """
    Simulates a 'CuckGPT is typing...' animation in a separate thread.
    """
    symbols = ["💬   ", "💬.  ", "💬.. ", "💬..."]
    i = 0
    while not stop_event.is_set():
        print(f"\r🤖 CuckGPT is typing {symbols[i % len(symbols)]}", end="", flush=True)
        time.sleep(0.5)
        i += 1
    print("\r" + " " * 40 + "\r", end="", flush=True)  # Clear line

def stream_cuckgpt(user_input, model="llama3"):
    prompt = f"""
You are CuckGPT — the official narrator of the CuckBayes CLI. Your personality is:

- Sarcastic and dry-humored
- Aware of the Cuckman vs. Alphaman archetypes
- Mildly condescending but always funny
- Self-aware like Marvin from Hitchhiker’s Guide, but not clinically depressed
- Cybersecurity-fluent with a disdain for poser infosec takes

The user is answering a quiz question. Respond with a one-liner comment after each answer.

User's latest input: "{user_input}"

Respond as CuckGPT:
"""

    try:
        process = subprocess.Popen(
            ["ollama", "run", model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        if process.stdin:
            process.stdin.write(prompt)
            process.stdin.close()

        # Typing animation
        stop_typing = threading.Event()
        t = threading.Thread(target=typing_indicator, args=(stop_typing,))
        t.start()

        response_lines = []
        if process.stdout:
            for line in process.stdout:
                response_lines.append(line.strip())

        process.wait()
        stop_typing.set()
        t.join()

        # Join and clean final output
        response_text = " ".join(response_lines).strip()
        print(f"\n🤖 CuckGPT: {response_text}\n", flush=True)

    except Exception as e:
        stop_typing.set()
        print(f"\n[CuckGPT Error] {str(e)}")
