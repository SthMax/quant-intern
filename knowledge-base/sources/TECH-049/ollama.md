Ollama | Microsoft Learn
Skip to main content
Skip to Ask Learn chat experience
This browser is no longer supported.
Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.
Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge
Table of contents
Exit editor mode
Ask Learn
Ask Learn
Reading mode
Table of contents
Read in English
Add
Add to Plans
Edit
Copy Markdown
Print
Note
Access to this page requires authorization. You can try signing in or changing directories.
Access to this page requires authorization. You can try changing directories.
Ollama
Feedback
Summarize this article for me
In this article
Ollama allows you to run open-source models locally and use them with Agent Framework. This is ideal for development, testing, and scenarios where you need to keep data on-premises.
Prerequisites
Install and start Ollama.
Download a model, such as ollama pull llama3.2.
Installation
dotnet add package OllamaSharp
dotnet add package Microsoft.Agents.AI --prerelease
Configuration
OLLAMA_ENDPOINT="http://localhost:11434"
OLLAMA_MODEL_NAME="llama3.2"
Create an Ollama agent
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OllamaSharp;
var endpoint = Environment.GetEnvironmentVariable("OLLAMA_ENDPOINT") ?? throw new InvalidOperationException("OLLAMA_ENDPOINT is not set.");
var modelName = Environment.GetEnvironmentVariable("OLLAMA_MODEL_NAME") ?? throw new InvalidOperationException("OLLAMA_MODEL_NAME is not set.");
// Get a chat client for Ollama and use it to construct an AIAgent.
AIAgent agent = new OllamaApiClient(new Uri(endpoint), modelName)
.AsAIAgent(instructions: "You are good at telling jokes.", name: "Joker");
// Invoke the agent and output the text result.
Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
Prerequisites
Ensure Ollama is installed and running locally with a model downloaded before running any examples:
ollama pull llama3.2
Note
Not all models support function calling. For tool usage, try llama3.2 or qwen3:4b.
Installation
Native Ollama
OpenAI Compatible
pip install agent-framework-ollama --pre
pip install agent-framework
Configuration
Native Ollama
OpenAI Compatible
OLLAMA_MODEL="llama3.2"
The native client connects to http://localhost:11434 by default. Override it with the OLLAMA_HOST environment variable or the host constructor argument.
OLLAMA_ENDPOINT="http://localhost:11434/v1/"
OLLAMA_MODEL="llama3.2"
Create Ollama Agents
Native Ollama
OpenAI Compatible
OllamaChatClient provides native Ollama integration with full support for function tools and streaming.
import asyncio
from agent_framework import Agent
from agent_framework.ollama import OllamaChatClient
async def main():
agent = Agent(
client=OllamaChatClient(),
name="HelpfulAssistant",
instructions="You are a helpful assistant running locally via Ollama.",
)
result = await agent.run("What is the largest city in France?")
print(result)
asyncio.run(main())
You can also use OpenAIChatClient with a custom base URL pointing to your Ollama instance.
import asyncio
import os
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
async def main():
agent = Agent(
client=OpenAIChatClient(
api_key="ollama",  # Placeholder, Ollama doesn't require an API key
base_url=os.environ["OLLAMA_ENDPOINT"],
model=os.environ["OLLAMA_MODEL"],
),
name="HelpfulAssistant",
instructions="You are a helpful assistant running locally via Ollama.",
)
result = await agent.run("What is the largest city in France?")
print(result)
asyncio.run(main())
Tools
The Python Ollama clients (OllamaChatClient and OpenAIChatClient pointed at an Ollama-compatible endpoint) support locally invoked tools. Hosted tool types do not exist because Ollama is a local model runtime.
Tool
Status
Notes
Function Tools
✅
Standard Python callables or @ai_function. Whether the selected model can actually call them depends on the model itself.
Tool Approval
✅
Provided by the framework's function-invoking chat client; works with any function-tool call.
Code Interpreter
❌
No hosted code interpreter.
File Search
❌
No hosted file search.
Web Search
❌
No hosted web search.
Hosted MCP Tools
❌
Ollama does not expose hosted MCP.
Local MCP Tools
✅
Runs in your process and works with any chat client.
Function Tools
Native Ollama
OpenAI Compatible
import asyncio
from datetime import datetime
from agent_framework import Agent
from agent_framework.ollama import OllamaChatClient
def get_time(location: str) -> str:
"""Get the current time."""
return f"The current time in {location} is {datetime.now().strftime('%I:%M %p')}."
async def main():
agent = Agent(
client=OllamaChatClient(),
name="TimeAgent",
instructions="You are a helpful time agent.",
tools=get_time,
)
result = await agent.run("What time is it in Seattle?")
print(result)
asyncio.run(main())
import asyncio
import os
from datetime import datetime
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
def get_time(location: str) -> str:
"""Get the current time."""
return f"The current time in {location} is {datetime.now().strftime('%I:%M %p')}."
async def main():
agent = Agent(
client=OpenAIChatClient(
api_key="ollama",
base_url=os.environ["OLLAMA_ENDPOINT"],
model=os.environ["OLLAMA_MODEL"],
),
name="TimeAgent",
instructions="You are a helpful time agent.",
tools=get_time,
)
result = await agent.run("What time is it in Seattle?")
print(result)
asyncio.run(main())
Streaming
from agent_framework import Agent
from agent_framework.ollama import OllamaChatClient
async def streaming_example():
agent = Agent(
client=OllamaChatClient(),
instructions="You are a helpful assistant.",
)
print("Agent: ", end="", flush=True)
async for chunk in agent.run("Tell me about Python.", stream=True):
if chunk.text:
print(chunk.text, end="", flush=True)
print()
Note
Go support for this feature is coming soon. See the Agent Framework Go repository for the latest status.
Next steps
GitHub Copilot
Feedback
Was this page helpful?
Yes
No
No
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn
Ask Learn
Suggest a fix?
Additional resources
Last updated on
2026-08-25
In this article
Was this page helpful?
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn
Ask Learn
Suggest a fix?
en-us
Your Privacy Choices
Theme
Light
Dark
High contrast
AI Disclaimer
Previous Versions
Blog
Contribute
Privacy
Consumer Health Privacy
Terms of Use
Trademarks
© Microsoft 2026
