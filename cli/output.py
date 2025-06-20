from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from scripts.prank_payloads import run_all_pranks, run_alpha_pranks
from utils.messaging import send_signal_message
from utils.certificate_generator import add_name_to_cert
from pathlib import Path
import os
import platform
import subprocess

console = Console()

def open_file(filepath: Path):
    """Cross-platform file opener."""
    try:
        if platform.system() == "Windows":
            os.startfile(filepath)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", filepath])
        else:  # Linux or others
            subprocess.run(["xdg-open", filepath])
    except Exception as e:
        console.print(f"[red]⚠️ Could not open file: {filepath} ({e})[/red]")

def show_results(result: dict):
    user_name = result.get("user_name", "Unknown Operative")
    score = result["score"]
    max_score = result["max_score"]
    label = result["label"]
    probability = result["probability"]
    title = result.get("title", "🌀 Enigmatic Unknown")

    # Emoji Meter Bar
    fill = "🟥" if label.lower() == "cuckman" else "🟩"
    empty = "⬛"
    meter = fill * score + empty * (max_score - score)

    # Header Display
    if label.lower() == "cuckman":
        console.print(Text("\n🔒 FINAL VERDICT: CUCKMAN 🔒", style="bold red"))
    else:
        console.print(Text("\n💪 FINAL VERDICT: ALPHAMAN 💪", style="bold green"))

    # Archetype Details
    console.print(f"🎭 Archetype: {title}", style="bold yellow")
    console.print(f"📊 CuckScore™: {score} / {max_score}", style="bold yellow")
    console.print(f"🧠 Cuckability: {probability:.0%}", style="bold cyan")
    console.print(f"📉 Meter: {meter}\n", style="bold magenta")

    if label.lower() == "cuckman":
        console.print("🔻 Consider removing the cuck chair. And the Signal app.")
        run_all_pranks()

        # 🎓 Generate and open certificates
        cert1 = add_name_to_cert(
            template_path=Path("assets/GCUCK_Certification.png"),
            user_name=user_name,
            save_as=f"GCUCK_Cert_{user_name.replace(' ', '_')}.png",
            name_coords=(440, 280)
        )

        cert2 = add_name_to_cert(
            template_path=Path("assets/BS_Cuckology.png"),
            user_name=user_name,
            save_as=f"SignalState_BS_{user_name.replace(' ', '_')}.png",
            name_coords=(430, 360)
        )

        console.print(Panel.fit(
            f"🎉 Your certifications are ready:\n\n"
            f"📜 GCUCK Cert: {cert1.resolve()}\n"
            f"🎓 B.S. in Cuckology: {cert2.resolve()}",
            title="CREDENTIALS EARNED",
            border_style="bold green"
        ))

        open_file(cert1)
        open_file(cert2)

    else:
        console.print("🔺 Keep dominating, Alpha. But beware the fedoras.")
        run_alpha_pranks()

    # ✅ Signal Broadcast
    sender = "+14054086698"
    group_id = "rVneiUAk6hTvBwDt66VRuKs0NCtk7PaU6rmVF+11de0="

    message = f"""[CuckBayes Broadcast Alert: {user_name}'s results are in!]
Archetype: {title}
CuckScore: {score}/{max_score} | Cuckability: {probability:.0%}
Verdict: {label.upper()}

Degree awarded: B.S. in Cuckological Sciences
Signal Activity: Detected
Chair Status: Confirmed Cuckchair
ICS Cyber Readiness: Moderate

Message auto-certified by Signal State University.
This transmission brought to you by CuckBayes™."""

    send_signal_message(sender, group_id, message, is_group=True)
