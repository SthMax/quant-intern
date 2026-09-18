Features / Open WebUI
Skip to main content
Open WebUIBlog
GitHubDiscord
Home
Getting Started
Reference
Features
Chat & Conversations
Workspace
Notes
Calendar
Channels
Open Terminal
Plugins & Extensibility
Authentication & Access
Administration
Ecosystem
Open Terminal & Terminals
Knowledge Base Sync (oikb)
Open WebUI Computer
Troubleshooting
Open WebUI for Enterprise
Tutorials
FAQ
Roadmap
Alternatives to Open WebUI
Security
Contributing
Sponsorships
Brand Guidelines
Open WebUI License
Our Mission
Our Team
Features
On this page
What You Can Do with Open WebUI
One interface for every AI model. Private, extensible, and built for teams.
Open WebUI replaces the patchwork of AI tools your team juggles daily - ChatGPT for writing, a separate app for image generation, another for document search, spreadsheets full of prompts nobody can find. Everything lives in one place: conversations, knowledge, tools, and the models that power them.
💬 Chat & Conversations​
Talk to any model, switch mid-conversation, and keep your context intact.
Your conversations are the core of Open WebUI. Chat with Ollama, OpenAI, Anthropic, or any OpenAI-compatible provider from a single interface. Attach files, search the web, execute code, and let the AI use tools - all without leaving the chat.
🔀 Multi-model chatsRun two models side-by-side and compare responses
📎 File & image uploadsAttach documents, images, and code for the AI to analyze
🔍 Web searchAI searches the web and cites sources in real time
🐍 Code executionRun Python directly in the browser or via Open Terminal
📝 Message queueKeep typing while the AI responds - messages send automatically
🧠 MemoryThe AI remembers facts about you across conversations
🗂️ Folders, tags, pinsOrganize conversations however you work
🎤 Voice & audioSpeech-to-text, text-to-speech, hands-free voice & video calls
🖼️ Image generationCreate and edit images with GPT-Image, Gemini, ComfyUI, and more
⏱️ AutomationsSchedule prompts to run automatically on recurring schedules
✅ Task managementModels maintain structured task lists for multi-step workflows
Explore chat features → · Audio → · Image Generation →
📚 Knowledge & RAG​
Give your AI access to your documents - and let it find what matters.
Upload files, build knowledge bases, and let the AI retrieve exactly the information it needs. Choose between vector search (RAG) for large collections or full-content injection for precision. With native function calling, models autonomously search, browse, and synthesize across your entire knowledge base.
📄 13 vector databasesChromaDB and PGVector (officially maintained), plus non-core integrations: Qdrant, Milvus, Elasticsearch, and more
🔍 Hybrid searchBM25 + vector search with cross-encoder reranking
📑 8 extraction enginesTika, Docling, Azure, Mistral OCR, Datalab Marker, MinerU, PaddleOCR, custom loaders
🤖 Agentic retrievalModels search and read your documents autonomously
📄 Full context modeInject entire documents - no chunking, no guessing
Learn about Knowledge →
🤖 Models & Agents​
Wrap any model with custom instructions, tools, and knowledge to build specialized agents.
Create a "Python Tutor" that always uses your style guide. A "Meeting Summarizer" with your company's template. A "Code Reviewer" with your linting rules baked in. Every agent is a configuration wrapper - pick any base model, bind knowledge, tools, and a system prompt.
🧩 Model presetsSystem prompts, tools, knowledge, and parameters in one package
🏷️ Dynamic variables{{ USER_NAME }}, {{ CURRENT_DATE }} injected automatically
🔧 Bound toolsForce-enable specific tools per model
👥 Access controlRestrict models to specific users or groups
📊 Global defaultsSet baseline capabilities and parameters for all models
Learn about Models →
📝 Notes​
Write, think, and refine with AI by your side.
A dedicated workspace for content that lives outside of any single conversation. Draft with a rich editor, use AI to rewrite text in place, and attach notes to any chat for precise context injection - no chunking, no vector search.
✍️ Rich editorMarkdown and Rich Text with a floating formatting toolbar
🤖 AI EnhanceRewrite or improve selected text in place
📎 Context injectionAttach notes to any chat for full-fidelity context
🔍 Agentic accessModels can search, read, and update notes autonomously
Learn about Notes →
💬 Channels​
Where your team and AI think together, in real time.
Persistent, shared spaces where humans and AI models participate in the same conversation. Tag @gpt-5.6 to draft a plan, then tag @claude to critique it - your whole team sees both responses in one timeline.
🤖 @model taggingSummon any AI model into the conversation on demand
🧵 Threads & reactionsReplies, pins, and emoji reactions
🔒 Access controlPublic, private, group-based, and direct message channels
🧠 AI channel awarenessModels search and synthesize across channels autonomously
Learn about Channels →
⚡ Open Terminal​
Give your AI a real computer to work on.
Connect a real computing environment to Open WebUI. The AI writes code, executes it, reads the output, fixes errors, and iterates - all from the chat. Handles files, installs packages, runs servers, and returns results.
🖥️ Code executionRuns real commands and returns output
📁 File browserBrowse, upload, download, and edit files in the sidebar
🌐 Website previewLive preview of web projects inside Open WebUI
🔒 Isolation optionalDocker container or bare metal
Learn about Open Terminal →
tip
Want the whole machine in a browser tab? See Open WebUI Computer, a separate Open WebUI project.
🔌 Extensibility​
Add any capability with Python tools, pipelines, MCP, or OpenAPI servers.
Open WebUI is a platform, not a locked-down product. Write Python tools that run inside the chat. Connect external services via OpenAPI or MCP. Build pipelines that filter, transform, or route every message. Import community-built extensions with one click.
🐍 Tools & FunctionsPython scripts that run in the chat - built-in code editor included
🔧 PipelinesModular plugin framework for filters, providers, and custom logic
🔗 MCP supportNative Streamable HTTP for Model Context Protocol servers
🌐 OpenAPI serversAuto-discover tools from any OpenAPI-compatible endpoint
📝 SkillsMarkdown instruction sets that teach models how to approach tasks
⚡ PromptsSlash-command templates with typed input variables and versioning
Learn about Extensibility →
🔐 Authentication & Access​
Control who gets in, what they can do, and how it connects to your identity stack.
Open WebUI is multi-user from day one. Define roles, create user groups, set per-model access, and integrate with your identity provider. From a solo install to an organization with thousands of seats.
👥 RBACRoles, groups, and per-resource permissions
🔐 SSO/OIDC/LDAPFederated authentication with any identity provider
📋 SCIM 2.0Automated user and group provisioning
🔑 API KeysProgrammatic access for scripts, bots, and integrations
Learn about Authentication & Access →
🔧 Administration​
Monitor usage, evaluate models, and communicate with your users.
📊 AnalyticsUsage dashboards with message volume, token consumption, and cost tracking
🏆 EvaluationModel arena, A/B testing, and ELO-based leaderboards
📢 BannersCustomizable system-wide announcements
🎚️ Default Interface SettingsInstance-wide starting values for everyone's interface options
🔔 WebhooksNotifications for sign-ups, chat completion, and external integrations
Learn about Administration →
🏗️ Deploy Anywhere​
Stateless architecture for horizontal scaling, on Docker, Kubernetes, pip, or bare metal. With data in shared databases and storage, and Redis coordinating instances, add application replicas behind a load balancer as demand grows.
🐳 Docker & ComposeOne-command deploy with GPU support
☸️ Kubernetes & HelmProduction-ready orchestration
📦 pip installpip install open-webui && open-webui serve
☁️ Cloud storageS3, GCS, Azure Blob for stateless instances
📊 OpenTelemetryTraces, metrics, and logs to your observability stack
⚖️ Horizontal scalingStateless application replicas with shared databases, storage, and Redis
Quick Start → · Scaling Guide → · Advanced Topics →
This content is for informational purposes only and does not constitute a warranty, guarantee, or contractual commitment. Open WebUI is provided "as is." See your license for applicable terms.
Edit this page
Previous
API Endpoints
Next
Chat & Conversations
💬 Chat & Conversations
📚 Knowledge & RAG
🤖 Models & Agents
📝 Notes
💬 Channels
⚡ Open Terminal
🔌 Extensibility
🔐 Authentication & Access
🔧 Administration
🏗️ Deploy Anywhere
Docs
Getting Started
FAQ
Help Improve The Docs
Community
GitHub
Discord
Reddit
𝕏
More
Release Notes
About
Sovereign AI
Report a Vulnerability / Responsible Disclosure
