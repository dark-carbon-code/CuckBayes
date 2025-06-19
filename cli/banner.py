import time
import os
import random
from rich.console import Console
from rich.text import Text
from rich.style import Style

console = Console()

banner_lines = [
    "  ______  __    __    ______  __  ___ .______        ___   ____    ____  _______     _______.",
    " /      ||  |  |  |  /      ||  |/  / |   _  \\      /   \\  \\   \\  /   / |   ____|   /       |",
    "|  ,----'|  |  |  | |  ,----'|  '  /  |  |_)  |    /  ^  \\  \\   \\/   /  |  |__     |   (----`",
    "|  |     |  |  |  | |  |     |    <   |   _  <    /  /_\\  \\  \\_    _/   |   __|     \\   \\    ",
    "|  `----.|  `--'  | |  `----.|  .  \\  |  |_)  |  /  _____  \\   |  |     |  |____.----)   |   ",
    " \\______| \\______/   \\______||__|\\__\\ |______/  /__/     \\__\\  |__|     |_______|_______/    ",
    "                                                                                             "
]

colors = ["magenta", "purple4", "cyan", "deep_sky_blue1", "blue", "turquoise2"]

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
    type_banner(banner_lines)
    time.sleep(0.5)
    flicker_final(banner_lines)
