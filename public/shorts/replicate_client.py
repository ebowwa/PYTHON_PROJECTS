import os
import replicate
import json
from pydantic import BaseModel
from typing import Dict, Optional

# Setting the API token

os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN

class Input(BaseModel):
    fps: int
    seed: int
    steps: int
    width: int
    height: int
    scheduler: str
    animations: str
    max_frames: int
    prompt_durations: Optional[str] = ""
    animation_prompts: str

def run_replicate(input_data: Dict) -> Dict:
    # Validate and parse the input data
    input_obj = Input(**input_data)
    input_dict = json.loads(input_obj.model_dump_json())

    # Call the replicate API
    output = replicate.run(
        "alaradirik/deforum-kandinsky-2-2:550e576a484886c105a5cf4ff09ac746e691ab473d12a6afe14eed23bc3bbe42",
        input=input_dict
    )

    return output

if __name__ == "__main__":
    # Example usage
    input_example = {
        "fps": 24,
        "seed": 17,
        "steps": 80,
        "width": 640,
        "height": 640,
        "scheduler": "euler_ancestral",
        "animations": "live | right | right | right | live",
        "max_frames": 72,
        "prompt_durations": "0.6 | 0.3 | 1 | 0.3 | 0.8",
        "animation_prompts": "winter forest, snowflakes, Van Gogh style | spring forest, flowers, sun rays, Van Gogh style | summer forest, lake, reflections on the water, summer sun, Van Gogh style | autumn forest, rain, Van Gogh style | winter forest, snowflakes, Van Gogh style"
    }

    result = run_replicate(input_example)
    print(result)
