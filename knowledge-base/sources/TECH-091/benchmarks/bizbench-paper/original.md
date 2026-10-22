BizBench: Unveiling Hidden Challenges  
in Deploying Long-Horizon Agents  
for Real-World Business

[Enhan Zhao](https://openreview.net/profile?id=~Enhan_Zhao1) <sup>1,2,*</sup>    [Yongqi Tong](https://openreview.net/profile?id=~Yongqi_Tong2) <sup>2,*</sup>    [Xuejun Yu](https://openreview.net/profile?id=~Yu_Xuejun1) <sup>2</sup>    [Hang Wang](https://openreview.net/profile?id=~Hang_Wang14) <sup>2</sup>    [Pan Wang](https://openreview.net/profile?id=~Pan_Wang13) <sup>2</sup>  
[Yichao Wang](https://openreview.net/profile?id=~yichao_wang7) <sup>2</sup>    [Di He](https://openreview.net/profile?id=~Di_He1) <sup>1</sup>    [Jianshe Li](https://openreview.net/profile?id=~JIANSHE_LI1) <sup>2</sup>    [Wei Wu](https://openreview.net/profile?id=~Wei_Wu1) <sup>2,<math data-latex="\dagger" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>†</mo> <annotation>\dagger</annotation></semantics></math></sup>

<sup>1</sup> Peking University  <sup>2</sup> Ant International

Emails: {zhaoenhan.zeh, tongyongqi.yq, xuejun.yu, wh549825, apen.wp}@ant-intl.com  
<sup><math data-latex="\dagger" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mo>†</mo> <annotation>\dagger</annotation></semantics></math></sup> Corresponding author: Wei Wu (wuwei19850318@gmail.com).

<svg id="p7.pic1" height="462.77" overflow="visible" version="1.1" viewBox="0 0 675 462.77" width="675"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" stroke-width="0.4pt" transform="translate(0,462.77) matrix(1 0 0 -1 0 0)"><g style="--ltx-fill-color:#C9DAEF;" fill="#C9DAEF" fill-opacity="1.0"><path style="stroke:none" d="M 0 6.46 L 0 456.32 C 0 459.88 2.89 462.77 6.46 462.77 L 668.54 462.77 C 672.11 462.77 675 459.88 675 456.32 L 675 6.46 C 675 2.89 672.11 0 668.54 0 L 6.46 0 C 2.89 0 0 2.89 0 6.46 Z"></path></g><g style="--ltx-fill-color:#F7FBFF;" fill="#F7FBFF" fill-opacity="1.0"><path style="stroke:none" d="M 0.55 6.46 L 0.55 456.32 C 0.55 459.58 3.2 462.22 6.46 462.22 L 668.54 462.22 C 671.8 462.22 674.45 459.58 674.45 456.32 L 674.45 6.46 C 674.45 3.2 671.8 0.55 668.54 0.55 L 6.46 0.55 C 3.2 0.55 0.55 3.2 0.55 6.46 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 28.11 39)"><foreignObject style="--ltx-fo-width:52.61em;--ltx-fo-height:29.16em;--ltx-fo-depth:1.36em;font-size:10pt;" height="422.3" overflow="visible" transform="matrix(1 0 0 -1 0 403.55)" width="727.97"><span id="p7.pic1.1" style="width:52.61em;"><span id="p7.pic1.1.1"><span id="p7.pic1.1.1.1" style="font-size:120%;--ltx-fg-color:#103CC8;">Abstract</span></span> <span id="p7.pic1.1.2"><span id="p7.pic1.1.2.1" style="font-size:90%;">Existing long-horizon agent benchmarks often emphasize final task success while providing limited assessment of intermediate execution validity. Yet real-world business operations require agents to navigate extensive, potentially outdated or conflicting policies while satisfying critical constraints throughout execution. These requirements are particularly consequential in high-stakes domains such as payments, where intermediate violations can incur financial losses or regulatory consequences regardless of the final outcome. To bridge this evaluation gap, we introduce BizBench, a multi-turn benchmark grounded in real-world procedures from a leading payments company. Its executable environment integrates 789 knowledge documents and 601 discoverable business tools, with consistent policies, states, and tool behavior. The benchmark comprises 50 tasks involving resource constraints, temporal dependencies, prior commitments, and conflicting or outdated guidance. Each task is validated through reference execution, while deterministic checks assess both goal attainment and execution validity without prescribing a single solution path. Experiments reveal substantial limitations even among frontier models: Claude Opus 5 and GPT-6 Sol achieve strict success rates of only 64.0% and 61.3%, respectively. For Qwen3.8-27B, goal attainment reaches 42.0%, but strict success drops to 32.7%, demonstrating how outcome-based evaluation can mask invalid execution. Beyond success rates, DeepSeek-V4.1-Flash averages 191.3 tool calls per run, approximately 70% more than reference executions, revealing substantial execution overhead. Overall, BizBench establishes a testbed for evaluating and advancing long-horizon agents beyond task completion, toward reliable and constraint-compliant execution in complex business environments.</span></span> <span id="p7.pic1.1.3"><span id="p7.pic1.1.3.1" style="font-size:80%;--ltx-fg-color:#000000;">Keywords: <span id="p7.pic1.1.3.1.1">long-horizon agents, business workflows, payment systems, benchmark evaluation</span></span></span></span></foreignObject></g></g></svg>

## 1 Introduction

![Refer to caption](https://arxiv.org/html/2610.20424v1/benchmark_overview.png)

Figure 1: Overview of BizBench construction. Business workflows are normalized into an executable environment; tasks combine consequential dependencies with separate goal, process, and protection criteria, and are validated using reference executions and targeted counterexamples.

Advances in artificial intelligence are transforming real-world business operations, with customer service providing a representative example. Early FAQ-based systems addressed user queries by matching them against curated question–answer pairs [^26] [^14]. Although effective for isolated queries, these systems offered limited support for contextual understanding across multiple turns. Subsequent advances in deep neural networks enabled end-to-end task-oriented dialogue systems, extending customer service from single-turn question answering to multi-turn task resolution [^24] [^3] [^15]. By tracking conversational context and incorporating external knowledge, these systems supported more sophisticated interactions, but remained largely constrained by predefined dialogue acts, slot schemas, and short-horizon state tracking. More recently, the emergence of large language models (LLMs) has driven a further transition toward agentic customer service, enabling increasingly autonomous execution of complex business workflows through policy interpretation, multi-step planning, and external tool orchestration [^39] [^31]. Unlike conventional dialogue systems, such agents can take actions that alter business states, commit resources, and constrain subsequent decisions. Consequently, reliable deployment requires not only successful task completion but also adherence to business requirements throughout the execution process [^25].

This transition toward autonomous business execution introduces two fundamental challenges. First, agents must maintain execution validity at critical intermediate steps, rather than merely achieve the desired final outcome. While exploratory actions may be permissible, certain business constraints must remain satisfied throughout execution, and violating them can constitute task failure regardless of the eventual outcome. For example, an unauthorized payment remains a compliance violation even if the transferred funds are subsequently returned. Thus, successful task completion does not necessarily imply valid execution. Second, agents must identify and apply the authoritative business rules governing their actions. In real-world operations, business rules are distributed across heterogeneous sources, including policy manuals, FAQs, and operational notices [^29]. These sources are maintained by different teams and updated at different times, allowing outdated guidance to coexist with current policies [^23]. Moreover, seemingly conflicting instructions may differ in their applicability across jurisdictions, products, or effective periods. Consequently, retrieving relevant information is insufficient: agents must determine which rules are authoritative, current, and applicable to the specific business context [^21]. Although existing long-horizon agent benchmarks evaluate policy-governed tool use and knowledge access [^18], evaluations centered primarily on final task success may fail to capture violations of critical intermediate constraints or incorrect application of business rules. This limitation leaves an important gap between benchmark performance and the assurance required for reliable deployment in real-world business environments.

We therefore introduce BizBench to evaluate whether agents can identify applicable rules before taking consequential actions and complete business requests while maintaining valid execution throughout. The benchmark comprises 50 long-horizon tasks grounded in real-world business workflows from a leading global payments company. These tasks combine tool use with multi-turn customer dialogue: a user simulator provides customer-specific information and responds to approval requests throughout execution. To test rule interpretation before action, we provide current and historical guidance with explicit scopes and effective periods across policy documents. Agents must determine which instructions govern the current request and use accompanying tool documentation to discover and invoke relevant tools. We instantiate these business workflows in a stateful environment, linking them through shared resources, timing requirements, and prior commitments. The environment retains action consequences, so later decisions must account for commitments already made.

To detect violations that final task success can conceal, a deterministic evaluator checks both outcomes and recorded execution histories against task goals and applicable rules. Success requires completing the requested goals while satisfying prior authorization requirements, persistent constraints, and restrictions on side effects. Successful task completion therefore cannot compensate for intermediate violations, while different legitimate strategies remain acceptable. Reference replays verify that goals and constraints are jointly satisfiable; alternative valid executions and targeted violations test whether the evaluator accepts valid solutions and rejects invalid ones.

Our experiments reveal that even advanced models such as GPT-6 Sol struggle on BizBench, achieving a strict success rate of only 61.3%. Performance also varies substantially across runs, with only 40.0% of tasks successfully completed in all three attempts, raising concerns about the reliability of frontier models in real-world business deployments. By evaluating both final outcomes and execution histories, BizBench identifies invalid executions that outcome-only evaluation would incorrectly deem successful. For instance, four DeepSeek-V4.1-Flash runs achieve their goals and finish above the required cash-reserve threshold, despite having breached it at intermediate steps. The challenges are even more pronounced for smaller models. Qwen3.5-9B, for example, averages 187.2 tool calls per run, more than half of which result in errors, primarily from attempts to access non-public resources. None of its 150 runs successfully achieves all task objectives. Together, these findings reveal complementary limitations in execution consistency, process compliance, and effective tool use.

BizBench combines: (1) long-horizon tasks grounded in real-world payment workflows, linked by shared resources, deadlines, and commitments; (2) distributed guidance that requires identifying applicable rules across scopes, versions, and effective periods; and (3) deterministic checks of goals, process compliance, and protection requirements over business states and execution histories, while accepting different valid strategies. These characteristics establish BizBench as a rigorous, business-grounded testbed for investigating how agents coordinate information gathering, planning, and action to accomplish complex business tasks while maintaining execution validity throughout.

## 2 Related Work

Long-horizon agent benchmarks. Agent benchmarks assess reasoning and tool use in interactive environments [^17] [^20]. Web and desktop benchmarks cover shopping, browsing, and computer operation [^36] [^7] [^41] [^13] [^33]. SWE-bench evaluates repository-level issue resolution, while Terminal-Bench tests broader technical tasks through final-state checks [^12] [^19]. SWE-Milestone checks feature completion and regressions at successive milestones [^6]; Long-Horizon-Terminal-Bench measures partial progress through subtask checks on the final state [^16]. While these benchmarks emphasize technical progress and software integrity, BizBench models business environments with scattered tool documentation, noisy, outdated, or conflicting information, and changing conditions. It checks intermediate actions against applicable business requirements. An action’s validity depends on the approvals, funds, and policy in force when it occurs.

Agents in business workflows. Business-oriented benchmarks introduce operational rules and organizational context. The $\tau$ family studies policy-governed interaction, user–agent coordination, and knowledge-grounded workflows [^39] [^1] [^29]. Enterprise suites cover browser-based knowledge work, compositional workflows, workplace collaboration, and CRM operations [^8] [^2] [^34] [^10] [^11]. AutomationBench evaluates final application states without prescribing tool-call sequences, preserving flexibility in how agents solve tasks [^28]. BizBench likewise allows exploration and alternative strategies, while checking authorization and other business requirements at consequential steps, such as whether a transfer was approved before execution.

Long-horizon planning and adaptation. Tool-use learning and reasoning–action interleaving provide foundations for language agents [^27] [^38]. Reflection, skill reuse, and search support multistep reasoning and planning [^30] [^32] [^37] [^40], while clarification research examines when additional information is useful [^9]. BizBench focuses on replanning in business systems where permitted actions can undermine later obligations and both acting and waiting can incur costs. Plans must accommodate commitments already made.

## 3 BizBench

BizBench evaluates agents that execute customer requests across real-world business workflows. Each task combines an objective, an initial business state, a customer scenario, and acceptance criteria. Agents use a shared environment of documents, records, and executable tools. Success requires fulfilling the request while respecting the requirements that govern its intermediate execution.

### 3.1 Business Context and Reconstructed Environment

BizBench draws on business workflows from one of the world’s leading payments and financial technology companies. The company supports merchants and enterprises through cross-border payments, foreign exchange, and treasury services. Customer requests can span multiple currencies, legal entities, and financial operations. In practice, deployed agents must reconcile fragmented records and apply the right rules, even when payments or reviews are still pending. An action accepted by one system can still consume funds or capacity needed to fulfill a later obligation.

To preserve the confidentiality of business rules, we abstract sensitive details from the source workflows. We reconstruct their key business logic and execution mechanisms in an executable environment. Agents consult documents for business rules and tool documentation, and query records to establish the customer’s current business state. They interact with a user simulator to obtain private customer information and required approvals. Business tools allow agents to execute operations and inspect their results. The frozen release contains 50 tasks and 789 knowledge documents. Agents have nine always-available tools through which they discover and invoke 601 business capabilities; the user simulator has ten tools. Each run uses an independent copy of the database. Appendix B reports the environment inventory and Golden trace statistics.

### 3.2 Construction Insights from Our Business Workflows

Outdated and conflicting guidance. Business documents can remain accessible after their instructions have been superseded. Apparent conflicts can also arise because two rules govern different products, regions, or effective periods. Resolving a conflict requires establishing which source is authoritative and which rule applies to the particular business event. An expired insurance policy, for example, may still cover a past incident. BizBench includes current and historical guidance with explicit scopes and effective periods, making rule selection part of executing the request.

Authorization and execution validity. General consent does not substitute for approval of a specific operation. Approval must cover the actual operation and its terms, come from an authorized approver, and precede execution. Other requirements, such as a minimum reserve or continuous guarantee coverage, must hold throughout the workflow. An operation accepted by a tool can still breach these requirements. For example, an account holds $60 and must retain at least $20 throughout execution. Paying a $60 retainer leaves the account at zero and immediately breaches this requirement, even though the payment is accepted. Later refunds and adjustments can restore the closing reserve without repairing the earlier breach (Appendix D.3). BizBench therefore evaluates the relevant approvals and state changes throughout execution alongside the requested outcomes.

Delayed information and time-sensitive decisions. Reviews, refunds, and settlements may finish after another obligation requires action. In the delivery case (Appendix C.2), the priority booking window closes before warehouse confirmation arrives. Waiting for that confirmation makes the first delivery deadline unattainable. BizBench represents when information becomes observable and when actions become available, so that waiting can change whether the request remains feasible.

### 3.3 Evaluating Outcomes and Execution

Let $\tau=(s_{0},e_{1},s_{1},\ldots,e_{T},s_{T})$ denote an execution history, where $e_{t}$ is a tool execution or environment event. Task $i$ succeeds when

$$
\operatorname{Success}_{i}(\tau)=G_{i}(\tau)\land P_{i}(\tau)\land F_{i}(\tau).
$$

Here, $G_{i}$ checks the requested outcomes and permitted terminal conditions, $P_{i}$ checks requirements governing execution, and $F_{i}$ checks protected objects and prohibited side effects. These categories are defined by the business requirements being checked; each uses the relevant business states and execution histories as evidence. For example, a payment goal may require an actual settlement receipt and its timestamp, while a reserve requirement needs the balance after each relevant state change.

Checks operate on business states, ledgers, receipts, and event histories. They distinguish an executed action from a proposal, an approval, or a rejected call without side effects. Different valid action sequences can satisfy the same criteria; the evaluator does not match executions to a Golden trace. The primary score is computed by deterministic, executable checks over business states and execution histories, without using an LLM judge.

## 4 Data Construction

We construct multi-turn tasks in which the agent and a user simulator work together to achieve a shared business goal. Drawing on the insights in Section 3.2, we retain current and historical guidance with explicit applicability conditions, introduce temporal dependencies between workflows, and check authorization and intermediate execution against business requirements. We organize data construction into five stages. First, we organize business rules into SOPs and adapt them for simulation (Section 4.1). Second, we build executable tasks by defining states, operations, and acceptance checks, and linking workflows through resource and timing constraints (Section 4.2). Third, we configure a user simulator to disclose customer information and perform customer-side actions through multi-turn interaction (Section 4.3). Fourth, we construct and replay Golden traces to establish executable strategies that satisfy the task requirements (Section 4.4). Finally, we validate task behavior and acceptance checks using alternative executions, violations, and variations in task conditions and execution, alongside expert review (Section 4.5).

### 4.1 Grounding Tasks in Business Workflows

We organize source business documents into structured SOPs that capture the rules and dependencies needed for executable tasks. As summarized in Algorithm 1, we extract candidate workflows with supporting source evidence and group related candidates into workflow plans that organize business branches. These plans are converted into SOPs specifying steps, decisions, transitions, and return paths. The associated rules record their scope, affected objects, prerequisites, actions, and exceptions.

Algorithm 1 Constructing SOPs from business documents

We review the extracted rules against their source evidence and exclude content whose meaning or applicability cannot be established. Differences that can be resolved through scope, version, or effective period are preserved and carried forward into the environment’s documentation. This allows current and historical guidance to coexist while providing the evidence needed to determine which instruction governs a particular operation.

To protect proprietary information, we rewrite sensitive business details consistently across related rules while preserving their decision logic and dependencies. We distinguish requirements grounded in the source documents, interpretations needed to make them executable, and additional constraints introduced during task construction. The resulting SOPs provide the business requirements used to construct the environment and tasks.

### 4.2 Building Executable Tasks

From these SOPs, we construct an executable environment with aligned documents, records, and tools. Documents specify business rules and tool interfaces; synthetic records instantiate entities, accounts, obligations, authorizations, and transaction histories; tools and scheduled events implement the corresponding state changes. For each operation, we align its documented conditions, relevant records, and implemented effects. To represent outdated and conflicting guidance, the synthesized documents include current and historical rules and guidance for related products, with explicit scopes, versions, and effective periods.

We construct tasks by selecting workflows that share business objects or resources, or whose outputs establish prerequisites for other operations. Each task specifies a customer objective, an initial database state, and scheduled events. Additional constraints introduced during task construction are stated in public documents or customer requirements. The facts needed to apply these constraints are available through record queries or customer interaction.

We connect workflows through shared resources, state prerequisites, and timing requirements. Temporal dependencies link scheduled events in one workflow to actions and deadlines in another. Together with delayed information availability, these dependencies create the time-sensitive decisions described in Section 3.2: waiting for an external result may close a required execution window. Because workflows share funds or authorization limits, a permitted action in one can consume resources needed by another obligation. Agents must therefore coordinate decisions across workflows and account for earlier actions when revising their plans. Dependency graphs capture these relationships and conditional branches during task construction.

Acceptance criteria are derived from the customer objective and applicable rules, jointly with the task’s initial conditions and dependencies, before generating Golden traces. Requested outcomes and permitted terminal conditions determine the goal checks $G$; requirements governing execution determine the process checks $P$; and protected objects and prohibited side effects determine the protection checks $F$. We link these checks to their governing rules or customer requirements and identify the relevant evidence in records, ledgers, receipts, and execution histories. For authorization and execution validity, intermediate checks verify that required approval covers the executed terms and precedes the operation, and test continuous constraints at each relevant state change. The checks evaluate the specified business conditions and allow different valid action sequences. Golden traces subsequently establish that the requirements are jointly satisfiable, as described in Section 4.4.

### 4.3 Setting Up the User Simulator

We configure an LLM as the user simulator for each task using a common interaction protocol and a task-specific customer scenario. The scenario specifies the customer’s objective, private facts, preferences, supporting materials, and opening request. The common protocol defines the customer role, permitted customer-side actions, and turn-taking behavior. Together, they guide the simulator’s responses based on the conversation and the results of its own tool calls.

The interaction begins with the opening request; other customer information is disclosed when relevant questions or proposals arise. The agent must ask for the constraints and materials needed to proceed, while the simulator answers from its scenario and customer-facing receipts. Fixed facts and constraints remain consistent across turns. Where the scenario permits negotiation, a revised preference must be stated explicitly. This requires the agent to elicit customer-specific requirements and retain their terms as the business workflow progresses.

The simulator also performs customer-side operations in the shared environment, such as submitting an available document or approving a proposed transaction. Approval is recorded against a specific request and its current terms; changed terms require renewed approval. Factual questions take priority over action requests. The simulator performs one requested write or wait at a time, reports its actual result, and returns control to the agent. If a requested action fails or is unclear, it reports the problem and asks for clarification. The resulting dialogue alternates customer input and actions with the agent’s investigation and execution until the interaction ends.

### 4.4 Constructing and Replaying Golden Traces

We construct Golden traces to establish that each task has at least one executable strategy satisfying its goal, process, and protection requirements. This is especially important for linked workflows, where shared resources and timing constraints can make otherwise feasible workflows incompatible.

We construct reference strategies from the SOPs, task conditions, and dependencies between workflows. Each strategy is executed through the tools and customer-side actions used in evaluation. The resulting Golden trace records the actions and their consequences.

We replay each trace from the task’s initial state and evaluate it using the goal, process, and protection checks defined for the task (Section 4.2). Even when individual workflows have already been validated, we replay the complete task to check their interactions through shared resources, state prerequisites, and timing constraints. Each of the 50 released tasks has a passing Golden trace.

### 4.5 Task Validation and Expert Review

Task validation checks whether the evaluator accepts valid executions and detects violations of the stated requirements. We test valid alternatives that use different permitted routes or action orders, and targeted violation traces that break specific requirements. A temporary reserve breach, for example, must fail the process check even if later transactions restore the balance.

We also change facts that determine whether an operation is valid or feasible, and verify that the same acceptance checks yield the expected judgments under the modified conditions. Such changes may require a different execution strategy. In contrast, operational variations that preserve compliance and business effects should leave the evaluation outcome unchanged. In particular, an idempotent retry permitted by the tool contract should produce no additional business effect.

Five researchers and a team of business-domain experts reviewed the tasks and acceptance checks against customer requests, documents, business records, and validation traces. They examined whether the linked workflows formed coherent business scenarios, whether agents could obtain the information needed for their decisions, and whether each check represented its governing rule or customer requirement. Identified inconsistencies in the documents, tools, simulator, or evaluator were corrected, and the affected executions were rerun. The final benchmark includes only tasks that passed both validation and expert review.

## 5 Experiments

Our experiments examine whether agents complete customer requests while satisfying the requirements that govern execution. We report goal, process, protection, and strict success across models, then use information ablations and execution traces to study customer interaction, document retrieval, and long-horizon tool use. We also assess the stability of the user simulator.

### 5.1 Experimental Setup

We evaluate BizBench on the same 50 tasks with proprietary and open-source models [^22] [^4] [^5] [^35] (Table 1). Each run starts from an independent copy of the initial database and uses the same public documents, tools, and acceptance criteria. In the default condition, agents retrieve documents, discover business capabilities, and interact with a DeepSeek-V4.1-Flash user simulator. Golden traces, executable checks, and unrevealed event outcomes remain unavailable to the agent.

Table 1: Goal ($G$), process ($P$), protection ($F$), intermediate failure, and strict success (%). Intermediate failure means that a process or protection requirement failed. Claude Opus 5 and Muse Spark 1.3 have one run per task; the other models have three.

| Model | Goal $\mathbf{(G)}$ | Process $\mathbf{(P)}$ | Protection $\mathbf{(F)}$ | IF $\mathbf{(\neg(P\land F))}$ | Strict $\mathbf{(G\land P\land F)}$ |
| --- | --- | --- | --- | --- | --- |
| Claude Opus 5 | 64.0 | 96.0 | 98.0 | 4.0 | 64.0 |
| GPT-6 Sol | 64.7 | 94.7 | 100.0 | 5.3 | 61.3 |
| GLM-5.3-Flash | 48.0 | 79.3 | 87.3 | 29.3 | 43.3 |
| DeepSeek-V4.1-Flash | 46.7 | 92.0 | 96.7 | 9.3 | 43.3 |
| DeepSeek-V4-Pro | 41.3 | 85.3 | 88.7 | 24.7 | 39.3 |
| Muse Spark 1.3 | 38.0 | 94.0 | 98.0 | 6.0 | 38.0 |
| Qwen3.8-27B | 42.0 | 74.0 | 93.3 | 28.0 | 32.7 |
| DeepSeek-V4-Flash | 7.3 | 53.3 | 95.3 | 47.3 | 5.3 |
| Qwen3.5-397B-A17B | 1.3 | 46.7 | 93.3 | 56.7 | 0.7 |
| Qwen3.5-9B | 0.0 | 18.7 | 89.3 | 83.3 | 0.0 |

Figure 2: Reliability and resource use for models with three runs per task. Left: pass^k averages, over all $k$ -run subsets, the fraction of tasks that succeed in every selected run. Right: mean assistant turns, distinct documents read, and assistant tool calls per run.

The runner imposes no cumulative limit on generated tokens, tool calls, or scheduler steps, and sets per-response output-token limits high enough to avoid routine truncation. Runs retain a wall-clock timeout and a tool-error threshold. Each model request includes the accumulated dialogue and tool history. Following [^29], if a provider reports context-window overflow, the oldest quarter of eligible knowledge-search and document-read tool responses is replaced in the model-facing context, while the complete execution record is preserved.

For models evaluated three times per task, we average single-run success across the three runs; other models have one run per task. Information ablations use the same tasks, bank-side tools, database, and acceptance criteria. We track infrastructure and simulator protocol failures separately from business outcomes, and resume transient transport interruptions from the verified prior state.

### 5.2 Overall Performance and Process Validity

The main comparison separates goal attainment from valid execution using the criteria in Equation 1. Table 1 reports the pass rates for goals and permitted terminal conditions ($G$), process requirements ($P$), protection requirements ($F$), strict success ($G\land P\land F$), and intermediate failure (IF, $\neg(P\land F)$). We report the predefined goal, process, and protection checks separately, with strict success requiring all three.

Frontier models perform well but leave substantial room for improvement: Claude Opus 5 achieves the highest strict success rate at 64.0%, followed by GPT-6 Sol at 61.3%. GLM-5.3-Flash and DeepSeek-V4.1-Flash each achieve 43.3% strict success, followed by DeepSeek-V4-Pro at 39.3%, while Qwen3.5-9B completes none of its 150 runs. Every model incurs intermediate failures, from 2 of 50 runs (4.0%) for Claude Opus 5 to 125 of 150 (83.3%) for Qwen3.5-9B; such failures are generally more frequent among lower-scoring models. Process pass rates are below protection pass rates for every model, spanning 18.7–96.0% for $P$ versus 87.3–100.0% for $F$. Figure 2(a) shows declining reliability: at $k=3$, GPT-6 Sol reaches 40.0%, DeepSeek-V4.1-Flash 26.0%, and GLM-5.3-Flash 22.0%. At $k=3$, Qwen3.8-27B reaches 10.0%, and DeepSeek-V4-Flash and both Qwen3.5 models reach 0%. These declines indicate that the models remain unreliable across repeated runs.

### 5.3 Information Acquisition

Table 2: DeepSeek-V4.1-Flash strict success under three information conditions on 50 tasks.

| Information condition | Strict (%) |
| --- | --- |
| Default condition | 43.3 |
| \+ Gold-doc | 50.0 |
| \+ Full customer disclosure | 70.0 |

Table 3: DeepSeek-V4.1-Flash strict success with tool-call caps (three-run mean); $R_{i}$ is the Golden call count.

| Tool-call cap | Strict (%) |
| --- | --- |
| $1.2\times R_{i}$ | 0.7 |
| $1.5\times R_{i}$ | 6.7 |
| $2.0\times R_{i}$ | 26.7 |
| No cap | 43.3 |

We examine how information acquisition affects task performance, focusing on two sources: business documents and customer interaction. Gold-doc provides applicable documents directly, while full customer disclosure supplies all customer-known task information in the opening request without a user simulator. Required customer approvals remain in force.

Table 3 compares these conditions with the default condition. Strict success increases from 43.3% to 50.0% with Gold-doc and to 70.0% with full customer disclosure. The larger gain from full disclosure implies that eliciting customer-specific constraints and retaining their terms through execution are particularly difficult. Gold-doc removes the search for applicable documents, but agents must still interpret their rules and apply them across linked actions. Its smaller gain suggests that document retrieval accounts for only part of the information-use challenge. Even with all customer facts available at the outset, 30.0% of tasks remain unsolved, highlighting the remaining difficulty of planning and valid execution.

### 5.4 Long-Horizon Behavior and Budget Sensitivity

The Golden traces average 111.8 assistant tool calls. DeepSeek-V4.1-Flash averages 191.3 calls (1.71 times the reference). The excess is concentrated in information access: database queries average 111.1 versus 59.2 in the Golden traces, and knowledge searches or document reads average 43.3 versus 11.5, while business capability calls and request executions are similar (26.9 versus 28.7).

Figure 2(b) shows that longer traces need not reflect greater progress across models. GLM-5.3-Flash matches DeepSeek-V4.1-Flash in strict success with 118.3 versus 191.3 tool calls and 9.4 versus 20.1 documents; Qwen3.5-397B-A17B uses 216.4 calls but succeeds only once in 150 runs. Appendix D reports the full call distributions.

Table 3 retrospectively limits each task to $\lceil\alpha R_{i}\rceil$ assistant tool calls, where $R_{i}$ is its Golden trace call count. Across three runs per task, strict success falls from 65/150 (43.3%) without a cap to 1/150 (0.7%) at $1.2\times$, 10/150 (6.7%) at $1.5\times$, and 40/150 (26.7%) at $2.0\times$. Even twice the reference call count excludes many otherwise successful runs, quantifying the cost of the agents’ information search and repeated checking.

### 5.5 Trajectory Analysis

Table 4: Execution-trace statistics across stronger and weaker models. Counts are means per run; repeated database reads have identical tool names, arguments, and responses. The last column counts runs reaching the goal but failing process or protection requirements.

| Model | Assistant tool calls | Repeated database reads | Tool errors | $\mathbf{G\land\neg(P\land F)}$ |
| --- | --- | --- | --- | --- |
| DeepSeek-V4.1-Flash | 191.3 | 16.4 | 2.0 | 5/150 |
| Qwen3.8-27B | 129.2 | 7.8 | 4.2 | 14/150 |
| DeepSeek-V4-Flash | 168.0 | 23.7 | 8.2 | 3/150 |
| Qwen3.5-9B | 187.2 | 16.5 | 101.6 | 0/150 |

Progress and repetition. Table 4 distinguishes additional tool use from literal repetition: a repeated database call has the same tool, arguments, and returned content as an earlier call in that run. DeepSeek-V4.1-Flash makes 16.4 such calls per run; DeepSeek-V4-Flash makes 23.7 despite making fewer tool calls overall. Qwen3.5-9B receives 101.6 tool-error replies per run, 71% of them for querying non-public resources, and reads only 6.4 distinct documents, compared with 20.1 for DeepSeek-V4.1-Flash. Thus, long traces mix information gathering with redundant reads and invalid navigation; the number of tool calls alone does not measure progress.

Intermediate violations. Among DeepSeek-V4.1-Flash runs, five reach the requested goal but fail the full criteria: four cross a required cash-reserve floor before later restoring the balance, and one attempts execution before approval and receives a rejection. Qwen3.8-27B has 14 such runs, including eight rejected pre-approval execution attempts; DeepSeek-V4-Flash has three. Qwen3.5-9B fails process requirements in 122/150 runs, including 88 pre-approval execution attempts, but reaches no goals. These histories explain why final goal checks alone overstate valid execution.

Business-document scope. Golden traces contain reads of 5.4 distinct documents per task, whereas DeepSeek-V4.1-Flash opens 20.1. Additional reads include documents on related payment operations and products with similar terminology but different applicability. This shows that the complexity of the knowledge base makes identifying applicable guidance challenging for the model. Appendix D.4 gives a tax-payment example.

### 5.6 Simulator Reliability and Evaluation Robustness

We assess whether the user simulator follows the interaction protocol under two prompt variants. The revised prompt explicitly specifies the order of customer actions and when to return control to the agent. Using DeepSeek-V4.1-Flash for both roles, we observe protocol violations on 4 of 50 tasks with the original prompt and none with the revised prompt. These violations involve batched approvals or further tool use before returning control. We therefore adopt the revised prompt as the default user-simulator prompt in our evaluations. Appendix D.2 details the protocol and paired analysis.

We also examine sensitivity to the choice of user-simulator model. Qwen3.8-27B executes the tasks in all four conditions. Figure 3 reports the mean strict success rate over three runs for each simulator. The mean rates range from 30.7% to 36.0%. The largest deviation from the default DeepSeek-V4.1-Flash setting (32.7%) is 3.3 percentage points. This small spread suggests that agent performance is relatively robust to the choice of user simulator in this comparison.

Figure 3: User-simulator model comparison using Qwen3.8-27B as the agent. Bars show the mean strict success rate over three runs; DeepSeek-V4.1-Flash is the default simulator.

## 6 Conclusion

With BizBench, business requirements become testable conditions on both the outcomes and execution of long-horizon tasks. Our experiments show that task completion, process compliance, and consistency across runs reveal different weaknesses in current agents. Information ablations suggest that obtaining the right customer facts can substantially improve performance, while trajectory analysis shows that extensive tool use does not necessarily indicate meaningful progress. These findings motivate closer coordination between information gathering and action selection: agents need to establish when they have sufficient evidence to proceed and which obligations must remain satisfied as execution unfolds.

## References

## Appendix A A Complete Task Example

Figure introduces Q03, which links receipts reconciliation with an account application. Panel (a) presents the workflow dependencies, and panel (b) illustrates the corresponding agent interaction. We explain below how the funding decision connects these workflows.

The three routes in Table 5 debit the same $60 reserve after Acacia’s file is closed. In the Golden trace, the customer explicitly raises the total fee cap from $50 to $60 and approves route B, which funds a single $50 review submission at $t=8$; the application is approved at $t=18$, within the deadline of $t=19$. From the same release time, route A credits funds at $t=18$, leaving the ten-minute review beyond the deadline, while route C falls one cent short of the submission fee. These comparisons are derived from the release terms, rather than observed model failures. The customer permits neither a top-up nor transfers from unrelated accounts.

Table 5: Three release routes for the same $60 reserve. The $50 review fee is additional.

| Release route | Net credit | Fee | Delay |
| --- | --- | --- | --- |
| A: Standard | $60 | $0 | 10 minutes |
| B: Same-cycle | $50 | $10 | Immediate |
| C: Reduced-net | $49.99 | $10.01 | Immediate |

Each task comprises *a customer objective and opening request*; *a customer scenario* governing private facts and cooperation; *an initial state* recording resources, histories, obligations, and scheduled events; *access to shared documents and executable tools*; and *deterministic acceptance criteria* for final outcomes and execution histories. A replayable Golden trace and validation evidence establish feasibility and check the evaluator’s treatment of valid alternatives and violations. The displayed dialogue is constructed from a Golden trace; the SOP graph, Golden trace, and executable checks are not supplied to the evaluated agent.

## Appendix B Dataset Statistics

All statistics refer to the 50 released tasks. Golden trace statistics use one validated trace per task. Table 7 summarizes the tasks and shared environment. Table 7 reports document lengths and Golden trace statistics.

Table 6: Task and environment counts in BizBench.

| Statistic | Count |
| --- | --- |
| Tasks | 50 |
| Always-available agent tools | 9 |
| Discoverable business capabilities | 601 |
| User-simulator tools | 10 |
| Knowledge documents | 789 |
| Total document-body tokens | 598,827 |
| Queryable database collections | 398 |
| Database records | 2,994 |

Table 7: Document lengths and Golden trace statistics.

<table><thead><tr><th>Metric</th><th>Mean</th><th>Median</th><th>Range</th></tr><tr><th colspan="4">Knowledge base: per document</th></tr><tr><th>Document length (tokens)</th><th>759.0</th><th>452</th><th>44–10,755</th></tr><tr><th colspan="4">Golden traces: per task</th></tr></thead><tbody><tr><th>Assistant tool calls</th><td>111.8</td><td>100.5</td><td>51–282</td></tr><tr><th>User-simulator tool calls</th><td>28.6</td><td>21.5</td><td>10–74</td></tr><tr><th>Distinct documents read</th><td>5.4</td><td>5</td><td>2–15</td></tr><tr><th>Distinct business records read</th><td>29.9</td><td>23.5</td><td>4–96</td></tr><tr><th>Executed business requests</th><td>14.2</td><td>11</td><td>6–36</td></tr></tbody></table>

Documents, tools, and records. Each document is counted once by its identifier. Token counts use document bodies and the cl100k\_base tokenizer, excluding titles and metadata. Tool counts distinguish always-available agent tools, discoverable business capabilities, and user-simulator tools across product portals. Database counts describe the shared initial database before task-specific changes, including background records and empty collections; 227 of its 398 queryable collections are nonempty. Private customer files and hidden event payloads are excluded. Collections are counted by query resource name.

Golden traces. Assistant and user-simulator tool calls are counted separately, and batched calls count individually. The traces average 111.8 assistant tool calls and 28.6 user-simulator tool calls per task.

Golden traces demonstrate feasible strategies, not minimum-length solutions.

Each dispatch call counts once toward its target capability; unlocking a capability counts as a separate tool call. Distinct documents are deduplicated by document identifier. Distinct records count successful full-record reads, deduplicated by resource name and record identifier. Executed business requests count distinct successfully executed request identifiers.

## Appendix C Illustrative Business Cases

The following examples focus on payment and delivery decisions in Q24 and Q34. All monetary amounts are in US dollars; times are logical minutes.

### C.1 A Limited Net-Delivery Guarantee (Q24)

Two suppliers must receive their exact remaining invoice balances under current banking instructions. The customer permits at most $75 in total bank charges, including the earlier transfer’s return charge. After that transfer resolves, the remaining balances are $300 and $400. A single-use guarantee offers exact net delivery for a fixed fee; the standard route exposes the recipient to intermediary deductions, followed by a separately charged top-up.

Consider assigning the guarantee to the $300 balance and sending the $400 balance through the standard route. Both suppliers ultimately receive the correct amounts. However, the $20 return charge, $20 guarantee fee, $35 intermediary deduction, and $5 top-up fee total $80. The fee budget is exceeded despite correct final payments. The case requires allocating a limited service across obligations and accounting for charges incurred at different stages of settlement.

### C.2 Payment Reconciliation and Delivery Windows (Q34)

A merchant must reconcile an already-paid order without charging again and deliver three compatible units: one rated at least 15 by minute 2, and two rated at least 10 by minute 5. All require the same socket. The priority delivery service takes one minute but must be booked by minute 0; ordinary delivery takes three minutes.

Consider repairing the merchant mapping and propagating two captures totaling $10 and a $1 refund, yielding the order’s $9 net payment, before waiting for the warehouse result at minute 1. The priority booking is then rejected because its window has closed. Compatible inventory is identified and the two later units arrive on time, but the early unit cannot meet its deadline through the remaining service. This sequence shows why an agent must coordinate information gathering with expiring service rights: correct reconciliation and suitable stock alone do not complete the commercial objective.

## Appendix D Execution-History Analysis

### D.1 Model execution length and tool use

We analyze DeepSeek-V4.1-Flash execution traces in the default condition. Table 8 counts batched calls individually and separates assistant and user-simulator tool calls. Database queries use search\_records or get\_record. An identical repeated database read has the same name, arguments, and response as an earlier read in the same run, excluding queries that observe changed state.

Table 8: DeepSeek-V4.1-Flash tool use per run in the default condition.

| Metric | Mean | Median | 90th percentile |
| --- | --- | --- | --- |
| Assistant tool calls | 191.3 | 182 | 287 |
| User-simulator tool calls | 28.2 | 26 | 41 |
| Database queries | 111.1 | 101 | 180 |
| Distinct documents read | 20.1 | 22 | 34 |
| Identical repeated database reads | 16.4 | 14 | 32 |

Successful runs average 13.7 identical repeated database reads, versus 18.5 in failed runs. Rechecking unchanged records is measurable redundancy, although some rechecks may be deliberate validation.

### D.2 User-simulator turn-taking reliability

We examine whether the user simulator returns control to the agent after customer-side operations. After a successful write or wait, it must report the result before using another tool. We count batching multiple writes or waits, or continuing tool use before reporting the result and returning control, as protocol violations.

The comparison uses the same 50 tasks and DeepSeek-V4.1-Flash in both roles, reusing an existing complete evaluation for the revised prompt. The original prompt already requests one write at a time; the revision clarifies how to prioritize mixed questions and action requests and when to return control. Violations occur on four tasks (8%) with the original prompt: two involve batched customer approvals and two involve continued portal use after a tool response. No such violations occur with the revised prompt (0%; paired exact McNemar $p=0.125$). These observations motivate our use of the revised prompt in benchmark evaluations.

### D.3 Example of goal attainment with process violations

The single-run audit in the default condition contains two executions with $G=1$ and $P=0$.

Rejected premature execution (Q13). The agent coordinates insurance settlement and a stored-value order payment. It invokes execute\_request on the payment before portal approval; the tool returns CUSTOMER\_APPROVAL\_REQUIRED, with no payment or balance change. The customer then approves and the agent completes the goals. The premature attempt violates approval discipline: $G=1$, $P=0$, $F=1$. No unauthorized transfer occurs.

Actual reserve breach (Q18). The customer needs interest corrections and accountant payments: a $60 retainer at minute 0 and a $40 balance by minute 2, while retaining $20 in the operating account throughout. The agent pays the retainer from the initial $60, leaving zero. A $18.66 refund settles and the agent posts a $50 adjustment at minute 1; the final account balance after the remaining payment is $28.66. The goals and closing reserve pass, but the earlier zero balance violates the continuous requirement: $G=1$, $P=0$, $F=1$. Only the execution history exposes this breach.

### D.4 Business-document scope in retrieval

In Q01, the customer asks the agent to pay suppliers in euros and pounds and match earlier tax payments to the correct periods. The applicable Operations Desk rules are described in DESK-tax and DESK-fx. Searching for tax payment matching periods reconciliation returns PX-B-77, an overpayment-credit document for a different product, in first position and PX-B-76, a tax-agent document for that product, in fifth position. The agent opens both documents, whose terminology matches the query although neither governs this Operations Desk task.

[^1]: Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. $\tau^{2}$ -bench: Evaluating conversational agents in a dual-control environment, 2025. URL [https://arxiv.org/abs/2506.07982](https://arxiv.org/abs/2506.07982). arXiv preprint arXiv:2506.07982.

[^2]: Léo Boisvert, Megh Thakkar, Maxime Gasse, Massimo Caccia, Thibault Le Sellier De Chezelles, Quentin Cappart, Nicolas Chapados, Alexandre Lacoste, and Alexandre Drouin. WorkArena++: Towards compositional planning and reasoning-based common knowledge work tasks. In *Advances in Neural Information Processing Systems*, volume 37, pages 5996–6051. Curran Associates, Inc., 2024. doi: 10.52202/079017-0195. URL [https://doi.org/10.52202/079017-0195](https://doi.org/10.52202/079017-0195).

[^3]: Paweł Budzianowski, Tsung-Hsien Wen, Bo-Hsiang Tseng, Iñigo Casanueva, Stefan Ultes, Osman Ramadan, and Milica Gasic. Multiwoz-a large-scale multi-domain wizard-of-oz dataset for task-oriented dialogue modelling. In *Proceedings of the 2018 conference on empirical methods in natural language processing*, pages 5016–5026, 2018.

[^4]: DeepSeek-AI. Deepseek-v4.1-flash: Pushing the limits of kv cache compression, 2026a. URL [https://arxiv.org/abs/2609.19969](https://arxiv.org/abs/2609.19969).

[^5]: DeepSeek-AI. Deepseek-v4: Towards highly efficient million-token context intelligence, 2026b. URL [https://arxiv.org/abs/2606.19348](https://arxiv.org/abs/2606.19348).

[^6]: Gangda Deng, Zhaoling Chen, Zhongming Yu, Haoyang Fan, Yuhong Liu, Yuxin Yang, Dhruv Parikh, Rajgopal Kannan, Le Cong, Mengdi Wang, Qian Zhang, Viktor Prasanna, Xiangru Tang, and Xingyao Wang. SWE-Milestone: Evaluating AI Agents on Continuous Software Evolution, 2026. URL [https://arxiv.org/abs/2603.13428](https://arxiv.org/abs/2603.13428). ICML 2026; arXiv:2603.13428.

[^7]: Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, and Yu Su. Mind2Web: Towards a generalist agent for the web. In *Advances in Neural Information Processing Systems*, volume 36, pages 28091–28114. Curran Associates, Inc., 2023. doi: 10.52202/075280-1220. URL [https://doi.org/10.52202/075280-1220](https://doi.org/10.52202/075280-1220).

[^8]: Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, David Vazquez, Nicolas Chapados, and Alexandre Lacoste. WorkArena: How capable are web agents at solving common knowledge work tasks? In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *Proceedings of the 41st International Conference on Machine Learning*, volume 235 of *Proceedings of Machine Learning Research*, pages 11642–11662. PMLR, 2024. URL [https://proceedings.mlr.press/v235/drouin24a.html](https://proceedings.mlr.press/v235/drouin24a.html).

[^9]: Anmol Gulati, Hariom Gupta, Elias Lumer, Sahil Sen, and Vamse Kumar Subbiah. Ask early, ask late, ask right: When does clarification timing matter for long-horizon agents?, 2026. URL [https://arxiv.org/abs/2605.07937](https://arxiv.org/abs/2605.07937). arXiv preprint arXiv:2605.07937.

[^10]: Kung-Hsiang Huang, Akshara Prabhakar, Sidharth Dhawan, Yixin Mao, Huan Wang, Silvio Savarese, Caiming Xiong, Philippe Laban, and Chien-Sheng Wu. CRMArena: Understanding the capacity of LLM agents to perform professional CRM tasks in realistic environments. In Luis Chiruzzo, Alan Ritter, and Lu Wang, editors, *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 3830–3850, Albuquerque, New Mexico, April 2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.naacl-long.194. URL [https://aclanthology.org/2025.naacl-long.194/](https://aclanthology.org/2025.naacl-long.194/).

[^11]: Kung-Hsiang Huang, Akshara Prabhakar, Onkar Thorat, Divyansh Agarwal, Prafulla Kumar Choubey, Yixin Mao, Silvio Savarese, Caiming Xiong, and Chien-Sheng Wu. CRMArena-Pro: Holistic assessment of LLM agents across diverse business scenarios and interactions. *Transactions on Machine Learning Research*, 2026. URL [https://arxiv.org/abs/2505.18878](https://arxiv.org/abs/2505.18878).

[^12]: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. SWE-bench: Can language models resolve real-world GitHub issues? In *International Conference on Learning Representations*, pages 54107–54157, 2024. URL [https://openreview.net/forum?id=VTF8yNQM66](https://openreview.net/forum?id=VTF8yNQM66).

[^13]: Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Chong Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Ruslan Salakhutdinov, and Daniel Fried. VisualWebArena: Evaluating multimodal agents on realistic visually grounded web tasks. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 881–905, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.50. URL [https://aclanthology.org/2024.acl-long.50/](https://aclanthology.org/2024.acl-long.50/).

[^14]: Feng-Lin Li, Minghui Qiu, Haiqing Chen, Xiongwei Wang, Xing Gao, Jun Huang, Juwei Ren, Zhongzhou Zhao, Weipeng Zhao, Lei Wang, Guwei Jin, and Wei Chu. AliMe Assist: An intelligent assistant for creating an innovative e-commerce experience. In *Proceedings of the 2017 ACM on Conference on Information and Knowledge Management*, pages 2495–2498. ACM, 2017a. doi: 10.1145/3132847.3133169. URL [https://doi.org/10.1145/3132847.3133169](https://doi.org/10.1145/3132847.3133169).

[^15]: Xiujun Li, Yun-Nung Chen, Lihong Li, Jianfeng Gao, and Asli Celikyilmaz. End-to-end task-completion neural dialogue systems. In *Proceedings of the Eighth International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, pages 733–743, 2017b.

[^16]: Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang, Zhichao Liu, Xiyang Wu, Anhao Li, Yue Yu, Ninghao Liu, Lichao Sun, Haotao Mi, and Leowei Liang. Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading, 2026. URL [https://arxiv.org/abs/2607.08964](https://arxiv.org/abs/2607.08964). arXiv preprint arXiv:2607.08964.

[^17]: Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, and Jie Tang. AgentBench: Evaluating LLMs as agents. In *International Conference on Learning Representations*, pages 52989–53046, 2024. URL [https://openreview.net/forum?id=zAdUB0aCTQ](https://openreview.net/forum?id=zAdUB0aCTQ).

[^18]: Jiarui Lu, Thomas Holleis, Yizhe Zhang, Bernhard Aumayer, Feng Nan, Haoping Bai, Shuang Ma, Shen Ma, Mengyu Li, Guoli Yin, Zirui Wang, and Ruoming Pang. ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities. In Luis Chiruzzo, Alan Ritter, and Lu Wang, editors, *Findings of the Association for Computational Linguistics: NAACL 2025*, pages 1160–1183, Albuquerque, New Mexico, April 2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.findings-naacl.65. URL [https://aclanthology.org/2025.findings-naacl.65/](https://aclanthology.org/2025.findings-naacl.65/).

[^19]: Mike A. Merrill, Alexander G. Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich, Lin Shi, Jeong Yeon Shin, Thomas Walshe, E. Kelly Buchanan, Junhong Shen, Guanghao Ye, Haowei Lin, Jason Poulos, Maoyu Wang, Marianna Nezhurina, Jenia Jitsev, Di Lu, Orfeas Menis Mastromichalakis, Zhiwei Xu, Zizhao Chen, Yue Liu, Robert Zhang, Leon Liangyu Chen, Anurag Kashyap, Jan-Lucas Uslu, Jeffrey Li, Jianbo Wu, Minghao Yan, Song Bian, Vedang Sharma, Ke Sun, Steven Dillmann, Akshay Anand, Andrew Lanpouthakoun, Bardia Koopah, Changran Hu, Etash Guha, Gabriel H. S. Dreiman, Jiacheng Zhu, Karl Krauth, Li Zhong, Niklas Muennighoff, Robert Amanfu, Shangyin Tan, Shreyas Pimpalgaonkar, Tushar Aggarwal, Xiangning Lin, Xin Lan, Xuandong Zhao, Yiqing Liang, Yuanli Wang, Zilong Wang, Changzhi Zhou, David Heineman, Hange Liu, Harsh Trivedi, John Yang, Junhong Lin, Manish Shetty, Michael Yang, Nabil Omi, Negin Raoof, Shanda Li, Terry Yue Zhuo, Wuwei Lin, Yiwei Dai, Yuxin Wang, Wenhao Chai, Shang Zhou, Dariush Wahdany, Ziyu She, Jiaming Hu, Zhikang Dong, Yuxuan Zhu, Sasha Cui, Ahson Saiyed, Arinbjörn Kolbeinsson, Jesse Hu, Christopher Michael Rytting, Ryan Marten, Yixin Wang, Alex Dimakis, Andy Konwinski, and Ludwig Schmidt. Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces, 2026. URL [https://arxiv.org/abs/2601.11868](https://arxiv.org/abs/2601.11868). arXiv preprint arXiv:2601.11868.

[^20]: Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. GAIA: a benchmark for general AI assistants. In *International Conference on Learning Representations*, pages 9025–9049, 2024. URL [https://openreview.net/forum?id=fibxvahvs3](https://openreview.net/forum?id=fibxvahvs3).

[^21]: Youngeun Nam, Joeun Kim, Hwanjun Song, Susik Yoon, Jae-Gil Lee, and Byung Suk Lee. TimelyRAG: Semantic-temporal hybrid retrieval for time-critical question answering in overlapping-evolving documents, 2026. URL [https://arxiv.org/abs/2609.11572](https://arxiv.org/abs/2609.11572). arXiv preprint arXiv:2609.11572.

[^22]: OpenAI. GPT-6 Astra: A new generation of intelligence. OpenAI, September 2026. URL [https://openai.com/index/gpt-6-astra/](https://openai.com/index/gpt-6-astra/).

[^23]: Jie Ouyang, Tingyue Pan, Mingyue Cheng, Ruiran Yan, Yucong Luo, Jiaying Lin, and Qi Liu. HoH: A dynamic benchmark for evaluating the impact of outdated information on retrieval-augmented generation. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 6036–6063, Vienna, Austria, July 2025. Association for Computational Linguistics. doi: 10.18653/v1/2025.acl-long.301. URL [https://aclanthology.org/2025.acl-long.301/](https://aclanthology.org/2025.acl-long.301/).

[^24]: Dinesh Raghu, Shantanu Agarwal, Sachindra Joshi, and Mausam. End-to-end learning of flowchart grounded task-oriented dialogs. In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, pages 4348–4366, Online and Punta Cana, Dominican Republic, November 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021.emnlp-main.357. URL [https://aclanthology.org/2021.emnlp-main.357/](https://aclanthology.org/2021.emnlp-main.357/).

[^25]: Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, and Tatsunori Hashimoto. Identifying the risks of LM agents with an LM-emulated sandbox. In *International Conference on Learning Representations*, 2024. URL [https://arxiv.org/abs/2309.15817](https://arxiv.org/abs/2309.15817).

[^26]: Wataru Sakata, Tomohide Shibata, Ribeka Tanaka, and Sadao Kurohashi. FAQ retrieval using query-question similarity and BERT-based query-answer relevance. In *Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval*, pages 1113–1116. ACM, 2019. doi: 10.1145/3331184.3331326. URL [https://doi.org/10.1145/3331184.3331326](https://doi.org/10.1145/3331184.3331326).

[^27]: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. In *Advances in Neural Information Processing Systems*, volume 36, 2023. doi: 10.52202/075280-2997. URL [https://doi.org/10.52202/075280-2997](https://doi.org/10.52202/075280-2997).

[^28]: Daniel Shepard and Robin Salimans. AutomationBench, 2026. URL [https://arxiv.org/abs/2604.18934](https://arxiv.org/abs/2604.18934). arXiv preprint arXiv:2604.18934.

[^29]: Quan Shi, Alexandra Zytek, Pedram Razavi, Karthik Narasimhan, and Victor Barres. $\tau$ -Knowledge: Evaluating conversational agents over unstructured knowledge, 2026. URL [https://arxiv.org/abs/2603.04370](https://arxiv.org/abs/2603.04370). arXiv preprint arXiv:2603.04370.

[^30]: Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. In *Advances in Neural Information Processing Systems*, volume 36, 2023. doi: 10.52202/075280-0377. URL [https://doi.org/10.52202/075280-0377](https://doi.org/10.52202/075280-0377).

[^31]: Yongqi Tong, Xiaoyun Feng, Lyuxin Xue, Jianshe Li, Xin Zhang, and Jiang-Ming Yang. How to train a real-world silicon concierge? internalizing complex business workflow to only OneModel. In *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 6: Industry Track)*, pages 1303–1316, San Diego, California, USA, July 2026. Association for Computational Linguistics. doi: 10.18653/v1/2026.acl-industry.91. URL [https://aclanthology.org/2026.acl-industry.91/](https://aclanthology.org/2026.acl-industry.91/).

[^32]: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models, 2023. URL [https://arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291). arXiv preprint arXiv:2305.16291.

[^33]: Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun Cheng, Dongchan Shin, Fangyu Lei, Yitao Liu, Yiheng Xu, Shuyan Zhou, Silvio Savarese, Caiming Xiong, Victor Zhong, and Tao Yu. OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments. In *Advances in Neural Information Processing Systems*, volume 37, pages 52040–52094. Curran Associates, Inc., 2024. doi: 10.52202/079017-1650. URL [https://doi.org/10.52202/079017-1650](https://doi.org/10.52202/079017-1650).

[^34]: Frank (Fangzheng) Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Wang, Xuhui Zhou, Zhitong Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin, Zhe Su, Leander Maben, Raj Mehta, Wayne Chi, Lawrence Jang, Yiqing Xie, Shuyan Zhou, and Graham Neubig. TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. In *Advances in Neural Information Processing Systems*, volume 38. Curran Associates, Inc., 2025. doi: 10.52202/085713-0315. URL [https://doi.org/10.52202/085713-0315](https://doi.org/10.52202/085713-0315).

[^35]: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu. Qwen3 technical report, 2025. URL [https://arxiv.org/abs/2505.09388](https://arxiv.org/abs/2505.09388).

[^36]: Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. WebShop: Towards scalable real-world web interaction with grounded language agents. In *Advances in Neural Information Processing Systems*, volume 35, pages 20744–20757. Curran Associates, Inc., 2022. doi: 10.52202/068431-1508. URL [https://doi.org/10.52202/068431-1508](https://doi.org/10.52202/068431-1508).

[^37]: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of Thoughts: Deliberate problem solving with large language models. In *Advances in Neural Information Processing Systems*, volume 36, 2023a. doi: 10.52202/075280-0517. URL [https://doi.org/10.52202/075280-0517](https://doi.org/10.52202/075280-0517).

[^38]: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: Synergizing reasoning and acting in language models. In *International Conference on Learning Representations*, 2023b. URL [https://openreview.net/forum?id=WE\_vluYUL-X](https://openreview.net/forum?id=WE_vluYUL-X).

[^39]: Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. $\tau$ -bench: A benchmark for tool-agent-user interaction in real-world domains. In *International Conference on Learning Representations*, pages 9965–10017, 2025. URL [https://openreview.net/forum?id=roNSXZpUDN](https://openreview.net/forum?id=roNSXZpUDN).

[^40]: Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang. Language agent tree search unifies reasoning, acting, and planning in language models. In *Proceedings of the 41st International Conference on Machine Learning*, volume 235 of *Proceedings of Machine Learning Research*, pages 62138–62160. PMLR, 2024a. URL [https://proceedings.mlr.press/v235/zhou24r.html](https://proceedings.mlr.press/v235/zhou24r.html).

[^41]: Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig. WebArena: A realistic web environment for building autonomous agents. In *International Conference on Learning Representations*, pages 15585–15606, 2024b. URL [https://openreview.net/forum?id=oKn9c6ytLx](https://openreview.net/forum?id=oKn9c6ytLx).