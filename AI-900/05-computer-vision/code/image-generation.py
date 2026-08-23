"""
Generate an image using Microsoft Foundry and the OpenAI SDK.

Requirements:
    Python 3.9 or later

Install dependencies:
    python -m pip install openai azure-identity

Configuration:
    Before running, update the following variable:
    - YOUR_FOUNDRY_ENDPOINT: Your Microsoft Foundry project endpoint.

Authentication:
    This example uses Azure DefaultAzureCredential.
    Make sure you are authenticated with Azure before running the script.

Usage:
    1. Sign in to Azure using the Azure CLI:
       az login

    2. Run the script:
       python image-generation.py

Output:
    The generated image is saved as:
       output.png
"""

import base64

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# Microsoft Foundry project endpoint
endpoint = "YOUR_FOUNDRY_ENDPOINT"

# Name of the deployed image generation model
deployment_name = "gpt-image-1-mini"


# Create an Azure authentication token provider
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)


# Create the OpenAI client using Azure authentication
client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)


# Generate an image using the deployed model
img = client.images.generate(
    model=deployment_name,
    prompt="A cute baby polar bear",
    n=1,
    size="1024x1024",
)


# Decode the generated image from Base64 format
image_bytes = base64.b64decode(img.data[0].b64_json)


# Save the generated image to a file
with open("output.png", "wb") as f:
    f.write(image_bytes)


print("Image generated successfully and saved as output.png")
