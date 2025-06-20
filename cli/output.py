from rich.console import Console
from rich.text import Text
from scripts.prank_payloads import run_all_pranks, run_alpha_pranks
from utils.messaging import send_signal_message  # ✅ Group-ready import

console = Console()

def show_results(result: dict):
    user_name = result.get("user_name", "Unknown Operative")
    score = result["score"]
    max_score = result["max_score"]
    label = result["label"]
    probability = result["probability"]
    title = result.get("title", "🌀 Enigmatic Unknown")

    # Emoji Meter Bar
    fill = "🟥" if label == "Cuckman" else "🟩"
    empty = "⬛"
    meter = fill * score + empty * (max_score - score)

    # Header Display
    if label == "Cuckman":
        console.print(Text("\n🔒 FINAL VERDICT: CUCKMAN 🔒", style="bold red"))
    else:
        console.print(Text("\n💪 FINAL VERDICT: ALPHAMAN 💪", style="bold green"))

    # Archetype Details
    console.print(f"🎭 Archetype: {title}", style="bold yellow")
    console.print(f"📊 CuckScore™: {score} / {max_score}", style="bold yellow")
    console.print(f"🧠 Probability: {probability:.0%}", style="bold cyan")  # ✅ Updated label
    console.print(f"📉 Meter: {meter}\n", style="bold magenta")

    # Flavor Text and Prank Payloads
    if label == "Cuckman":
        console.print("🔻 Consider removing the cuck chair. And the Signal app.")
        run_all_pranks()  # 🔥 Trigger CUCK pranks
    else:
        console.print("🔺 Keep dominating, Alpha. But beware the fedoras.")
        run_alpha_pranks()  # 🔥 Trigger ALPHA pranks

    # ✅ Signal Broadcast
    sender = "+14054086698"  # Your registered Signal number
    group_id = "rVneiUAk6hTvBwDt66VRuKs0NCtk7PaU6rmVF+11de0="  # Signal group ID

    message = f"""[CuckBayes Broadcast Alert: {user_name}'s results are in!]
Archetype: {title}
CuckScore: {score}/{max_score} | Probability: {probability:.0%}
Verdict: {label.upper()}

Degree awarded: B.S. in Cuckological Sciences
Signal Activity: Detected
Chair Status: Confirmed Cuckchair
ICS Cyber Readiness: Moderate

Message auto-certified by Signal State University.
This transmission brought to you by CuckBayes™."""

    send_signal_message(sender, group_id, message, is_group=True)
