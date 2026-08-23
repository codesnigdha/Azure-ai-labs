"""
Detect the language of text using Azure AI Language / Text Analytics.

Requirements:
    Python 3.9 or later

Install dependencies:
    python -m pip install azure-ai-textanalytics azure-core

Configuration:
    Before running, update the following variables:
    - YOUR_API_KEY: Your Azure Language API key.
    - YOUR_PROJECT_ENDPOINT: Your Azure Language endpoint.
    - YOUR_DOCUMENT_TEXT: The text you want to analyze.

Authentication:
    This example uses an Azure Language API key.

Usage:
    1. Update the configuration values.
    2. Run the script:
       python language_detection.py
"""

# Import the required Azure Text Analytics libraries
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# Store the Azure Language service API key
# Keep your actual API key private.
language_key = "<YOUR_API_KEY>"

# Store the Azure Language service endpoint
language_endpoint = "<YOUR_PROJECT_ENDPOINT>"


# Create and authenticate the Text Analytics client
def authenticate_client():

    # Create credentials using the API key
    ta_credential = AzureKeyCredential(language_key)

    # Create the Text Analytics client using the endpoint and credentials
    text_analytics_client = TextAnalyticsClient(
        endpoint=language_endpoint,
        credential=ta_credential
    )

    return text_analytics_client


# Create the authenticated client
client = authenticate_client()


# Example method for detecting the language of text
def language_detection_example(client):

    try:
        # Provide the text that needs to be analyzed
        documents = ["<YOUR_DOCUMENT_TEXT>"]

        # Detect the language of the provided text
        response = client.detect_language(
            documents=documents,
            country_hint="us"
        )[0]

        # Display the detected language
        print("Language:", response.primary_language.name)

    except Exception as err:
        # Display an error message if something goes wrong
        print("Encountered exception. {}".format(err))


# Run the language detection example
language_detection_example(client)
