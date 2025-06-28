import openai
from datetime import datetime

openai.api_key = "your-openai-api-key"

def analyze_squawk(squawk_text):
    prompt = f"""You are an expert aviation maintenance AI. Analyze the following squawk (pilot discrepancy report):

    Squawk: {squawk_text}

    Return a JSON object with:
    - ATA code (guess best match)
    - Probable cause
    - Recommended maintenance tasks (ATA, task number, if applicable)
    - Suggested write-up
    - RTS write-off format with today's date and placeholder technician ID
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You assist mechanics in processing pilot squawks and generating correct paperwork."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800
    )

    return response['choices'][0]['message']['content']
