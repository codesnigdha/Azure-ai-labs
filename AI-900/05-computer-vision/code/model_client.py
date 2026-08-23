"""
Send a prompt to a deployed model using Microsoft Foundry and the OpenAI SDK.

Requirements:
    Python 3.9 or later

Install dependencies:
    python -m pip install openai azure-identity

Configuration:
    Before running, update the following variable:
    - YOUR_AZURE_AI_FOUNDRY_ENDPOINT: Your Microsoft Foundry project endpoint.

Authentication:
    This example uses Azure DefaultAzureCredential.
    Make sure you are authenticated with Azure before running the script.

Usage:
    1. Sign in to Azure:
       az login

    2. Run the script:
       python model_client.py
"""

# Import the OpenAI client
from openai import OpenAI

# Import Azure authentication tools
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# Azure AI Foundry endpoint
endpoint = "<YOUR_AZURE_AI_FOUNDRY_ENDPOINT>"

# Name of the deployed model
deployment_name = "gpt-5-mini"


# Create a token provider for Azure authentication
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)


# Create the OpenAI client using Azure authentication
client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)


# Send a prompt to the deployed model
response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?"
)


# Display the model's response
print(f"Answer: {response.output_text}")
