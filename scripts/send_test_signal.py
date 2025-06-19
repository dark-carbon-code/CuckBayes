import subprocess
import shutil

# Locate signal-cli binary
signal_cli = shutil.which("signal-cli") or shutil.which("signal-cli.cmd")
if not signal_cli:
    raise RuntimeError("signal-cli not found. Ensure it's installed and in your PATH.")

sender = "+14054086698"
recipient = "+14054086698"

# One-line message (no line breaks)
message = (
    "📡 Test from CuckBayes-CLI | ✅ Signal working | 🎓 GCUCK Engine operational."
)

# Proper command format
cmd = [
    signal_cli,
    "-u", sender,
    "send",
    "-m", message,
    "--", recipient
]

# Print full command for debug
print("Full command:")
print(" ".join(f'"{arg}"' if " " in arg else arg for arg in cmd))
print()

# Run
print(f"Sending message to {recipient}...")
result = subprocess.run(cmd, capture_output=True, text=True)

# Results
if result.returncode == 0:
    print("✅ Message sent successfully!")
else:
    print("❌ Failed to send message.")
    print("STDOUT:", result.stdout.strip())
    print("STDERR:", result.stderr.strip())
