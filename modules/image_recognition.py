import openai
import base64

# Set your OpenAI API key here or securely using environment variables
openai.api_key = "your-openai-api-key"

def identify_aircraft_part(image_file):
    image_bytes = image_file.read()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are an expert aircraft technician assistant."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What aircraft part is this? Provide the ATA chapter and suggested CRJ-700/900 manual tasks (AMM, IPC, CMM) for inspection or removal."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=800
    )
    return response['choices'][0]['message']['content']
