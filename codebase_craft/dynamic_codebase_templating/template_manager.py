# dynamic_codebase_templating/template_manager.py
import json


def store_template(template, filename="template"):
    with open(f"{filename}.txt", "w") as f:
        json.dump(template, f)


def reformat_template(logger, filename="template"):
    with open(f"{filename}.txt", "r") as f:
        text_str = f.read()
        if text_str.startswith('"') and text_str.endswith('"'):
            text_str = text_str[1:-1]  # Remove the enclosing quotes
            text_str = text_str.replace('\\"', '"')  # Unescape the inner quotes
        text_str = text_str.replace("\\n", "\n").replace(
            '\\"', '"'
        )  # Remove extra backslashes

    json_obj = json.loads(text_str)

    logger.info("Reformatting files")

    with open(f"{filename}.json", "w") as f:
        json.dump(json_obj, f, indent=2)


def load_template(logger, filename="template"):
    with open(f"{filename}.json", "r") as f:
        content = f.read()
        try:
            # If the content is a string representation of a JSON object,
            # remove the enclosing quotes and parse it as JSON
            if content.startswith('"') and content.endswith('"'):
                content = content[1:-1]  # Remove the enclosing quotes
                content = content.replace('\\"', '"')  # Unescape the inner quotes
            json_obj = json.loads(content)
        except json.JSONDecodeError:
            logger.error(
                f"Could not parse JSON data in {filename}. Please check the file contents."
            )
            return None
        return json_obj
