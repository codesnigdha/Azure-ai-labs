"""
Send a request to an AI agent using Microsoft Foundry
and the Azure AI Projects SDK.

Requirements:
    Python 3.9 or later

Install dependencies:
    pip install "azure-ai-projects>=2.1.0"

Configuration:
    Before running, update the following variable:
    - YOUR_PROJECT_ENDPOINT: Your Microsoft Foundry project endpoint.

Authentication:
    This example uses DefaultAzureCredential for Azure authentication.
    Make sure you are authenticated with Azure before running the script.

Usage:
    1. Sign in to Azure:
       az login

    2. Run the script:
       python agent_client.py
"""

# Import DefaultAzureCredential to authenticate with Azure
from azure.identity import DefaultAzureCredential

# Import AIProjectClient to connect to the Microsoft Foundry project
from azure.ai.projects import AIProjectClient


# Microsoft Foundry project endpoint
# Replace this with your own project endpoint
endpoint = "<YOUR_PROJECT_ENDPOINT>"


# Create a client to connect to the Microsoft Foundry project
# DefaultAzureCredential() handles Azure authentication
project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)


# Name of the agent created in Microsoft Foundry
agent_name = "computing-historian"

# Version of the agent being used
agent_version = "1"


# Get the OpenAI client from the Foundry project client
openai_client = project_client.get_openai_client()


# Send a request to the selected Foundry agent
# The agent processes the user's question and generates a response
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


# Display the agent's response in the terminal
print(f"Response output: {response.output_text}")
