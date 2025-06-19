# cuckbayes/cli/main.py

from cli.banner import render_intro_banner
from cli.archetype_builder import run_archetype_builder
from model.predictor import predict_character
from cli.output import show_results  # Handles final result display

def run_cli():
    # 1. Show intro banner
    render_intro_banner()

    # 2. Build archetype
    traits = run_archetype_builder()

    # 3. Predict character type
    result = predict_character(traits)

    # 4. Display styled result with emojis + color + archetype title
    show_results(result)
