"""
Send a request to an AI agent using Microsoft Foundry
and the Azure AI Projects SDK.

Requirements:
    Python 3.9 or later

Install dependencies:
    pip install "azure-ai-projects>=2.1.0"

Configuration:
    Before running, update the following variables:
    - YOUR_PROJECT_ENDPOINT: Your Microsoft Foundry project endpoint.
    - YOUR_AGENT_NAME: The name of your deployed agent.
    - YOUR_AGENT_VERSION: The version of your agent.

Authentication:
    This example uses Azure DefaultAzureCredential.
    Make sure you are authenticated with Azure before running the script.

Usage:
    1. Sign in to Azure:
       az login

    2. Run the script:
       python agent_client.py
"""

# Import Azure authentication and AI Projects client
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


# Azure AI Foundry project endpoint
# Replace this with your own project endpoint
endpoint = "<YOUR_PROJECT_ENDPOINT>"


# Create the AI Project client using Azure credentials
project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)


# Name of the agent
agent_name = "<YOUR_AGENT_NAME>"

# Version of the agent
agent_version = "<YOUR_AGENT_VERSION>"


# Get the OpenAI-compatible client from the project
openai_client = project_client.get_openai_client()


# Send a request to the selected agent
response = openai_client.responses.create(
    input=[
        {
            "role": "user",
            "content": "Tell me what you can help with."
        }
    ],

    # Reference the agent by name and version
    extra_body={
        "agent_reference": {
            "name": agent_name,
            "version": agent_version,
            "type": "agent_reference"
        }
    },
)


# Display the agent's response
print(f"Response output: {response.output_text}")
