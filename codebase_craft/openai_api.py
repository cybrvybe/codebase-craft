import os
import yaml
import sys
import openai
from . import config


def generate_template(project):
    # Load the directory structure from the yaml file
    with open("dir_structure.yaml", "r") as f:
        dir_structure = yaml.safe_load(f)

    # Use the OpenAI API to generate a generic template
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"Create a generic template from this directory structure:\n\n{dir_structure}",
        },
    ]

    openai.api_key = config.OPENAI_API_KEY
    response = openai.ChatCompletion.create(model="gpt-4.0-turbo", messages=messages)

    template = response["choices"][0]["message"]["content"]

    # Save the template to a yaml file
    with open("dir_structure_template.yaml", "w") as f:
        yaml.dump(template, f)
