# Instructions

## 1. Open Microsoft Foundry

- Open **Microsoft Foundry** and sign in with your Azure account.
- Enable **New Foundry** if required.
- Open the required Foundry project.
- Wait until the project is ready.

## 2. Deploy a Vision-Capable Model

- Go to **Discover → Models**.
- Search for **gpt-5-mini**.
- Select **Deploy** and use the default settings.
- Wait for the deployment to complete.
- Open the model in the Playground.

## 3. Analyze Images

- Set the model instructions to:

```text
You are an AI assistant that helps people identify vintage computer hardware.
```

- Select **Upload image**.
- Upload one of the provided images.
- Enter a prompt such as:

```text
What can you tell me about this?
```

- Review the AI-generated description.
- Upload the other images and test additional prompts such as:
  - `What is this?`
  - `Tell me about this.`

## 4. View Image Analysis Code

- Open the **Call model** tab.
- Select **Python** as the language.
- Select **Key authentication**.
- Review the sample code for sending both text and image content to the model.
- Keep any API keys, endpoints, and other private information hidden.

## 5. Generate an Image

- Return to the **Models** page.
- Select **Deploy a base model**.
- Select **Direct from Azure** under Collections.
- Select **Text to image** under Inference tasks.
- Choose an available image-generation model.
- Deploy the model.
- Open the image Playground.
- Enter a prompt such as:

```text
A vintage PC with a CRT monitor.
```

- Review the generated image.

## 6. View Image Generation Code

- If the deployed image-generation model provides code samples, select **View code**.
- Choose **Python** and the **OpenAI SDK**.
- Select **Key authentication**.
- Review the sample code for generating an image.
- Hide any API keys, endpoints, or other private information before saving or sharing the code.

## 7. Generate a Video _(If Available)_

- Return to the **Models** page.
- Select **Deploy a base model**.
- Select **Direct from Azure**.
- Select **Video generation** under Inference tasks.
- If **Sora-2** or another available video-generation model is accessible, deploy it.
- Open the video Playground.
- Enter a prompt such as:

```text
A retro computer game.
```

- Review the generated video.

## 8. View Video Code _(If Available)_

- Open **View Code** in the video Playground.
- Review the sample REST API code.
- Keep API keys, endpoints, and other private information hidden.

## 9. Complete the Lab

- Review the different computer vision and generative AI capabilities explored.
- Confirm that you tested image analysis.
- Confirm that you generated an image if an image-generation model was available.
- Review the sample code for the capabilities you explored.
- If video generation was unavailable, continue without it.

## 🧹 Cleanup

- Open the **Azure portal**.
- Go to the resource group containing the lab resources.
- Delete resources that are no longer needed to avoid unnecessary Azure costs.
