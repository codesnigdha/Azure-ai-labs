"""
Analyze a document using Azure Content Understanding.

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
        URL of the document or file to analyze.

Authentication:
    This example supports API key authentication or
    DefaultAzureCredential when no API key is provided.

Usage:
    1. Update the configuration values.
    2. Authenticate with Azure if using DefaultAzureCredential:
       az login
    3. Run the script:
       python document_analysis.py
"""

import json
from urllib.parse import urlparse

from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential


# Check whether the provided value is a valid absolute URL.
def is_absolute_url(value: str) -> bool:
    parsed_url = urlparse(value)
    return bool(parsed_url.scheme and parsed_url.netloc)


def main() -> None:

    # Microsoft Foundry Content Understanding endpoint.
    # Keep your actual endpoint private.
    endpoint = "YOUR_CONTENT_UNDERSTANDING_ENDPOINT"

    # API key for Content Understanding.
    # Keep your actual API key private.
    key = "YOUR_CONTENT_UNDERSTANDING_KEY"

    # URL of the document or file to analyze.
    file_url = "YOUR_FILE_URL"

    # Analyzer used to extract text and document content.
    analyzer_id = "prebuilt-read"

    # Content Understanding API version.
    api_version = "2026-06-01-preview"

    # Validate the Content Understanding endpoint.
    if not is_absolute_url(endpoint):
        print("[Error] Invalid endpoint.")
        return

    # Validate the document/file URL.
    if not is_absolute_url(file_url):
        print("[Error] Invalid file URL.")
        return

    # Use API key authentication when a key is provided.
    # Otherwise, use Azure DefaultAzureCredential.
    credential = (
        AzureKeyCredential(key)
        if key and key != "YOUR_CONTENT_UNDERSTANDING_KEY"
        else DefaultAzureCredential()
    )

    # Create the Content Understanding client.
    client = ContentUnderstandingClient(
        endpoint=endpoint,
        credential=credential,
        api_version=api_version,
    )

    # Display the analyzer and file being processed.
    print(f"Analyzing with {analyzer_id} analyzer...")
    print(f"File URL: {file_url}\n")

    try:
        # Start the document analysis.
        poller = client.begin_analyze(
            analyzer_id=analyzer_id,
            inputs=[AnalysisInput(url=file_url)],
        )

        # Wait for the analysis to complete.
        result: AnalysisResult = poller.result()

    except AzureError as err:
        # Handle Azure-specific errors.
        print(f"[Azure Error]: {err}")
        return

    except Exception as ex:
        # Handle unexpected errors.
        print(f"[Unexpected Error]: {ex}")
        return

    # Convert the analysis result into formatted JSON.
    result_str = json.dumps(result.as_dict(), indent=2)

    print("=" * 50)
    print("Analysis Result:")
    print("=" * 50 + "\n")

    # Display only the first 50 lines if the result is very large.
    max_display_lines = 50
    result_lines = result_str.splitlines()

    if len(result_lines) > max_display_lines:
        print("\n".join(result_lines[:max_display_lines]))

        print(
            f"\n{len(result_lines) - max_display_lines} "
            "more lines not displayed..."
        )
    else:
        print(result_str)


# Run the program.
if __name__ == "__main__":
    main()
