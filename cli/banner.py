# cli/banner.py

import time
import os
import platform
import random
import threading
from shutil import get_terminal_size
from rich.console import Console
from rich.text import Text
from rich.style import Style

console = Console()

colors = ["magenta", "purple4", "cyan", "deep_sky_blue1", "blue", "turquoise2"]

banner_lines = [
    "  ______  __    __    ______  __  ___ .______        ___   ____    ____  _______     _______.",
    " /      ||  |  |  |  /      ||  |/  / |   _  \\      /   \\  \\   \\  /   / |   ____|   /       |",
    "|  ,----'|  |  |  | |  ,----'|  '  /  |  |_)  |    /  ^  \\  \\   \\/   /  |  |__     |   (----`",
    "|  |     |  |  |  | |  |     |    <   |   _  <    /  /_\\  \\  \\_    _/   |   __|     \\   \\    ",
    "|  `----.|  `--'  | |  `----.|  .  \\  |  |_)  |  /  _____  \\   |  |     |  |____.----)   |   ",
    " \\______| \\______/   \\______||__|\\__\\ |______/  /__/     \\__\\  |__|     |_______|_______/    ",
    "                                                                                             "
]

def play_intro_sound():
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("assets/cuckbayes_theme.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        console.print(f"[yellow]⚠️ Could not play intro theme: {e}[/yellow]")

def type_banner(lines, delay=0.07):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, line in enumerate(lines):
        style = Style(color=colors[i % len(colors)], bold=True)
        console.print(Text(line, style=style))
        time.sleep(delay)

def flicker_final(lines):
    for _ in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        if random.random() > 0.4:
            for line in lines:
                flicker_style = Style(color=random.choice(colors), bold=True)
                console.print(Text(line, style=flicker_style))
        time.sleep(random.uniform(0.1, 0.2))
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, line in enumerate(lines):
        style = Style(color=colors[i % len(colors)], bold=True)
        console.print(Text(line, style=style))
    console.print(Text(">> CuckBayes: A Serious Tool for the Serious Cuck <<", style="bold magenta"))

def render_intro_banner():
    # Start theme music in background
    threading.Thread(target=play_intro_sound, daemon=True).start()

    width = get_terminal_size().columns
    divider = "═" * width

    console.print(f"[bold blue]{divider}")
    console.print(Text("🧠 CuckBayes™".center(width), style="bold magenta"))
    console.print(Text("Bayesian Archetype Classification Engine".center(width), style="italic cyan"))
    console.print(f"[bold blue]{divider}")
    time.sleep(0.8)

    type_banner(banner_lines)
    time.sleep(0.5)
    flicker_final(banner_lines)

    animated_lines = [
        ">> Signal is active...",
        ">> Bayesian priors loaded...",
        ">> Memetic payloads unlocked...",
        ">> Establishing trust boundary...",
        ">> Retrieving Cuckman/Alphaman models...",
        ">> Finalizing archetype scaffolding...",
        "[bold green]>> Initialization Complete.[/bold green]",
    ]

    for line in animated_lines:
        console.print(line.center(width))
        time.sleep(0.4)

    console.print("\n" + "⌛ Launching the test sequence...".center(width), style="bold yellow")
    time.sleep(1.2)
