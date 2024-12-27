import pyfiglet
import random
import json
from pydantic import BaseModel, Field

class FontData(BaseModel):
    fonts: list[str] = Field(..., description="List of available fonts")

class DynamicCliFont:
    def __init__(self, json_path: str):
        self.fonts = self.load_fonts_from_json(json_path)
        
    def load_fonts_from_json(self, json_path: str):
        with open(json_path, "r") as json_file:
            raw_data = json.load(json_file)
            validated_data = FontData(**raw_data)
            return validated_data.fonts

    def select_random_font(self):
        selected_font = random.choice(self.fonts)
        return selected_font

    def generate_ascii_art(self, text: str):
        selected_font = self.select_random_font()
        figlet = pyfiglet.Figlet(font=selected_font)
        ascii_art = figlet.renderText(text)
        return ascii_art

if __name__ == '__main__':
    cli_font = DynamicCliFont("fonts.json")
    ascii_art = cli_font.generate_ascii_art("ASCII Art")
    print(ascii_art)
