# prank_payloads.py
from time import sleep
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- CUCKMAN PAYLOADS ---

def fake_ransomware_screen():
    console.print(Panel.fit(
        "[bold red]🔐 SignalRansom v1.7.3 Activated[/bold red]\n"
        "Your dignity has been encrypted.\n"
        "All Signal chats, gym mirror selfies, and the cuckchair registry are now locked.\n\n"
        "To restore access, send 3 ETH to Signal State University's finance office.\n"
        "Time remaining: [bold yellow]∞[/bold yellow] (because this is fake)\n",
        title="RANSOMWARE DETECTED", border_style="red"))
    sleep(2)
    console.print("\n💡 Tip: Maybe uninstall Signal while you're at it.\n")

def fake_ics_malware_payload():
    console.print(Panel.fit(
        "[bold magenta]🛠️ PLCreep.A ICS Payload Engaged[/bold magenta]\n"
        "Reverse cuckchain initiated.\n"
        "Exploiting:\n"
        "- Siemens C7-633\n"
        "- Allen-Bradley SLC-69\n"
        "- Honeywell HONEYPOT 9000\n\n"
        "EtherCuck™ uplink established. Modbus compromised.\n",
        title="ICS ANOMALY", border_style="magenta"))
    sleep(2)
    console.print("📉 SCADA confidence levels: [bold red]0%[/bold red]\n")

def cuckshell_empire():
    console.print(Panel.fit(
        "[bold blue]🧠 CuckShell Empire - PowerSplunk Framework Loaded[/bold blue]\n"
        "> Import-Module 🪑\n"
        "> Invoke-Cuck -Target 'Living Room Chair'\n"
        "> Start-Recon -SpouseStatus\n",
        title="CUCKSHELL EMPIRE", border_style="blue"))
    sleep(1.5)
    console.print("\n📦 Module loaded: cuckchair.ps1\n")
    sleep(1)
    console.print("🎯 Target acquired: IKEA POÄNG Chair\n")

def cuckdropper_stage1():
    console.print(Panel.fit(
        "[bold green]🚨 CuckDropper.exe Stage 1: Initializing Payload[/bold green]\n"
        "Embedding cuckception routines...\n"
        "Spawning AlphaMan decoy process...\n"
        "Uploading meme telemetry to /dev/null\n",
        title="CUCKDROPPER", border_style="green"))
    sleep(1.5)
    console.print("🔃 Callback to GCUCK Command & Control complete.\n")

def rootcuck_install():
    console.print(Panel.fit(
        "[bold dark_red]🔧 Installing RootCuck.sys...[/bold dark_red]\n"
        "Rootkit signature: CUCK-1337-BOOT\n"
        "Persistence level: BIOS+UEFI+Wi-Fi toaster\n\n"
        "Hidden from Task Manager, but not from shame.\n",
        title="ROOTCUCK INSTALLER", border_style="dark_red"))
    sleep(1.5)
    console.print("📁 RootCuck.sys planted in /System32/Chairs\n")

def fake_network_scan():
    console.print(Panel.fit(
        "[bold yellow]🌐 Running nmap --script=cuckscan on LAN...[/bold yellow]\n"
        "Discovered targets:\n"
        " - 192.168.0.69: Open Port 88 (CuckService)\n"
        " - 192.168.1.42: Open Port 1337 (AlphaStream)\n"
        " - 192.168.1.13: Closed port (WifeSecProxy)\n",
        title="NETWORK SCAN ACTIVE", border_style="yellow"))
    sleep(2)
    console.print("🛰️ Sending payload to all known cuckchairs in broadcast domain...\n")

def run_all_pranks():
    fake_ransomware_screen()
    fake_ics_malware_payload()
    cuckshell_empire()
    cuckdropper_stage1()
    rootcuck_install()
    fake_network_scan()

# --- ALPHAMAN PAYLOADS (Cyber Parody Edition) ---

def broSploit_launch():
    console.print(Panel.fit(
        "[bold red]💥 broSploit v9.11 Activated 💥[/bold red]\n"
        "Chainloading 0-day vulnerabilities in outdated fitness apps.\n"
        "Exploit: CVE-6969-FLEX — buffer overflow on bicep curls.\n"
        "Post-exploitation module: 'shirtless_root.exe'\n",
        title="BROSploit Framework", border_style="red"))
    sleep(2)
    console.print("🧠 Operator: 'AlphaMan1337' verified via mirror reflection\n")

def swoleC2_beacon():
    console.print(Panel.fit(
        "[bold green]🛰️ SwoleC2 Beacon Detected[/bold green]\n"
        "Payload stage: LiverStack Persistence\n"
        "Beacon frequency: Every 3 reps\n"
        "Kill switch: Never\n",
        title="C2 SERVER: GymCentral", border_style="green"))
    sleep(2)
    console.print("📡 C2 Callout IP: 10.0.0.ALPHA\n")

def redteam_romance():
    console.print(Panel.fit(
        "[bold magenta]❤️ Adversary Simulation: Tactic - Seduction ❤️[/bold magenta]\n"
        "Emulating threat actor: 'APT69 - Bromantic Leopard'\n"
        "Initial Access: Tinder phishing\n"
        "Privilege Escalation: Compliment escalation chain\n",
        title="ALPHAMAN TTPs", border_style="magenta"))
    sleep(2)
    console.print("🔥 Successfully bypassed all emotional firewalls\n")

def alpha_payload_injector():
    console.print(Panel.fit(
        "[bold cyan]🚀 AlphaInjector v3.14 Injecting Payload...[/bold cyan]\n"
        "Injecting test into:\n"
        " - Testosterone.sys\n"
        " - ProteinShake.dll\n"
        " - CryptoWallet.nudes\n",
        title="PAYLOAD DELIVERY SYSTEM", border_style="cyan"))
    sleep(2)
    console.print("💉 Hormone injection verified. Beard growth: 17% complete.\n")

def gymbot_telemetry():
    console.print(Panel.fit(
        "[bold yellow]📈 gymbot.exe Collecting Metrics...[/bold yellow]\n"
        "Sensors online:\n"
        "- SweatRate\n"
        "- GruntVolume\n"
        "- Mirror Check Frequency\n",
        title="OT DEVICE: Gym ICS Node", border_style="yellow"))
    sleep(2)
    console.print("⚙️ Reporting to Prometheus: /metrics/alpha_flux\n")

def run_alpha_pranks():
    broSploit_launch()
    swoleC2_beacon()
    redteam_romance()
    alpha_payload_injector()
    gymbot_telemetry()
