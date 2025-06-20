# utils/certificate_generator.py

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Define paths
ASSETS_DIR = Path("assets")
OUTPUT_DIR = Path("generated_certs")
OUTPUT_DIR.mkdir(exist_ok=True)

def add_name_to_cert(template_path: Path, user_name: str, save_as: str, name_coords=(100, 100), font_size=48) -> Path:
    """
    Adds a user's name to a certificate template and saves it.

    Args:
        template_path (Path): Path to the base certificate PNG.
        user_name (str): Name to render on the certificate.
        save_as (str): Filename to save the generated cert as (e.g., "cert_JohnDoe.png").
        name_coords (tuple): (x, y) pixel coordinates to position the name.
        font_size (int): Font size to use for the name text.

    Returns:
        Path: Full path to the generated certificate image.
    """
    try:
        image = Image.open(template_path).convert("RGBA")
        draw = ImageDraw.Draw(image)

        # Try to load Arial or fallback
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except OSError:
            font = ImageFont.load_default()

        draw.text(name_coords, user_name, font=font, fill=(0, 0, 0, 255))

        output_path = OUTPUT_DIR / save_as
        image.save(output_path)
        return output_path

    except Exception as e:
        raise RuntimeError(f"Failed to generate certificate: {e}")
