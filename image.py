import os
import openai
import requests

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Step 4: Initialize API key
from config import API_KEY, IMAGE_PATH
openai.api_key = API_KEY

# Step 5: Make API Call
def generate_image(prompt, n=1, size="1024x1024"):
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size=size
    )
    
    # Step 6: Handle Response
    if response['data']:
        for i, img_data in enumerate(response['data']):
            img_url = img_data['url']
            download_image(img_url, f"{IMAGE_PATH}/{prompt.replace(' ', '_')}_{i+1}.jpg")

# Download image from URL
def download_image(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

# Example usage
if __name__ == "__main__":
    prompt = "river dam in mountain valley"  # Replace this with your desired prompt
    generate_image(prompt, n=2)  # This will generate a image based on the prompt
