import os
import requests
from config import API_KEY
import uuid

def generate_and_save_images(prompt, save_directory='downloaded_images', image_count=1, image_size='1024x1024'):
    """
    Generates images based on a prompt and saves them to the specified directory.
    
    :param prompt: The prompt to generate images for.
    :param save_directory: The directory to save downloaded images.
    :param image_count: The number of images to generate.
    :param image_size: The size of the generated images.
    """
    endpoint_url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Check if the images directory exists, if not, create it
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Check prompt length
    if len(prompt) > 4000:
        raise ValueError("The prompt is too long. Please limit it to 4000 characters.")
    
    # Body of the request
    body = {
        'model': 'dall-e-3',
        'prompt': prompt,
        'n': image_count,
        'size': image_size
    }

    try:
        # Make the POST request
        response = requests.post(endpoint_url, headers=headers, json=body)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response to JSON
            response_data = response.json()

            # Extract image URLs
            images = response_data.get('data', [])
            for i, image in enumerate(images, start=1):
                image_url = image.get('url')
                if image_url:
                    # Download the image data
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        # Generate a unique filename for the image
                        unique_filename = str(uuid.uuid4())
                        image_path = os.path.join(save_directory, f'{unique_filename}.png')

                        # Save the image to the specified path
                        with open(image_path, 'wb') as image_file:
                            image_file.write(image_response.content)
                            print(f'Image saved to {image_path}')
                    else:
                        print(f"Error downloading image {i}: {image_response.status_code}")
                else:
                    print(f"No URL found for image {i}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
user_prompt = input("Enter the prompt for the image generation: ")
generate_and_save_images(user_prompt)