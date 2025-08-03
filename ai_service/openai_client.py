import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_caption_and_description(prompt: str) -> tuple[str, str]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a marketing expert."},
            {"role": "user", "content": f"Generate a catchy ad caption and a short 2-line description for this prompt: {prompt}"}
        ],
        temperature=0.7
    )

    message = response.choices[0].message.content.strip()

    parts = message.split("\n", 1)
    caption = parts[0].strip()
    description = parts[1].strip() if len(parts) > 1 else ""

    return caption, description

def generate_image(prompt: str) -> str:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

