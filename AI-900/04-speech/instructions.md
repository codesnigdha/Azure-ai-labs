# Instructions

## 1. Open Microsoft Foundry

- Open **Microsoft Foundry** and sign in with your Azure account.
- Enable **New Foundry** if required.
- Open the required Foundry project.
- Wait until the project is ready.

## 2. Create an AI Agent

- From the **Home** page, select **Start building** under **Build an agent**.
- Create a new agent named `speech-agent`.
- Make sure a model is selected for the agent.
- Add the following instructions:

```text
You are an AI agent that provides information about AI and related topics. You answer questions concisely and precisely.
```

- Save the agent.
- Test it with:

```text
What can you help me with?
```

## 3. Enable Voice Mode

- Enable **Voice mode** under the model selection area.
- Open the **Configuration** panel if it does not appear automatically.
- Review the **Speech input** settings.
- Review the **Speech output** voice settings.
- Save the changes.

## 4. Start a Speech Session

- In the Chat pane, select **Start session**.
- Allow microphone access if prompted.
- Wait for the agent to show **Listening…**.
- Ask:

```text
How does speech recognition work?
```

- Observe the **Processing…** and **Speaking…** stages.
- Use the **CC** option to view the conversation as text.

## 5. Continue the Conversation

- Ask another question, such as:

```text
How does speech synthesis work?
```

- Review the agent's spoken response.
- End the session using the **X** button.
- Review the generated transcript.

## 6. View Client Code

- Select **Call agent** at the top of the Chat pane.
- Review the sample client code.
- Check how the code:
  - Connects to the Foundry project.
  - Accesses the AI agent.
  - Handles audio input and output.
  - Uses microphone and speaker devices.

## 7. Complete the Lab

- Review the speech capabilities explored during the lab.
- Verify that the speech agent can receive spoken input and provide spoken responses.
- Clean up any temporary Azure resources that are no longer needed.

## 🧹 Cleanup

Delete Azure resources that are no longer needed to avoid unnecessary costs.
