import os
os.environ["PATH"] += os.pathsep + r"C:\Users\scott\scoop\shims"

import subprocess
import shutil

def send_signal_message(sender, recipient, message, is_group=False):
    signal_cli = shutil.which("signal-cli") or shutil.which("signal-cli.cmd")
    if not signal_cli:
        print("⚠️ signal-cli not found. Skipping message send.")
        return

    if is_group:
        cmd = [
            signal_cli,
            "-u", sender,
            "send",
            "-g", recipient,
            "-m", message
        ]
    else:
        cmd = [
            signal_cli,
            "-u", sender,
            "send",
            "-m", message,
            "--", recipient
        ]

    print(f"📨 Sending Signal message via: {signal_cli}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ Signal message sent successfully!")
    else:
        print("❌ Failed to send Signal message.")
        print("STDOUT:", result.stdout.strip())
        print("STDERR:", result.stderr.strip())
