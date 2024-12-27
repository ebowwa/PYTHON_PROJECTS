import os
import argparse
import gradio as gr
import pandas as pd
from groq import Groq
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_model", type=str)  # model path
    parser.add_argument("--n_gpus", type=int, default=1)  # n_gpu
    return parser.parse_args()

def predict(history, system_prompt, temperature, max_tokens, csv_file):
    instruction = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. "
    for human, assistant in history:
        instruction += 'USER: '+ human + ' ASSISTANT: '+ assistant + '</s>'
    problem = [instruction]
    stop_tokens = ["USER:", "USER", "ASSISTANT:", "ASSISTANT"]

    # Load the CSV data
    df = pd.read_csv(csv_file)

    # Iterate through the CSV data
    for _, row in df.iterrows():
        prompt = row['descr'] + " " + row['ascii_art']
        # ascii_art = row['ascii_art']
        client = Groq(
            api_key="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",
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
            max_tokens=max_tokens,
        )
        generated_text = chat_completion.choices[0].message.content
        history.append(("USER", prompt))
        history.append(("ASSISTANT", generated_text))
        for idx in range(len(generated_text)):
            yield generated_text[:idx+1]

    # Save the generated content to a JSON file
    with open("generated_content.json", "w") as f:
        json.dump(history, f)
if __name__ == "__main__":
    # args = parse_args()

    # history = []
    # system_prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."
    # temperature = 0.9
    # max_tokens = 1024
    # csv_file = "training/Groq/data.csv"

    # for output in predict(history, system_prompt, temperature, max_tokens, csv_file):
    #     print(output, end="")
        # history.append(("ASSISTANT", output))
    with open('generated_content.json', 'r') as file:
        data = json.load(file)
        reformatted_data = []
        for i in range(0, len(data), 2):
            instruction = "As a creator, describe how you would imagine this object in a dynamic scene."
            # breakpoint()
            input_data = data[i][1]
            output_data = data[i+1][1]
            reformatted_data.append({"instruction": instruction, "input": input_data, "output": output_data})
        with open("reformatted_dataset.json", "w") as f:
            json.dump(reformatted_data, f, indent=2)

        # df = pd.read_csv(csv_file)
        # result = []
        # # Iterate through the CSV data
        # for _, row in df.iterrows():
        #     prompt = row['descr'] + " " + row['ascii_art']
        #     result["input"] = prompt
        #     result["output"] = "test"
