AI Endpoints | LibreChat
Skip to main contentLibreChat is joining ClickHouse to power the open-source Agentic Data Stack 🎉 Learn more
LibreChat
LibreChat
Search⌘K
Versionv0.8.x (latest)
DocsBlogChangelogDocumentationDeploy
Quick Start
Local Installation
Remote Hosting
Configure
ConfigurationCore
Environment VariablesHTTP Security HeadersLibreChat YAMLExampleAI EndpointsAnyscaleAPIpieAzure OpenAICloudflare Workers AICohereDatabricksDeepseekFireworksGroqHeliconeHuggingfaceAMD LemonadeLiteLLMMistralApple MLXMoonshotNEAR AI CloudNeurochainAIOllamaOpenRouterPerplexityPortkey AIShuttleAItogether.aiTrueFoundry AI GatewayvLLMVultr Cloud InferencexAI
Object Structure
Services
Authentication
Pre-configured AI
Tools
Speech SettingsInfrastructure
MongoDB
RedisFile Storage & CDN
SharePoint IntegrationDocker OverrideMonitoring & Moderation
Automated ModerationLangfuse TracingLogging SystemMetricsMeilisearchUI
BannerToken UsageRAG API
Use
Features
Compatibility MatrixMCP Servers
User Guides
Tools
Toolkit
Contributing
TranslationDevelopment
English
AI Endpoints
ConfigurationLibreChat YAMLAI Endpoints
AI Endpoints
This section lists known, compatible AI Endpoints with example setups for the `librechat.yaml` AKA the LibreChat Custom Config file.
Copy MarkdownOpen
Intro
This section lists known, compatible AI Endpoints, also known as "Custom Endpoints," with example setups for the librechat.yaml file, also known as the Custom Config file.
In all of the examples, arbitrary environment variable names are defined but you can use any name you wish, as well as changing the value to user_provided to allow users to submit their own API key from the web UI.
Important: 'user_provided' Key Setting
When setting API keys to "user_provided", this allows users to enter their own API keys through the web interface. This is different from the pre-configured endpoints in the .env file where you would set ENDPOINT_KEY=user_provided (e.g., OPENAI_API_KEY=user_provided).
For custom endpoints in librechat.yaml, you would use:
endpoints:
custom:
- name: "Your Endpoint"
apiKey: "user_provided"  # No need for ${} syntax here
For environment variables in the .env file, you would use:
OPENAI_API_KEY=user_provided
Some of the endpoints are marked as Known, which means they might have special handling and/or an icon already provided in the app for you.
Notes
It's recommended you follow the Custom Endpoints Quick Start Guide before proceeding with the examples below.
Important: make sure you setup the librechat.yaml file correctly: setup documentation.
How is this guide?
GoodBad
Edit on GitHub
Example
Previous Page
Anyscale
Configure Anyscale as a custom endpoint in LibreChat.
On this page
IntroNotes
