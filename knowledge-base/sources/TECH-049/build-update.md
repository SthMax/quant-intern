Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more | Microsoft Agent Framework
Skip to main content
Dev Blogs
AI
All .NET posts
.NET MAUI
ASP.NET Core
Blazor
Entity Framework
C++
C#
F#
TypeScript
NuGet
Servicing
.NET Blog in Chinese
Microsoft for Developers
Agent Framework
Develop from the cloud
Xcode
ISE Developer
TypeScript
PowerShell
Python
Java
Java Blog in Chinese
Go
Microsoft Edge Dev
Microsoft 365 Developer
Microsoft Entra Identity Developer
Microsoft Entra PowerShell
Visual Studio
Visual Studio Code
Aspire
All things Azure
Azure SDK
Azure VM Runtime Team
Microsoft Azure
Azure Cosmos DB
Azure DocumentDB
Azure Data Studio
Azure SQL
DevOps
DirectX
Microsoft Foundry
Power Platform
OData
Unified Data Model (IDEAs)
Windows Command Line
#ifdef Windows
Inside MSIX
MIDI and music
React Native
The Old New Thing
Windows Developer
Dev Blogs
Microsoft Agent Framework
Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more
June 3rd, 2026
0 reactions
Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more
Shawn Henry
Principal Group Product Manager
Show more
Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more
BUILD 2026 is underway, and the Microsoft Agent Framework team have a round-up of exciting announcements! Microsoft Agent Framework (MAF) is our open-source SDK and runtime for building AI agents and multi-agent workflows, with the same concepts and APIs across .NET and Python. It gives you a clean programming model – chat clients, tools, MCP integrations, context providers, middleware, and multi-step workflows – so you can focus on agent logic instead of plumbing. MAF reached 1.0 GA on April 2, 2026, bringing the convergence of AutoGen and Semantic Kernel into a single, supported platform. Everything below builds on that 1.0 foundation.
What’s new
Agent Harness: production patterns, built in
The agent harness is the layer where model reasoning meets real execution: shell and filesystem access, human-in-the-loop approval flows, and context management across long-running sessions. With MAF, these patterns are now first-class and consistently built in from the get-go. Agent harness extensions turn any chat client into a fully-featured Agent Harness using a single method.
These building blocks ship in the harness:
Automatic context compaction: monitors token usage and compacts chat history mid-loop to prevent context window overflow during long tool-calling chains
Built-in default instructions and instruction merging: ships with opinionated system instructions for task breakdown, tool usage, and reasoning patterns
Instruction merging: harness instructions appear first, then your custom agent instructions
Built-in Providers and tools:
FileMemoryProvider: session-scoped file-based memory so the agent can persist notes/learnings across turns; stored in agent-file-memory/{session}/
FileAccessProvider: general file access so that the agent can access and change any files it needs to operate on
TodoProvider: lets the agent track work items (add, complete, remove, list) in session state for multi-step task management
AgentModeProvider: supports “plan” vs “execute” operating modes so the agent can separate planning from action
AgentSkillsProvider: skill discovery and execution from the file system, enabling modular capability injection
BackgroundAgentsProvider: delegate subtasks to child agents running in parallel for fan-out orchestration
Web search: hosted web search tool out of the box (disable with DisableWebSearch)
Shell execution (.NET only): run shell commands via a sandboxed ShellExecutor
Middleware and customization:
ToolApprovalAgent: “don’t ask again” approval rules for sensitive tool calls
OpenTelemetryAgent: automatic opent telemetry Semantic Conventions tracing
Pluggable storage backends: swap FileMemoryStore and FileAccessStore with any AgentFileStore implementation (file system, blob storage, etc.)
Example in .NET:
AIAgent agent =
chatClient.AsHarnessAgent(MaxContextWindowTokens, MaxOutputTokens, new HarnessAgentOptions
{
Name = "BlogWriterAgent",
Description = "A blog writing assistant that researches a topic, plans an outline, and drafts a blog post.",
FileMemoryStore = new FileSystemAgentFileStore(Path.Combine(AppContext.BaseDirectory, "artifacts")),
ChatOptions = new ChatOptions
{
Instructions = instructions,
Tools =
[
new WebBrowsingTool(),
],
},
});
// Run the interactive console session using the shared HarnessConsole helper.
await HarnessConsole.RunAgentAsync(
agent,
userPrompt: "Enter a blog topic to get started.",
new HarnessConsoleOptions
{
Observers = [
new OpenAIResponsesWebSearchDisplayObserver(),
new OpenAIResponsesErrorObserver()
]
CommandHandlers = HarnessConsoleOptions.BuildDefaultCommandHandlers(agent),
});
Example in python:
# Create a harness agent with research-specific instructions.
# All other features (todo, mode, compaction, skills, telemetry, web search) are
# automatically configured with sensible defaults.
agent = create_harness_agent(
client=client,
max_context_window_tokens=128_000,
max_output_tokens=16_384,
name="ResearchAgent",
description="A research assistant that plans and executes research tasks.",
agent_instructions=RESEARCH_INSTRUCTIONS,
)
Learn more: Agent Harness in Agent Framework · Harness samples on GitHub
Foundry Hosted Agents: from local to production
Once your MAF agent runs locally, the next question is how to deploy, monitor, evaluate, and version it. Hosted Agents in Foundry Agent Service is the easiest way to give that agent a production home with your own code, packaged as a container and deployed onto Foundry-managed infrastructure, with built-in identity, automatic scaling, managed session state, observability, and versioning.
What you get out of the box:
Scale to zero, pay nothing while the agent is idle; it scales back up on the next request.
Resume with filesystem intact, files, disk state, and session identity persist across scale-to-zero, so the agent restarts exactly where it left off.
Per-session isolation, every session gets its own VM-isolated sandbox with persistent state.
Built-in observability, MAF’s OpenTelemetry traces flow into Application Insights with zero extra wiring.
Turning a local agent into a hosted agent takes only a few lines. In .NET:
using Microsoft.Agents.AI.Foundry.Hosting;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);
var app = builder.Build();
app.MapFoundryResponses();
app.Run();
And in Python:
server = ResponsesHostServer(agent)
server.run()
Learn more: From Local to Production with Foundry Hosted Agents · .NET samples · Python samples
CodeAct: faster agents with fewer model turns
Many agents aren’t bottlenecked by model quality, they’re bottlenecked by orchestration overhead. When an agent chains together many small tool calls, each step is a separate model turn, driving up latency and token usage.
CodeAct collapses that loop. Instead of choosing a tool, waiting, and choosing the next one, the model writes a single short Python program that calls your tools via call_tool(…), runs it once in a sandbox, and returns a consolidated result. CodeAct ships in the new agent-framework-hyperlight (alpha) package, which runs the model-generated code in a fresh, locally isolated Hyperlight micro-VM per call, so strong isolation is essentially free at the granularity of a single tool call.
Wiring it in is a one-line change to how your tools are registered:
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider
@tool
def get_weather(city: str) -> dict[str, float | str]:
"""Return the current weather for a city."""
return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}
codeact = HyperlightCodeActProvider(
tools=[get_weather],
approval_mode="never_require",
)
agent = Agent(
client=client,
name="CodeActAgent",
instructions="You are a helpful assistant.",
context_providers=[codeact],
)
result = await agent.run(
"Get the weather for Seattle and Amsterdam and compare them."
)
On a representative multi-step workload (computing order totals across many users, dozens of tool calls), the difference is significant:
Wiring
Time
Tokens
Traditional
27.81s
6,890
CodeAct
13.23s
2,489
Improvement
52.4%
63.9%
Learn more: CodeAct in Agent Framework · Hyperlight package · Benchmark sample
Also reaching 1.0
The features in Microsoft Agent Framework are graduating from preview to release:
GitHub Copilot SDK integration
MAF now supports building agents on the GitHub Copilot SDK as a backend, bringing Copilot’s coding-oriented capabilities  (shell execution, file operations, URL fetching, and MCP server integration) into the standard MAF programming model.
Python:
import asyncio
from agent_framework.github import GitHubCopilotAgent
async def basic_example():
agent = GitHubCopilotAgent(
default_options={"instructions": "You are a helpful assistant."},
)
async with agent:
result = await agent.run("What is Microsoft Agent Framework?")
print(result)
.NET:
using GitHub.Copilot.SDK;
using Microsoft.Agents.AI;
await using CopilotClient copilotClient = new();
await copilotClient.StartAsync();
AIAgent agent = copilotClient.AsAIAgent();
Console.WriteLine(await agent.RunAsync("What is Microsoft Agent Framework?"));
The Copilot agent is a standard MAF agent, so it supports tools, instructions, streaming, sessions, MCP servers, and built-in OpenTelemetry observability.
Learn more: GitHub Copilot provider docs
Multi-agent orchestration: the Handoff pattern
Multi-agent systems often start as a router that forwards to a specialist, and sometimes break the first time an agent needs a follow-up question, more context from a peer, or realizes mid-turn that the request belongs elsewhere. Handoff orchestration is built for exactly that: you declare the agents and the directed edges between them, and the framework injects the handoff tools each agent uses to transfer control. Topology and guardrails stay with the developer; routing decisions stay with the agents.
.NET
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;
AIAgent triage = chatClient.AsAIAgent(
instructions: "You receive a user request and route it to the right specialist.",
name: "Triage");
AIAgent billing = chatClient.AsAIAgent(
instructions: "You handle billing questions.", name: "Billing");
AIAgent tech = chatClient.AsAIAgent(
instructions: "You handle technical support questions.", name: "Tech");
Workflow workflow = AgentWorkflowBuilder
.CreateHandoffBuilderWith(triage)
.WithHandoff(triage, billing)
.WithHandoff(triage, tech)
.Build();
The same graph in Python:
from agent_framework_orchestrations import HandoffBuilder
workflow = (
HandoffBuilder(participants=[triage, billing, tech])
.with_start_agent(triage)
.add_handoff(triage, [billing, tech])
.build()
)
Learn more: A Tour of the Handoff Orchestration Pattern
See us at BUILD
Come find the team at the Foundry booths and sessions at BUILD. Bring your agents and your questions!
Can’t make it in person? Watch online. Sessions featuring Microsoft Agent Framework:
BRK243: Claw and agent harness in Microsoft Foundry
BRK 241: From prototype to production: build and run agents at scale
DEM361: Understand and fix Agent Framework apps with observability and evals
DEM333: How Foundry integrates with open-source frameworks and tools
DEM312: Multi-agents in action with 3 AI agents, 3 frameworks, tools & models
BRK250: Observe and control agents across any framework with open source tools
If you’ve enjoyed building with Agent Framework, give us a star on GitHub and share feedback in our Discussions. We can’t wait to see what you build. Download the SDK on GitHub, read the documentation, visit the developer blog, or join the Discord.
0
0
2
Share on Facebook
Share on X
Share on Linkedin
Category
Agent Framework
Share
Author
Shawn Henry
Principal Group Product Manager
Principal Group Product Manager
0 comments
Discussion is closed.
Code of Conduct
Read next
June 9, 2026
ICYMI: Inside the Microsoft Agent Framework: How we designed a layered SDK
Shawn Henry
June 22, 2026
Build your own claw and agent harness with Microsoft Agent Framework
Wes Steyn
Stay informed
Get notified when new posts are published.
Email *
Country/Region *
Select...United StatesAfghanistanÅland IslandsAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBonaireBosnia and HerzegovinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBritish Virgin IslandsBruneiBulgariaBurkina FasoBurundiCabo VerdeCambodiaCameroonCanadaCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCongo (DRC)Cook IslandsCosta RicaCôte dIvoireCroatiaCuraçaoCyprusCzechiaDenmarkDjiboutiDominicaDominican RepublicEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEswatiniEthiopiaFalkland IslandsFaroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-BissauGuyanaHaitiHeard Island and McDonald IslandsHondurasHong Kong SARHungaryIcelandIndiaIndonesiaIraqIrelandIsle of ManIsraelItalyJamaicaJan MayenJapanJerseyJordanKazakhstanKenyaKiribatiKoreaKosovoKuwaitKyrgyzstanLaosLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgMacau SARMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMicronesiaMoldovaMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorth MacedoniaNorthern Mariana IslandsNorwayOmanPakistanPalauPalestinian AuthorityPanamaPapua New GuineaParaguayPeruPhilippinesPitcairn IslandsPolandPortugalPuerto RicoQatarRéunionRomaniaRwandaSabaSaint BarthélemySaint Kitts and NevisSaint LuciaSaint MartinSaint Pierre and MiquelonSaint Vincent and the GrenadinesSamoaSan MarinoSão Tomé and PríncipeSaudi ArabiaSenegalSerbiaSeychellesSierra LeoneSingaporeSint EustatiusSint MaartenSlovakiaSloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and South Sandwich IslandsSouth SudanSpainSri LankaSt HelenaAscensionTristan da CunhaSurinameSvalbardSwedenSwitzerlandTaiwanTajikistanTanzaniaThailandTimor-LesteTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluU.S. Outlying IslandsU.S. Virgin IslandsUgandaUkraineUnited Arab EmiratesUnited KingdomUruguayUzbekistanVanuatuVatican CityVenezuelaVietnamWallis and FutunaYemenZambiaZimbabwe
I would like to receive the Microsoft Agent Framework Newsletter. Privacy Statement.
Subscribe
Follow this blog
Are you sure you wish to delete this
comment?
OK
Cancel
Sign in
Theme
Insert/edit link
Close
Enter the destination URL
URL
Link Text
Open link in a new tab
Or link to existing content
Search
No search term specified. Showing recent items.
Search or use up and down arrow keys to select an item.
Cancel
Code Block
×
Paste your code snippet
Ok
Cancel
Surface Pro
Surface Laptop
Surface Laptop Ultra
Surface RTX Spark Dev Box
Copilot for organizations
Copilot for personal use
Explore Microsoft products
Windows 11 apps
Account profile
Download Center
Microsoft Store support
Returns
Order tracking
Certified Refurbished
Microsoft Store Promise
Flexible Payments
Microsoft in education
Devices for education
Microsoft Teams for Education
Microsoft 365 Education
How to buy for your school
Educator training and development
Deals for students and parents
AI for education
Microsoft AI
Microsoft Security
Dynamics 365
Microsoft 365
Microsoft Power Platform
Microsoft Teams
Microsoft 365 Copilot
Small Business
Azure
Microsoft Developer
Microsoft Learn
Support for AI marketplace apps
Microsoft Tech Community
Microsoft Marketplace
Software companies
Visual Studio
Careers
About Microsoft
Company news
Privacy at Microsoft
Investors
Diversity and inclusion
Accessibility
Sustainability
Your Privacy Choices
Consumer Health Privacy
Sitemap
Contact Microsoft
Privacy
Manage cookies
Terms of use
Trademarks
Safety & eco
Recycling
About our ads
