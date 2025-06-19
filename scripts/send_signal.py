# scripts/send_signal.py
import subprocess

def send_signal_group_message(sender_number, group_id, message):
    cmd = [
        "signal-cli", 
        "-u", sender_number,
        "send",
        "-m", message,
        "--group", group_id
    ]

    print(f"📨 Sending message to Signal group...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ Group message sent successfully!")
    else:
        print("❌ Failed to send group message.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
