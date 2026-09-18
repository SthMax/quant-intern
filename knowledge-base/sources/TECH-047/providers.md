Configure LLM Provider | goose | Your open source AI agent
Skip to main content
✨ goose has moved to the Agentic AI Foundation (AAIF): Learn more! ✨
QuickstartDocsTutorialsBlogResourcesExtensions
Recipe Cookbook
Deeplink Generator
DiscordGitHub
Quickstart
Getting Started
Install goose
Configure LLM Provider
Using Extensions
GDK
Guides
Tutorials
MCP Servers
Architecture Overview
Experimental
Troubleshooting
Getting Started
Configure LLM Provider
On this page
Copy page
Supported LLM Providers
goose is compatible with a wide range of LLM providers, allowing you to choose and integrate your preferred model.
Model Selection
goose relies heavily on tool calling capabilities and currently works best with Claude 4 models.
Berkeley Function-Calling Leaderboard can be a good guide for selecting models.
Available Providers​
ProviderDescriptionParameters
AI/ML APIOne API key for 300+ chat, image, video, audio, and embedding models from many providers, OpenAI-compatible.AIMLAPI_API_KEY
Amazon BedrockOffers a variety of foundation models, including Claude, Jurassic-2, and others. AWS environment variables must be set in advance, not configured through goose configureCredential auth: AWS_PROFILE, or AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGIONBearer token auth: AWS_BEARER_TOKEN_BEDROCK and AWS_REGION, AWS_DEFAULT_REGION, or AWS_PROFILE
Amazon SageMaker TGIRun Text Generation Inference models through Amazon SageMaker endpoints. AWS credentials must be configured in advance.SAGEMAKER_ENDPOINT_NAME, AWS_REGION (optional), AWS_PROFILE (optional)
AnthropicOffers Claude, an advanced AI model for natural language tasks.ANTHROPIC_API_KEY, ANTHROPIC_HOST (optional)
Atomic ChatRun local models with Atomic Chat's OpenAI-compatible server. Because this provider runs locally, you must first download a model.None required. Connects to local server at localhost:1337 by default.
AvianCost-effective inference API with DeepSeek, Kimi, GLM, and MiniMax models. OpenAI-compatible with streaming and function calling support.AVIAN_API_KEY, AVIAN_HOST (optional)
Azure AI FoundryAccess OpenAI, Anthropic, Microsoft, Meta, Mistral, DeepSeek, GLM, Kimi, and other models deployed through Azure AI Foundry project or MaaS endpoints.AZURE_FOUNDRY_ENDPOINT, AZURE_FOUNDRY_API_KEY (optional), AZURE_FOUNDRY_AD_TOKEN (optional), AZURE_FOUNDRY_API_VERSION (optional)
Azure OpenAIAccess Azure-hosted OpenAI models, including GPT-4 and GPT-3.5. Supports API key, Entra ID bearer token, and Azure credential chain authentication.AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_NAME, AZURE_OPENAI_API_KEY (optional), AZURE_OPENAI_AD_TOKEN (optional)
ChatGPT CodexAccess GPT-5 Codex models optimized for code generation and understanding. Requires a ChatGPT Plus/Pro subscription.No manual key. Uses browser-based OAuth authentication for both CLI and Desktop.
DatabricksUnified data analytics and AI platform for building and deploying models.DATABRICKS_HOST, DATABRICKS_TOKEN
Docker Model RunnerLocal models running in Docker Desktop or Docker CE with OpenAI-compatible API endpoints. Because this provider runs locally, you must first download a model.OPENAI_HOST, OPENAI_BASE_PATH
EmpirioLabs AIFrontier open and proprietary chat models (Qwen, DeepSeek, GLM, Kimi, MiniMax) through one OpenAI-compatible API with streaming. Catalog available at https://api.empiriolabs.ai/v1/models.EMPIRIOLABS_API_KEY
Friendli AIFriendli Model APIs provide instant access to a curated set of models, powered by a proprietary inference stack called Friendli Engine for high-performance, cost-efficient inference.FRIENDLI_API_KEY
FuturMixUnified AI gateway providing access to models from Anthropic, Google, OpenAI, and DeepSeek through an OpenAI-compatible API.FUTURMIX_API_KEY
GeminiAdvanced LLMs by Google with multimodal capabilities (text, images). Gemini 3 models support configurable thinking levels.GOOGLE_API_KEY, GEMINI3_THINKING_LEVEL (optional)
GCP Vertex AIGoogle Cloud's Vertex AI platform, supporting Gemini and Claude models. Credentials must be configured in advance. Filters for allowed models by organization policy (if configured).GCP_PROJECT_ID, GCP_LOCATION and optionally GCP_MAX_RATE_LIMIT_RETRIES (5), GCP_MAX_OVERLOADED_RETRIES (5), GCP_INITIAL_RETRY_INTERVAL_MS (5000), GCP_BACKOFF_MULTIPLIER (2.0), GCP_MAX_RETRY_INTERVAL_MS (320_000).
GitHub CopilotAccess to AI models from OpenAI, Anthropic, Google, and other providers through GitHub's Copilot infrastructure. GitHub account with Copilot access required.No manual key. Uses device flow authentication for both CLI and Desktop.
GondolaPay-per-request inference via Venice AI, settled in USDC on Base. No subscription or minimum. Includes privacy-preserving TEE models (e2ee-*). OpenAI-compatible.GONDOLA_API_KEY, GONDOLA_HOST (optional)
GroqHigh-performance inference hardware and tools for LLMs.GROQ_API_KEY
iFlytek SparkiFlytek Spark (讯飞星火) models (4.0Ultra, generalv3.5, max-32k) via the OpenAI-compatible HTTP API. Best for chat: Spark needs tool_calls_switch=true (not injectable here) to return OpenAI-style tool calls.SPARK_API_PASSWORD
iFlytek Astron MaaSiFlytek Astron MaaS (讯飞星辰) hosting Spark X2, DeepSeek, GLM, Kimi, MiniMax, Qwen, and Astron coding models via an OpenAI-compatible API. Set ASTRON_BASE_URL to switch between the Token Plan and Coding Plan endpoints.ASTRON_API_KEY, ASTRON_BASE_URL (optional)
LiteLLMLiteLLM proxy supporting multiple models with automatic prompt caching and unified API access.LITELLM_HOST, LITELLM_BASE_PATH (optional), LITELLM_API_KEY (optional), LITELLM_CUSTOM_HEADERS (optional), LITELLM_TIMEOUT (optional)
LM StudioRun local models with LM Studio's OpenAI-compatible server. Because this provider runs locally, you must first download a model.None required. Connects to local server at localhost:1234 by default.
MetaMeta's Model API, home of the Muse Spark models.META_MODEL_API_KEY
Mistral AIProvides access to Mistral models including general-purpose models, specialized coding models (Codestral), and multimodal models (Pixtral).MISTRAL_API_KEY
NEAR AI CloudTEE-backed private inference through an OpenAI-compatible API with dynamic model discovery.NEARAI_API_KEY
Novita AI90+ open-source models with OpenAI-compatible API and competitive pricing. Supports Kimi K2.5, DeepSeek, GLM, MiniMax, Qwen, and more.NOVITA_API_KEY
OllamaLocal model runner supporting Qwen, Llama, DeepSeek, and other open-source models. Because this provider runs locally, you must first download and run a model.OLLAMA_HOST
Ollama CloudAccess hosted models on ollama.com via OpenAI-compatible API. Requires an Ollama account and API key.OLLAMA_CLOUD_API_KEY
OpenAIProvides gpt-4o, o1, and other advanced language models. Also supports OpenAI-compatible endpoints (e.g., self-hosted LLaMA, vLLM, KServe). o1-mini and o1-preview are not supported because goose uses tool calling.OPENAI_API_KEY, OPENAI_HOST (optional), OPENAI_ORGANIZATION (optional), OPENAI_PROJECT (optional), OPENAI_CUSTOM_HEADERS (optional)
OpenRouterAPI gateway for unified access to various models with features like rate-limiting management.OPENROUTER_API_KEY, OPENROUTER_HOST (optional), OPENROUTER_PARAMETERS (optional)
PerplexityChat models with built-in real-time web search grounding. OpenAI-compatible chat completions API at https://api.perplexity.ai.PERPLEXITY_API_KEY
OVHcloud AIProvides access to open-source models including Qwen, Llama, Mistral, and DeepSeek through AI Endpoints service.OVHCLOUD_API_KEY
RamalamaLocal model using native OCI container runtimes, CNCF tools, and supporting models as OCI artifacts. Ramalama API is a compatible alternative to Ollama and can be used with the goose Ollama provider. Supports Qwen, Llama, DeepSeek, and other open-source models. Because this provider runs locally, you must first download and run a model.OLLAMA_HOST
RoutstrOpenAI-compatible aggregator that fronts dozens of upstream providers (Anthropic, OpenAI, Google, DeepSeek, Llama, …) behind a single API. Authenticate with an sk-... bearer issued by your Routstr instance — payment is handled outside goose.ROUTSTR_API_KEY, ROUTSTR_HOST (optional, default https://api.routstr.com)
SayGMTEE-backed private inference via an OpenAI-compatible API with dynamic model routing. Prices are determined at runtime per request.SAYGM_API_KEY
SaladCloud AI GatewayOpenAI-compatible access to SaladCloud-hosted open-source models, including Qwen, Gemma, and others.SALAD_CLOUD_API_KEY
ScalewayEuropean cloud offering OpenAI-compatible access to models like Mistral, Qwen, and open-source weights. Ensures data residency and GDPR compliance.SCW_SECRET_KEY
SnowflakeAccess the latest models using Snowflake Cortex services, including Claude models. Requires a Snowflake account and programmatic access token (PAT).SNOWFLAKE_HOST, SNOWFLAKE_TOKEN
VMware Tanzu PlatformEnterprise-managed LLM access through AI Services on VMware Tanzu Platform. Models are fetched dynamically from the endpoint.TANZU_AI_API_KEY, TANZU_AI_ENDPOINT
Tetrate Agent Router ServiceUnified API gateway for AI models including Claude, Gemini, GPT, open-weight models, and others. Supports PKCE authentication flow for secure API key generation.TETRATE_API_KEY, TETRATE_HOST (optional)
TrustedRouterModels from OpenAI, Anthropic, Google, DeepSeek and others via TrustedRouter's OpenAI-compatible API, with per-request routing and failover.TRUSTEDROUTER_API_KEY
Venice AIProvides access to open source models like Llama, Mistral, and Qwen while prioritizing user privacy. Requires an account and an API key.VENICE_API_KEY, VENICE_HOST (optional), VENICE_BASE_PATH (optional), VENICE_MODELS_PATH (optional)
CerebrasFast inference on Cerebras wafer-scale engines with models like Llama, Qwen, and others.CEREBRAS_API_KEY
xAIAccess to xAI's Grok models including grok-3, grok-3-mini, and grok-3-fast with 131,072 token context window.XAI_API_KEY, XAI_HOST (optional)
Prompt Caching for Claude Models
goose automatically enables Anthropic's prompt caching when using Claude models via Anthropic, Amazon Bedrock, Databricks, OpenRouter, and LiteLLM providers. This adds cache_control markers to requests, which can reduce costs for longer conversations by caching frequently-used context. See the provider implementations for technical details.
CLI Providers​
ProviderDescriptionRequirements
Cursor Agent (cursor-agent)Uses Cursor's AI CLI tool with your Cursor subscription. Provides access to GPT-5, Claude 4, and other models through the cursor-agent command-line interface.cursor-agent CLI installed and authenticated
ACP Providers​
goose supports Agent Client Protocol (ACP) agents as providers. ACP providers pass goose extensions through to the agent as MCP servers.
ProviderDescriptionRequirements
Claude ACP (claude-acp)Uses Claude Code via ACP. Passes goose extensions to the agent as MCP servers.npm install -g @agentclientprotocol/claude-agent-acp, active Claude Code subscription
Codex ACP (codex-acp)Uses OpenAI Codex via ACP. Passes goose extensions to the agent as MCP servers.npm install -g @agentclientprotocol/codex-acp, active ChatGPT Plus/Pro subscription or OpenAI API credits
ACP Providers
See the ACP Providers guide for detailed setup instructions.
Configure Provider and Model​
To configure your chosen provider, see available options, or select a model, visit the Models tab in goose Desktop or run goose configure in the CLI.
goose Desktop
goose CLI
First-time users:
On the welcome screen the first time you open goose, you have these options:
Quick Setup with API Key - goose will automatically configure your provider based on your API key
ChatGPT Subscription - Sign in with your ChatGPT Plus/Pro credentials to access GPT-5 Codex models
Agent Router by Tetrate - Access multiple AI models with automatic setup
OpenRouter - Access 200+ models with one API using pay-per-use pricing
Other Providers - Manually configure additional providers through settings
Quick Setup
ChatGPT Subscription
Agent Router
OpenRouter
Other Providers
Choose Quick Setup with API Key.
Enter your API key from your provider (for example, OpenAI, Anthropic, or Google).
goose will automatically detect your provider and configure the connection.
When setup is complete, you're ready to begin your first session.
Choose ChatGPT Subscription.
goose will open a browser window for you to sign in with the credentials of your active ChatGPT Plus or Pro subscription.
Authorize goose to access your ChatGPT subscription.
When you return to goose Desktop, you're ready to begin your first session.
We recommend new users start with Agent Router by Tetrate. Tetrate provides access to multiple AI models with built-in rate limiting and automatic failover.
Free Credits Offer
You'll receive $10 in free credits the first time you automatically authenticate with Tetrate through goose. This offer is available to both new and existing Tetrate users.
Choose Agent Router by Tetrate.
goose will open a browser window for you to authenticate with Tetrate, or create a new account if you don't have one already.
When you return to goose Desktop, you're ready to begin your first session.
Choose Automatic setup with OpenRouter.
goose will open a browser window for you to authenticate with OpenRouter, or create a new account if you don't have one already.
When you return to the goose Desktop, you're ready to begin your first session.
If you have a specific provider you want to use with goose, and an API key from that provider, choose Other Providers.
Find the provider of your choice and click its Configure button. If you don't see your provider in the list, click Add Custom Provider at the bottom of the window to configure a custom provider.
Depending on your provider, you'll need to input your API Key, API Host, or other optional parameters. Click the Submit button to authenticate and begin your first session.
Ollama Model Detection
For Ollama users, all locally installed models display automatically in the model selection dropdown.
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Configure providers
Click your provider in the list
Add your API key and other required configurations, then click Submit
To change your current model:
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Switch models
Choose from your configured providers in the dropdown, or select Use other provider to configure a new one
Select a model from the available options, or choose Use custom model to enter a specific model name
Click Select model to confirm your choice
Shortcut
For faster access, click your current model name at the bottom of the app and choose Change Model.
To start over with provider and model configuration:
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Reset Provider and Model to clear your current settings and return to the welcome screen
In your terminal, run the following command:
goose configure
Select Configure Providers from the menu and press Enter.
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Custom Providers│  ○ Add Extension│  ○ Toggle Extensions│  ○ Remove Extension│  ○ goose Settings└
Choose a model provider and press Enter. Use the arrow keys (↑/↓) to move through the options, or start typing to filter the list.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Amazon Bedrock│  ○ Amazon SageMaker TGI│  ● Anthropic (Claude and other models from Anthropic)│  ○ Azure OpenAI│  ○ Claude Code CLI│  ○ ...└
Enter your API key (and any other configuration details) when prompted.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Anthropic│◆  Provider Anthropic requires ANTHROPIC_API_KEY, please enter a value│  ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪└
If you're just changing models, skip any prompts to update the provider configuration.
Enter your desired ANTHROPIC_HOST or press Enter to use the default.
◆  Provider Anthropic requires ANTHROPIC_HOST, please enter a value│  https://api.anthropic.com (default)
Choose the model you want to use. Depending on the provider, you can:
Select the model from a list
Search for the model by name
Enter the model name directly
│◇  Model fetch complete│◇  Select a model:│  claude-sonnet-4-5 (default)│◒  Checking your configuration...└  Configuration saved successfully
This change takes effect the next time you start a session.
note
goose configure doesn't support entering custom model names. To use a model not in the provider's list, use goose Desktop or edit the GOOSE_MODEL variable in your config.yaml directly.
tip
Set the model for an individual session using the run command:
goose run --model claude-sonnet-4-0 -t "initial prompt"
Using Custom OpenAI Endpoints​
The built-in OpenAI provider can connect to OpenAI's official API (api.openai.com) or any OpenAI-compatible endpoint, such as:
Self-hosted LLMs (e.g., LLaMA, Mistral) using vLLM or KServe
Private OpenAI-compatible API servers
Enterprise deployments requiring data governance and security compliance
OpenAI API proxies or gateways
Custom Provider Option
Need to connect to multiple OpenAI-compatible endpoints? Configure custom providers instead for easier switching and better organization, as well as custom naming and shareable configurations.
Pointing at a LiteLLM proxy
You can reach a LiteLLM proxy in either of two ways—pick one, don't mix them:
Use the OpenAI provider: set OPENAI_HOST to your proxy's root (no trailing path) and OPENAI_BASE_PATH to the path it serves (usually v1/chat/completions). A 404 usually means OPENAI_BASE_PATH is wrong for your proxy. A 401 with No api key passed in is a different problem—the API key is not being loaded (for example, a key placed in config.yaml, which is ignored); see Provider API keys and config.yaml.
Use the dedicated LiteLLM provider, which is configured with its own LITELLM_HOST, LITELLM_BASE_PATH, and LITELLM_API_KEY variables instead of the OPENAI_* ones.
Configuration Parameters​
ParameterRequiredDescription
OPENAI_API_KEYYesAuthentication key for the API
OPENAI_HOSTNoCustom endpoint URL (defaults to api.openai.com)
OPENAI_BASE_PATHNoRequest path appended to the host (defaults to v1/chat/completions). Set this when your endpoint serves the chat completions API at a different path—most proxies expect v1/chat/completions, but some are mounted at chat/completions (no v1).
OPENAI_ORGANIZATIONNoOrganization ID for usage tracking and governance
OPENAI_PROJECTNoProject identifier for resource management
OPENAI_CUSTOM_HEADERSNoAdditional headers to include in the request. Can be set via environment variable, configuration file, or CLI, in the format HEADER_A=VALUE_A,HEADER_B=VALUE_B.
OPENAI_STORENoWhether to persist the generated Responses API response for later retrieval via API. Defaults to false.
Example Configurations​
vLLM Self-Hosted
KServe Deployment
Enterprise OpenAI
Custom Headers
If you're running LLaMA or other models using vLLM with OpenAI compatibility:
OPENAI_HOST=https://your-vllm-endpoint.internalOPENAI_API_KEY=your-internal-api-key
For models deployed on Kubernetes using KServe:
OPENAI_HOST=https://kserve-gateway.your-clusterOPENAI_API_KEY=your-kserve-api-keyOPENAI_ORGANIZATION=your-org-idOPENAI_PROJECT=ml-serving
For enterprise OpenAI deployments with governance:
OPENAI_API_KEY=your-api-keyOPENAI_ORGANIZATION=org-id123OPENAI_PROJECT=compliance-approved
For OpenAI-compatible endpoints that require custom headers:
OPENAI_API_KEY=your-api-keyOPENAI_ORGANIZATION=org-id123OPENAI_PROJECT=compliance-approvedOPENAI_CUSTOM_HEADERS="X-Header-A=abc,X-Header-B=def"
Setup Instructions​
goose Desktop
goose CLI
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Configure providers
Click OpenAI in the provider list
Fill in your configuration details:
API Key (required)
Host URL (for custom endpoints)
Organization ID (for usage tracking)
Project (for resource management)
Click Submit
Run goose configure
Select Configure Providers
Choose OpenAI as the provider
Enter your configuration when prompted:
API key
Host URL (if using custom endpoint)
Organization ID (if using organization tracking)
Project identifier (if using project management)
Enterprise Deployment
For enterprise deployments, you can pre-configure these values using environment variables or configuration files to ensure consistent governance across your organization.
Configure Custom Provider​
Create custom providers to connect to services that aren't already supported or customize how you connect to them. Custom providers appear in goose's provider list and can be selected like any other provider.
Benefits:
Multiple endpoints: Switch between different services (e.g., vLLM, corporate proxy, OpenAI)
Pre-configured models: Store a list of preferred models
Shareable configuration: JSON files can be shared across teams or checked into repos
Custom naming: Show "Corporate API" instead of "OpenAI" in the UI
Separate credentials: Assign each provider its own API key
Custom providers must use OpenAI, Anthropic, or Ollama compatible API formats. They can include custom headers for additional authentication, API keys, tokens, or tenant identifiers. Each custom provider maps to a JSON configuration file.
To add a custom provider:
goose Desktop
goose CLI
Config File
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Configure providers
Click Add Custom Provider at the bottom of the window
Fill in the provider details:
Provider Type:
OpenAI Compatible (most common)
Anthropic Compatible
Ollama Compatible
Display Name: A friendly name for the provider
API URL: The base URL of the API endpoint
Authentication:
API Key: The API key, which is accessed using a custom environment variable and stored in the keychain (or secrets.yaml if the keyring is disabled or cannot be accessed)
For providers that don't require authorization (e.g., local models like Ollama, vLLM, or internal APIs), uncheck the "This provider requires an API key" checkbox
Available Models: Comma-separated list of available model names
Streaming Support: Whether the API supports streaming responses (click to toggle)
Click Create Provider
Custom Headers
Currently, custom headers can't be defined in goose Desktop. As a workaround, edit the provider configuration file after creation.
In your terminal, run the following command:
goose configure
Select Custom Providers. Use the arrow keys (↑/↓) to move through the options.
┌   goose-configure│◆  What would you like to configure?│  ○ Configure Providers│  ● Custom Providers (Add custom provider with compatible API)│  ○ Add Extension│  ○ Toggle Extensions│  ○ Remove Extension│  ○ goose Settings└
Select Add A Custom Provider
┌   goose-configure│◇  What would you like to configure?│  Custom Providers│◆  What would you like to do?│  ● Add A Custom Provider (Add a new OpenAI/Anthropic/Ollama compatible Provider)│  ○ Remove Custom Provider└
Follow the prompts to enter the provider details:
API Type:
OpenAI Compatible (most common)
Anthropic Compatible
Ollama Compatible
Name: A friendly name for the provider
API URL: The base URL of the API endpoint
Authentication Required: Answer "Yes" if your provider needs an API key, or "No" if authentication is not required
If Yes: Choose how goose should obtain the credential:
Static API key: You'll be prompted to enter your API Key (stored securely in the keychain, or in secrets.yaml if the keyring is disabled or cannot be accessed)
Command (refreshable): You'll be prompted for a command (and optional arguments) that goose runs to fetch the credential, plus a refresh interval in seconds. Use this for short-lived credentials issued by an IdP or key vault, so goose can refresh them automatically instead of requiring a restart when they expire. See Command-Based Authentication below.
If No: The API key prompt is skipped
Available Models: Comma-separated list of available model names
Streaming Support: Whether the API supports streaming responses
Custom Headers: Any additional header names and values
Custom Headers
Currently, custom headers can only be defined for OpenAI compatible providers in the CLI. For Anthropic or Ollama compatible providers, edit the provider configuration file after creation.
First create a JSON file in the custom_providers directory:
macOS/Linux: ~/.config/goose/custom_providers/
Windows: %APPDATA%\Block\goose\config\custom_providers\
Example custom_corp_api.json configuration file:
{  "name": "custom_corp_api",  "engine": "openai",  "display_name": "Corporate API",  "description": "Custom Corporate API provider",  "api_key_env": "CUSTOM_CORP_API_API_KEY",  "base_url": "https://api.company.com/v1/chat/completions",  "models": [    {      "name": "gpt-4o",      "context_limit": 128000    },    {      "name": "gpt-3.5-turbo",      "context_limit": 16385    }  ],  "headers": {    "x-origin-client-id": "YOUR_CLIENT_ID",    "x-origin-secret": "YOUR_SECRET_VALUE"  },  "supports_streaming": true,  "requires_auth": true}
Then use the api_key_env to set the key for your session. For example:
export CUSTOM_CORP_API_API_KEY="your-api-key"goose session start --provider custom_corp_api
Keychain Key Storage
If you want to store the API key in the goose keychain, update the provider in goose Desktop and enter the key. This provides secure, persistent storage and allows goose to connect natively to the provider.
Command-Based Authentication​
Instead of a static api_key_env, a custom provider can be configured to run a command to obtain its credential. This is useful for short-lived credentials issued by an IdP or key vault: goose re-runs the command to refresh the credential instead of requiring a restart when it expires.
Add an auth object to the provider's JSON configuration in place of api_key_env (the two are mutually exclusive):
{  "name": "custom_corp_api",  "engine": "openai",  "display_name": "Corporate API",  "base_url": "https://api.company.com/v1/chat/completions",  "models": [{ "name": "gpt-4o", "context_limit": 128000 }],  "requires_auth": true,  "auth": {    "command": "/path/to/get-token.sh",    "args": [],    "refresh_interval": 3600,    "timeout_seconds": 10  }}
command: The executable to run. It is spawned directly, without a shell — none of command/args are shell-interpolated. If your script needs shell features (pipes, variable expansion), invoke an interpreter explicitly, e.g. "command": "/bin/bash", "args": ["-c", "..."]. A bare name (no path separator, e.g. "get-token") is looked up on PATH; a relative path (e.g. "./scripts/get-token.sh") is resolved against cwd.
args (optional): Arguments passed to command.
refresh_interval (optional, defaults to 3600): How long, in seconds, a fetched credential is cached before the command is re-run. Set to 0 to disable proactive refresh entirely — the command then only reruns reactively, after the provider's API rejects a request with an auth error.
timeout_seconds (optional, defaults to 10): How long to wait for the command before treating it as failed.
cwd (optional): Working directory for the command, and the base a relative command path is resolved against. Defaults to goose's current directory.
The command's trimmed standard output is used as the credential. It must exit successfully and print a non-empty value; on failure, goose surfaces an error rather than silently reusing a stale credential. The command inherits goose's full environment, since the same user configures goose and writes the script.
goose CLI
Config File
In goose configure, choose Command (refreshable) when prompted for how to obtain credentials for a custom provider (see above).
Add the auth object shown above to the provider's JSON file instead of setting api_key_env.
To update a custom provider:
goose Desktop
goose CLI
Config File
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Configure providers
Click on your custom provider in the list
Update the fields you want to change
Click Update Provider
In your terminal, run the following command:
goose configure
Select Configure Providers from the menu and press Enter.
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Custom Providers│  ○ Add Extension│  ○ Toggle Extensions│  ○ Remove Extension│  ○ goose Settings└
Select the custom provider you want to update and press Enter. Use the arrow keys (↑/↓) to move through the options, or start typing to filter the list.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Amazon Bedrock│  ○ Amazon SageMaker TGI│  ○ Anthropic│  ○ Azure OpenAI│  ○ Claude Code CLI│  ● Corporate API (Custom Corporate API provider)│  ○ Cursor Agent│  ○ ...└
Follow the prompts to update the fields.
Open the custom provider configuration file in the custom_providers directory:
macOS/Linux: ~/.config/goose/custom_providers/
Windows: %APPDATA%\Block\goose\config\custom_providers\
Update the fields you want to change and save your changes.
Your changes are available in your next goose session.
To remove a custom provider:
goose Desktop
goose CLI
Config File
Click the  button in the top-left to open the sidebar
Click the Settings button on the sidebar
Click the Models tab
Click Configure providers
Click on your custom provider in the list
Click Delete Provider
Confirm that you want to permanently remove the custom provider and its stored API key (if applicable) by clicking Confirm Delete
In your terminal, run the following command:
goose configure
Select Custom Providers. Use the arrow keys (↑/↓) to move through the options.
┌   goose-configure│◆  What would you like to configure?│  ○ Configure Providers│  ● Custom Providers (Add custom provider with compatible API)│  ○ Add Extension│  ○ Toggle Extensions│  ○ Remove Extension│  ○ goose Settings└
Select Remove Custom Provider.
┌   goose-configure│◇  What would you like to configure?│  Custom Providers│◆  What would you like to do?│  ○ Add A Custom Provider│  ● Remove Custom Provider (Remove an existing custom provider)└
Select the custom provider you want to remove.
The provider configuration file is removed from the custom_providers directory and the key is removed from the keychain.
tip
If the provider's API key is stored in the keychain, use goose CLI to remove the custom provider. This also removes the stored API key.
Delete the custom provider configuration file in the custom_providers directory:
macOS/Linux: ~/.config/goose/custom_providers/
Windows: %APPDATA%\Block\goose\config\custom_providers\
Using goose for Free​
goose is a free and open source AI agent that you can start using right away, but not all supported LLM Providers provide a free tier.
Below, we outline a couple of free options and how to get started with them.
Limitations
These free options are a great way to get started with goose and explore its capabilities. However, you may need to upgrade your LLM for better performance.
Groq​
Groq provides free access to open source (open weight) models with high-speed inference. To use Groq with goose, you need an API key from Groq Console.
Groq offers several open source models that support tool calling, including:
moonshotai/kimi-k2-instruct-0905 - Mixture-of-Experts model with 1 trillion parameters, optimized for agentic intelligence and tool use
qwen/qwen3-32b - 32.8 billion parameter model with advanced reasoning and multilingual capabilities
llama-3.3-70b-versatile - Meta's Llama 3.3 model for versatile applications
llama-3.1-8b-instant - Meta's Llama 3.1 model for fast inference
For the complete list of supported Groq models, see groq.json.
To set up Groq with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose Groq as provider from the list.
Click Configure, enter your API key, and click Submit.
Select the Groq model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose Groq as the provider.
Enter your API key when prompted.
Select the Groq model of your choice.
EmpirioLabs AI​
EmpirioLabs AI provides access to frontier open and proprietary chat models through a single OpenAI-compatible API with streaming. To use EmpirioLabs with goose, you need an API key from EmpirioLabs.
EmpirioLabs offers models that support tool calling, including:
qwen3-7-plus - Qwen3.7 Plus with a 1M context window
qwen3-7-max - Qwen3.7 Max with a 1M context window
deepseek-v4-pro - DeepSeek V4 Pro with a 1M context window
deepseek-v4-flash - DeepSeek V4 Flash with a 1M context window
glm-5-1 - GLM-5.1 with a 202K context window
kimi-k2-7-code - Kimi K2.7 Code with a 256K context window
minimax-m3 - MiniMax M3 with a 524K context window
The full live catalog is available at https://api.empiriolabs.ai/v1/models. For the complete list of EmpirioLabs models configured in goose, see empiriolabs.json. For more details, see the EmpirioLabs documentation.
To set up EmpirioLabs with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose EmpirioLabs AI as provider from the list.
Click Configure, enter your API key, and click Submit.
Select the EmpirioLabs model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose EmpirioLabs AI as the provider.
Enter your API key when prompted.
Select the EmpirioLabs model of your choice.
FuturMix​
FuturMix is a unified AI gateway providing access to models from Anthropic, Google, OpenAI, and DeepSeek through an OpenAI-compatible API. To use FuturMix with goose, you need an API key from FuturMix.
FuturMix offers models that support tool calling, including:
claude-sonnet-4-20250514 - Anthropic Claude Sonnet 4 with 200K context
gpt-4o - OpenAI GPT-4o with 128K context
gemini-2.5-pro - Google Gemini 2.5 Pro with 1M context
deepseek-chat - DeepSeek V3 with 131K context
claude-haiku-4-20250514 - Anthropic Claude Haiku 4 with 200K context
For the complete list of supported FuturMix models, see futurmix.json.
To set up FuturMix with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose FuturMix as provider from the list.
Click Configure, enter your API key, and click Submit.
Select the FuturMix model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose FuturMix as the provider.
Enter your API key when prompted.
Select the FuturMix model of your choice.
Novita AI​
Novita AI provides access to 90+ open-source models via an OpenAI-compatible API with competitive pricing. To use Novita AI with goose, you need an API key from Novita AI.
Novita AI offers many models that support tool calling, including:
moonshotai/kimi-k2.5 - Moonshot's latest model with 262K context window
minimax/minimax-m2.7 - MiniMax M2.7 with 205K context
zai-org/glm-5.1 - Zhipu's GLM-5.1 with 205K context
deepseek/deepseek-v3.2 - DeepSeek V3.2 with 164K context
google/gemma-4-31b-it - Google Gemma 4 31B with 262K context
For the complete list of supported Novita AI models, see novita.json.
To set up Novita AI with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose Novita AI as provider from the list.
Click Configure, enter your API key, and click Submit.
Select the Novita AI model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose Novita AI as the provider.
Enter your API key when prompted.
Select the Novita AI model of your choice.
Routstr​
Routstr is an OpenAI-compatible aggregator that fronts dozens of upstream providers behind a single API. Payment is handled by the Routstr instance itself, so all goose needs is the sk-... bearer that instance issues you. To use Routstr with goose, pick an instance (the default is https://api.routstr.com) and obtain an API key from its payment flow.
Routstr aggregates models from many upstream providers, including:
claude-opus-4.7 — Anthropic's Claude opus 4.7
deepseek-v4-pro — DeepSeek V4 Pro
gemini-3.1-pro-preview — gemini-3.1 Pro Preview
/v1/models is queried at configure time, so the full catalogue your Routstr instance exposes is available in the model picker. For the static defaults shipped with goose, see routstr.json.
To set up Routstr with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose Routstr as provider from the list.
Click Configure, enter your ROUTSTR_API_KEY (and optionally override ROUTSTR_HOST to point at a different Routstr instance), and click Submit.
Select the Routstr model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose Routstr as the provider.
Enter your API key when prompted (and optionally override ROUTSTR_HOST).
Select the Routstr model of your choice.
SayGM​
SayGM provides TEE-backed private inference via an OpenAI-compatible API. Model routing and prices are determined at runtime per request. To use SayGM with goose, you need an API key from SayGM.
SayGM supports many models, including:
Qwen/Qwen3-235B-A22B-Thinking-2507-TEE — Qwen3 235B thinking model (TEE-backed)
deepseek-ai/DeepSeek-V3.2-TEE — DeepSeek V3.2 (TEE-backed)
moonshotai/Kimi-K3-TEE — Kimi K3 (TEE-backed)
zai-org/GLM-5.2-TEE — GLM-5.2 (TEE-backed)
/v1/models is queried at configure time, so the full catalogue SayGM exposes is available in the model picker.
To set up SayGM with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose SayGM as provider from the list.
Click Configure, enter your API key, and click Submit.
Select the SayGM model of your choice.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose SayGM as the provider.
Enter your API key when prompted.
Select the SayGM model of your choice.
Google Gemini​
Google Gemini provides a free tier. To start using the Gemini API with goose, you need an API Key from Google AI studio.
To set up Google Gemini with goose, follow these steps:
goose Desktop
goose CLI
To update your LLM provider and API key:
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure Providers
Choose Google Gemini as provider from the list.
Click Configure, enter your API key, and click Submit.
Run:
goose configure
Select Configure Providers from the menu.
Follow the prompts to choose Google Gemini as the provider.
Enter your API key when prompted.
Enter the Gemini model of your choice.
┌   goose-configure│◇ What would you like to configure?│ Configure Providers│◇ Which model provider should we use?│ Google Gemini│◇ Provider Google Gemini requires GOOGLE_API_KEY, please enter a value│▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪│◇ Enter a model from that provider:│ gemini-2.0-flash-exp│◇ Hello! You're all set and ready to go, feel free to ask me anything!│└ Configuration saved successfully
Local LLMs​
goose is a local AI agent, and by using a local LLM, you keep your data private, maintain full control over your environment, and can work entirely offline without relying on cloud access. However, please note that local LLMs require a bit more set up before you can use one of them with goose.
Limited Support for models without tool calling
goose extensively uses tool calling, so models without it can only do chat completion. If using models without tool calling, all goose extensions must be disabled.
Here are some local providers we support:
Ollama
LM Studio
Atomic Chat
Docker Model Runner
Ramalala
DeepSeek-R1
Other Models
Download Ramalama.
In a terminal, run any Ollama model supporting tool-calling or GGUF format HuggingFace Model:
The --runtime-args="--jinja" flag is required for Ramalama to work with the goose Ollama provider.
Example:
ramalama serve --runtime-args="--jinja" ollama://qwen2.5
In a separate terminal window, configure with goose:
goose configure
Choose to Configure Providers
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Toggle Extensions│  ○ Add Extension└
Choose Ollama as the model provider since Ramalama is API compatible and can use the goose Ollama provider
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Anthropic│  ○ Databricks│  ○ Google Gemini│  ○ Groq│  ● Ollama (Local open source models)│  ○ OpenAI│  ○ OpenRouter└
Enter the host where your model is running
Endpoint
For the Ollama provider, if you don't provide a host, we set it to localhost:11434. When constructing the URL, we prepend http:// if the scheme is not http or https. Since Ramalama's default port to serve on is 8080, we set OLLAMA_HOST=http://0.0.0.0:8080
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◆  Provider Ollama requires OLLAMA_HOST, please enter a value│  http://0.0.0.0:8080└
Enter the model you have running
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◇  Provider Ollama requires OLLAMA_HOST, please enter a value│  http://0.0.0.0:8080│◇  Enter a model from that provider:│  qwen2.5│◇  Welcome! You're all set to explore and utilize my capabilities. Let's get started on solving your problems together!│└  Configuration saved successfully
Context Length
If you notice that goose is having trouble using extensions or is ignoring .goosehints, it is likely that the model's default context length of 2048 tokens is too low. Use ramalama serve to set the --ctx-size, -c option to a higher value.
The native DeepSeek-r1 model doesn't support tool calling, however, we have a custom model you can use with goose.
warning
Note that this is a 70B model size and requires a powerful device to run smoothly.
Download Ollama.
In a terminal window, run the following command to install the custom DeepSeek-r1 model:
ollama run michaelneale/deepseek-r1-goose
In a separate terminal window, configure with goose:
goose configure
Choose to Configure Providers
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Toggle Extensions│  ○ Add Extension└
Choose Ollama as the model provider
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Anthropic│  ○ Databricks│  ○ Google Gemini│  ○ Groq│  ● Ollama (Local open source models)│  ○ OpenAI│  ○ OpenRouter└
Enter the host where your model is running
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◆  Provider Ollama requires OLLAMA_HOST, please enter a value│  http://localhost:11434└
Enter the installed model from above
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◇   Provider Ollama requires OLLAMA_HOST, please enter a value│  http://localhost:11434│◇  Enter a model from that provider:│  michaelneale/deepseek-r1-goose│◇  Welcome! You're all set to explore and utilize my capabilities. Let's get started on solving your problems together!│└  Configuration saved successfully
Download Ollama.
In a terminal, run any model supporting tool-calling
Example:
ollama run qwen2.5
In a separate terminal window, configure with goose:
goose configure
Choose to Configure Providers
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Toggle Extensions│  ○ Add Extension└
Choose Ollama as the model provider
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Anthropic│  ○ Databricks│  ○ Google Gemini│  ○ Groq│  ● Ollama (Local open source models)│  ○ OpenAI│  ○ OpenRouter└
Enter the host where your model is running
Endpoint
For Ollama, if you don't provide a host, we set it to localhost:11434.
When constructing the URL, we prepend http:// if the scheme is not http or https.
If you're running Ollama on a different server, you'll have to set OLLAMA_HOST=http://{host}:{port}.
For hosted models on ollama.com, use the Ollama Cloud provider instead.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◆  Provider Ollama requires OLLAMA_HOST, please enter a value│  http://localhost:11434└
Enter the model you have running
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Ollama│◇  Provider Ollama requires OLLAMA_HOST, please enter a value│  http://localhost:11434│◇  Enter a model from that provider:│  qwen2.5│◇  Welcome! You're all set to explore and utilize my capabilities. Let's get started on solving your problems together!│└  Configuration saved successfully
Context Length
If you notice that goose is having trouble using extensions or is ignoring .goosehints, it is likely that the model's default context length of 4096 tokens is too low. Set the OLLAMA_CONTEXT_LENGTH environment variable to a higher value.
LM Studio lets you run open-source models locally with an OpenAI-compatible API server.
Download and install LM Studio.
Open LM Studio and download a model that supports tool calling (e.g., Qwen, Llama, or Mistral variants).
Start the local server in LM Studio. The server runs on http://localhost:1234 by default
Configure goose to use LM Studio:
goose Desktop
goose CLI
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure providers.
Choose LM Studio from the provider list and click Configure.
Click Submit (no API key is needed).
Select the model you have loaded in LM Studio.
Run:
goose configure
Select Configure Providers from the menu.
Choose LM Studio as the provider.
Enter the model name that matches the model loaded in LM Studio.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  LM Studio│◇  Enter a model from that provider:│  qwen2.5-7b-instruct│└  Configuration saved successfully
Model Name
Make sure the model name you enter in goose matches the model identifier shown in LM Studio's server panel.
Atomic Chat lets you run open-source models locally with an OpenAI-compatible API server.
Download and install Atomic Chat from atomic.chat or GitHub Releases.
Open Atomic Chat and download a model that supports tool calling (e.g., Qwen, Llama, or Mistral variants).
Start the local server in Atomic Chat. The server runs on http://localhost:1337 by default
Configure goose to use Atomic Chat:
goose Desktop
goose CLI
Click the  button in the top-left to open the sidebar.
Click the Settings button on the sidebar.
Click the Models tab.
Click Configure providers.
Choose Atomic Chat from the provider list and click Configure.
Click Submit (no API key is needed).
Select the model you have loaded in Atomic Chat.
Run:
goose configure
Select Configure Providers from the menu.
Choose Atomic Chat as the provider.
Enter the model name that matches the model loaded in Atomic Chat.
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  Atomic Chat│◇  Enter a model from that provider:│  qwen2.5-7b-instruct│└  Configuration saved successfully
Model Name
Make sure the model name you enter in goose matches the model identifier shown for your server in Atomic Chat. If the API listens on a different origin than http://localhost:1337, set ATOMIC_CHAT_HOST in goose to match (scheme, host, and port only).
Get Docker
Enable Docker Model Runner
Pull a model, for example, from Docker Hub AI namespace, Unsloth, or from HuggingFace
Example:
docker model pull hf.co/unsloth/gemma-3n-e4b-it-gguf:q6_k
Configure goose to use Docker Model Runner, using the OpenAI API compatible endpoint:
goose configure
Choose to Configure Providers
┌   goose-configure│◆  What would you like to configure?│  ● Configure Providers (Change provider or update credentials)│  ○ Toggle Extensions│  ○ Add Extension└
Choose OpenAI as the model provider:
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◆  Which model provider should we use?│  ○ Anthropic│  ○ Amazon Bedrock│  ○ Claude Code│  ● OpenAI (GPT-4 and other OpenAI models, including OpenAI compatible ones)│  ○ OpenRouter
Configure Docker Model Runner endpoint as the OPENAI_HOST:
┌   goose-configure│◇  What would you like to configure?│  Configure Providers│◇  Which model provider should we use?│  OpenAI│◆  Provider OpenAI requires OPENAI_HOST, please enter a value│  https://api.openai.com (default)└
The default value for the host-side port Docker Model Runner is 12434, so the OPENAI_HOST value could be:
http://localhost:12434.
Configure the base path:
◆  Provider OpenAI requires OPENAI_BASE_PATH, please enter a value│  v1/chat/completions (default)└
Docker model runner uses /engines/llama.cpp/v1/chat/completions for the base path.
Finally configure the model available in Docker Model Runner to be used by goose: hf.co/unsloth/gemma-3n-e4b-it-gguf:q6_k
│◇  Enter a model from that provider:│  gpt-4o│◒  Checking your configuration...└  Configuration saved successfully
OpenRouter Advanced Parameters​
OpenRouter accepts provider-specific request parameters such as verbosity, reasoning, plugins, require_parameters, and other supported fields. Set OPENROUTER_PARAMETERS in your config.yaml to add these fields to every OpenRouter chat completion request.
You can use a YAML object:
OPENROUTER_PARAMETERS:  verbosity: xhigh  reasoning:    effort: high  plugins:    - id: web
Or a JSON string:
OPENROUTER_PARAMETERS: '{"verbosity":"xhigh","plugins":[{"id":"web"}]}'
goose ignores reserved request fields it already manages, such as model, messages, stream, and stream_options. Other OpenRouter-specific top-level fields are passed through the shared OpenAI-compatible request parameter handling.
GitHub Copilot Authentication​
GitHub Copilot uses a device flow for authentication, so no API keys are required:
Run goose configure and select GitHub Copilot
An eight-character code will be automatically copied to your clipboard
A browser will open to GitHub's device activation page
Paste the code to authorize the application
When you return to goose, GitHub Copilot will be available as a provider in both CLI and Desktop.
Azure OpenAI Authentication​
goose supports three authentication methods for Azure OpenAI:
Entra ID Bearer Token - Uses a pre-acquired Microsoft Entra access token from AZURE_OPENAI_AD_TOKEN, sent as Authorization: Bearer <token>. goose skips Azure CLI and token acquisition entirely, which suits enterprise deployments where only short-lived tokens are exposed to the runtime (e.g. obtained via az account get-access-token --resource https://cognitiveservices.azure.com --query accessToken --output tsv)
API Key Authentication - Uses the AZURE_OPENAI_API_KEY for direct authentication
Azure Credential Chain - Uses Azure CLI credentials automatically without requiring an API key
When more than one is configured, AZURE_OPENAI_AD_TOKEN takes precedence over AZURE_OPENAI_API_KEY, which takes precedence over the credential chain.
To use the Azure Credential Chain:
Ensure you're logged in with az login
Have appropriate Azure role assignments for the Azure OpenAI service
Configure with goose configure and select Azure OpenAI, leaving the API key field empty
This method simplifies authentication and enhances security for enterprise environments.
Multi-Model Configuration​
Beyond single-model setups, goose supports multi-model configurations that can use different models and providers for specialized tasks:
Subagents - Delegate scoped tasks to isolated sessions to keep your primary workflow focused and efficient
Meta Muse Spark Reasoning Effort​
Meta's Muse Spark models support a configurable reasoning effort that maps to Meta's reasoning_effort request parameter:
Low - Faster responses, lighter reasoning
Medium - Balanced reasoning depth and latency
High - Deeper reasoning, higher latency
Max - Sent as xhigh, the deepest reasoning level Meta supports
goose Desktop
goose CLI
When selecting a Muse Spark model, a "Thinking Effort" dropdown appears automatically. Select your preference and the setting persists across sessions.
When you run goose configure and select a Muse Spark model, you'll be prompted to choose a thinking effort:
◆  Select thinking effort:│  ● Off - No extended thinking│  ○ Low - Better latency, lighter reasoning│  ○ Medium - Moderate thinking│  ○ High - Deep reasoning│  ○ Max - No constraints on thinking depth
You can also set this globally with the GOOSE_THINKING_EFFORT environment variable (off, low, medium, high, or max).
note
Muse Spark always reasons and has no way to disable it, so choosing off is clamped to low (the lightest level Meta supports) rather than omitting the reasoning_effort parameter.
Gemini 3 Thinking Levels​
Gemini 3 models support configurable thinking levels to balance response latency and reasoning depth:
Low (default) - Faster responses, lighter reasoning
High - Deeper reasoning, higher latency
tip
When thinking is enabled, you can view the model's reasoning process. See Viewing Model Reasoning for details.
goose Desktop
goose CLI
When selecting a Gemini 3 model, a "Thinking Level" dropdown appears automatically. Select your preference and the setting persists across sessions.
Interactive configuration:
When you run goose configure and select a Gemini 3 model, you'll be prompted to choose a thinking level:
◆  Select thinking level for Gemini 3:│  ● Low - Better latency, lighter reasoning│  ○ High - Deeper reasoning, higher latency
Priority Order
The thinking level is determined in this order (highest to lowest priority):
request_params.thinking_level in model configuration
GEMINI3_THINKING_LEVEL environment variable
Default value: low
Viewing Model Reasoning​
Some models expose their internal reasoning or "chain of thought" as part of their response. goose automatically captures this reasoning output and makes it available to you. The following models and providers support reasoning output:
Provider / ModelHow It Works
DeepSeek-R1 (via OpenAI, Ollama, OpenRouter, OVHcloud, etc.)Reasoning captured from the reasoning_content field in the API response
Kimi (via Groq or other OpenAI-compatible endpoints)Reasoning captured from the reasoning_content field in the API response
Gemini CLI (Google Gemini models with thinking enabled)Thinking blocks captured from the streaming response
Claude (Anthropic, with Claude thinking enabled)Thinking blocks captured from the API response
goose Desktop
goose CLI
Reasoning output appears automatically in a collapsible "Show reasoning" toggle above the model's response. Click it to expand and view the model's thought process.
Reasoning output is hidden by default in the CLI. To display it, set the GOOSE_CLI_SHOW_THINKING environment variable:
export GOOSE_CLI_SHOW_THINKING=1
When enabled, reasoning appears under a "Thinking:" header in dimmed text before the model's main response.
note
This requires stdout to be a terminal (reasoning output won't appear when piping output to a file or another command).
tip
Reasoning output can be useful for understanding how the model arrived at its answer, debugging unexpected behavior, or learning from the model's problem-solving approach. However, it can also be verbose — toggle it on only when you need it.
If you have any questions or need help with a specific provider, feel free to reach out to us on Discord or on the goose repo.
Previous
Install goose
Next
Using Extensions
Available ProvidersCLI Providers
ACP Providers
Configure Provider and ModelUsing Custom OpenAI Endpoints
Configure Custom ProviderCommand-Based Authentication
Using goose for FreeGroq
EmpirioLabs AI
FuturMix
Novita AI
Routstr
SayGM
Google Gemini
Local LLMs
OpenRouter Advanced Parameters
GitHub Copilot Authentication
Azure OpenAI Authentication
Multi-Model Configuration
Meta Muse Spark Reasoning Effort
Gemini 3 Thinking Levels
Viewing Model Reasoning
Quick Links
Install goose
Extensions
Community
Spotlight
Discord
YouTube
LinkedIn
Twitter / X
BlueSky
Nostr
More
Blog
GitHub
Copyright © 2026 AAIF (Agentic AI Foundation)
