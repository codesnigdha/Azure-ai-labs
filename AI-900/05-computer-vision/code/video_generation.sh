# Send a request to create a video
curl -X POST "YOUR_FOUNDRY_ENDPOINT/videos" \

# Specify the request content type
-H "Content-Type: application/json" \

# Authenticate using the Azure API key
-H "Authorization: Bearer $AZURE_API_KEY" \

# Provide the video generation settings
-d '{
    # Describe the video you want to generate
    "prompt": "<video description>",

    # Specify the video generation model
    "model": "sora-2",

    # Specify the video dimensions
    "size": "<dimension>",

    # Specify the video duration in seconds
    "seconds": "<duration>"
}'