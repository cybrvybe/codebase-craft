# utils/openai_api.py

import openai
import typer
from rich.console import Console
from rich.syntax import Syntax

openai.api_key = "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"

app = typer.Typer()


def generate_template(outline):
    """
    Generate a template using the GPT API.
    """
    # Convert the outline to a string
    outline_str = "\n".join(f"{k}: {v}" for k, v in outline.items())

    # Define the prompt
    prompt = f"Given the following outline of a codebase:\n\n{outline_str}\n\nPlease generate a JSON \
        representation of the directory structure for a new project based on this codebase. The JSON \
        should only include directories and files that would be included in a new project template. \
        Please exclude any files or folders that are specific to the current project and would not \
        be included in a new project. Your response should only include the JSON representation of \
        the directory structure, with no additional explanations or comments. Please format the JSON \
        with proper indentation for readability in a template"

    # Use the OpenAI API to generate a template
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the generated template from the response
    template = response["choices"][0]["message"]["content"]

    return template


@app.command()
def run_template_generation(outline):
    # Indicate the code generation process
    with Console().status("[bold green] Fetching responses from GPT API ...") as status:
        template = generate_template(outline)
        status.update("[bold green]Template generation complete!")

        return template


if __name__ == "__main__":
    app()
