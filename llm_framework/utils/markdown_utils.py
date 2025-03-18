from datetime import datetime
import os

def save_response_to_markdown(response, file_path, title):
    """Saves the response from the LLM to a markdown file with a specified title."""
    with open(file_path, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Model:** {response.model}\n")
        f.write(f"**Token usage:** {response.usage}\n\n")
        f.write(f"## Response\n\n")
        f.write(response.text)
        f.write("\n\n---\n")
        f.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")