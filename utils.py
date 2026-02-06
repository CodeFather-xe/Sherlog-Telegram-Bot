import json

def load_config(filename="config.json"):
    """Loads the configuration from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode {filename}. Please check its format.")
        return None

def load_content(filename="content.json"):
    """Loads content from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create it.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode {filename}. Please check its format.")
        return None
