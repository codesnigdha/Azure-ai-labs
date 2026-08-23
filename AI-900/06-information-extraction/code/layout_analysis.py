"""
Analyze a document layout using Azure Content Understanding.

Requirements:
    Python 3.9 or later

Install dependencies:
    python -m pip install --pre azure-ai-contentunderstanding azure-identity

Configuration:
    Before running, update the following variables:
    - YOUR_CONTENT_UNDERSTANDING_ENDPOINT:
        Your Azure Content Understanding endpoint.
    - YOUR_CONTENT_UNDERSTANDING_KEY:
        Your API key, if using key-based authentication.
    - YOUR_FILE_URL:
        URL of the document to analyze.

Authentication:
    This example supports API key authentication or
    DefaultAzureCredential when no API key is provided.

Usage:
    1. Update the configuration values.
    2. Authenticate with Azure if using DefaultAzureCredential:
       az login
    3. Run the script:
       python layout_analysis.py
"""

import json
from urllib.parse import urlparse

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential


# Check whether a value is a valid absolute URL
def is_absolute_url(value: str) -> bool:
    parsed_url = urlparse(value)
    return bool(parsed_url.scheme and parsed_url.netloc)


def main() -> None:

    # Microsoft Foundry Content Understanding endpoint
    # Keep your actual endpoint private.
    endpoint = "YOUR_CONTENT_UNDERSTANDING_ENDPOINT"

    # API key (optional when using DefaultAzureCredential)
    # Keep your actual API key private.
    key = "YOUR_CONTENT_UNDERSTANDING_KEY"

    # URL of the document to analyze
    file_url = "YOUR_FILE_URL"

    # Analyzer used for general document layout analysis
    analyzer_id = "prebuilt-layout"

    # Content Understanding API version
    api_version = "2026-06-01-preview"

    # Validate the endpoint
    if not is_absolute_url(endpoint):
        print("[Error] Invalid endpoint.")
        return

    # Validate the file URL
    if not is_absolute_url(file_url):
        print("[Error] Invalid file URL.")
        return

    # Use API key authentication if provided.
    # Otherwise, use Azure's DefaultAzureCredential.
    credential = (
        AzureKeyCredential(key)
        if key and key != "YOUR_CONTENT_UNDERSTANDING_KEY"
        else DefaultAzureCredential()
    )

    # Create the Content Understanding client
    client = ContentUnderstandingClient(
        endpoint=endpoint,
        credential=credential,
        api_version=api_version,
    )

    # Display the analyzer and file being processed
    print(f"Analyzing with {analyzer_id} analyzer...")
    print("File URL:", file_url)

    try:
        # Start the document layout analysis
        poller = client.begin_analyze(
            analyzer_id=analyzer_id,
            inputs=[AnalysisInput(url=file_url)],
        )

        # Wait for the analysis to complete
        result: AnalysisResult = poller.result()

    except AzureError as err:
        # Handle Azure-specific errors
        print(f"[Azure Error]: {err}")
        return

    except Exception as ex:
        # Handle unexpected errors
        print(f"[Unexpected Error]: {ex}")
        return

    # Convert the analysis result into formatted JSON
    result_str = json.dumps(result.as_dict(), indent=2)

    print("\n" + "=" * 50)
    print("Analysis Result")
    print("=" * 50)

    # Display the analysis result
    print(result_str)


# Run the program
if __name__ == "__main__":
    main()
