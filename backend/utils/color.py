from PIL import Image
from collections import Counter


def extract_color_palette(image_path: str, k: int = 3) -> list[str]:
    image = Image.open(image_path).convert("RGB").resize((128, 128))
    pixels = list(image.getdata())
    common = Counter(pixels).most_common(k)
    return [f"rgb{rgb}" for rgb, _ in common]
