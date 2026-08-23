"""
Detect and redact Personally Identifiable Information (PII)
using Azure AI Language / Text Analytics.

Requirements:
    Python 3.9 or later

Install dependencies:
    python -m pip install azure-ai-textanalytics azure-core

Configuration:
    Before running, update the following variables:
    - YOUR_AZURE_LANGUAGE_API_KEY: Your Azure Language API key.
    - YOUR_AZURE_LANGUAGE_ENDPOINT: Your Azure Language endpoint.
    - YOUR_DOCUMENT_TEXT: The text you want to analyze.

Authentication:
    This example uses an Azure Language API key.

Usage:
    1. Update the configuration values.
    2. Run the script:
       python pii_recognition.py
"""

# Import the Azure Text Analytics client
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# Azure Language service credentials
# Keep your actual API key private.
key = "<YOUR_AZURE_LANGUAGE_API_KEY>"
endpoint = "<YOUR_AZURE_LANGUAGE_ENDPOINT>"


# Authenticate the Azure Language client
def authenticate_client():
    # Create Azure credentials using the API key
    ta_credential = AzureKeyCredential(key)

    # Create the Text Analytics client
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=ta_credential
    )

    return text_analytics_client


# Create the authenticated client
client = authenticate_client()


# Detect sensitive information (PII) from text
def pii_recognition_example(client):

    # Provide the text to analyze
    documents = [
        "<YOUR_DOCUMENT_TEXT>"
    ]

    # Recognize PII entities from the document
    response = client.recognize_pii_entities(
        documents,
        language="en"
    )

    # Keep only successful responses
    result = [doc for doc in response if not doc.is_error]

    # Process each document
    for doc in result:

        # Display the text with PII information redacted
        print("Redacted Text: {}".format(doc.redacted_text))

        # Display details about each detected PII entity
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("Category: {}".format(entity.category))
            print("Confidence Score: {}".format(entity.confidence_score))
            print("Offset: {}".format(entity.offset))
            print("Length: {}".format(entity.length))


# Run the PII recognition example
pii_recognition_example(client)
