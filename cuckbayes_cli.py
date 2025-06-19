from rich.console import Console
from cli.banner import render_intro_banner
from cli.archetype_builder import run_archetype_builder
from model.predictor import predict_character
from cli.output import show_results

if __name__ == "__main__":
    console = Console()

    render_intro_banner()  # 🖼️ Display animated ASCII intro banner

    # Ask for name input
    user_name = input("\n📛 Enter your name for official broadcast certification: ").strip()

    # Run quiz
    traits = run_archetype_builder()
    traits["user_name"] = user_name

    # Run prediction
    result = predict_character(traits)
    result["user_name"] = user_name

    # Show results & broadcast
    show_results(result)
