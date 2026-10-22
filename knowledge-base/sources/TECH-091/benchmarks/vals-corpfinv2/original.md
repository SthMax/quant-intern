## Dataset and Context

In both the finance and legal industries, it is a common task to ask a specific question or understand a piece of information from a very long document. A common document type is a credit agreement - contracts, often over 200 pages, used when large corporations receive a line of credit from a banking entity (see this [example credit agreement filed with the SEC](https://www.sec.gov/Archives/edgar/data/1357204/000119312511160440/dex1020.htm)).

For this dataset, we worked with a team of experts, including financial analysts, legal professionals, and academics, to create a set of questions and answers about these credit agreements. The dataset is divided into:

- **Public Validation**: 20 questions from 1 document, accessible to anyone on request (email [contact@vals.ai](mailto:contact@vals.ai) for access).
- **Private Validation**: 340 questions from 17 documents, available for purchase to evaluate and improve your own models.
- **Test**: 858 questions from 43 documents. This is the privately held set for Vals AI benchmarking and is never shared.

The dataset is also organized into three distinct tasks, which all use the entire set of questions, but pass a different subset of information into each model’s context window. The three tasks are:

1. **Exact Pages**: This variation provides only the necessary pages required to answer each question, typically resulting in a small context of only a few pages.
2. **Shared Max Context**: This variation takes a subset of pages (~80) that is guaranteed to fit in the context window of all models, and also contain the answer. The subselection doesn’t necessarily start at the first page, which can make document structure comprehension challenging for models.
3. **Max Fitting Context**: This variation includes the largest possible chunk of the document, starting from the first page, that fits within the model’s context window. This means longer-context models have more information than models with shorter context windows.

The types of questions written by the experts include:

- **Basic extraction of terms and numbers:** Some examples include “Who is the borrower’s legal counsel?” or “What currencies are the USD 325mm RCF first lien available in?”
- **Summarization and interpretation questions:** Some examples include, “Is there an erroneous payment provision?” and “How will the loan proceeds be used?”
- **Numeric reasoning or calculation-based questions:** Some examples include “How much initial debt capacity is available to the Borrower on day one?”
- **Questions involving referring to multiple sections of the provided text, especially to previous definitions:** For instance, one example is “What is the minimum required amount of Available Liquidity that the company must maintain?” The model must refer to a previous definition of Available Liquidity.
- **Giving opinions of terms based on market standards:** For instance, “Are there any unusual terms used to define or adjust EBITDA?” These questions require the models to make a judgment call, rather than just make a statement of fact.
- **Questions making use of industry jargon:** There are several terms like “baskets”, which have a commonly understood meaning in the industry, but are almost never explicitly used in the agreement itself. An example is “Does the contract contain a Chewy Blocker?” (a type of clause meant to prevent a subsidiary from being released from its debt obligations).

---

## Results

Although the larger and more powerful flagship models generally perform the best, the gap between the smaller models is not as big as in other benchmarks. When the latency and price are taken into account, it means that sometimes the smaller models provide a better accuracy for a given cost.

---

## Model Output Examples

The questions that require synthesizing content and calculating values across multiple sections in the document are some of the hardest. The fact that the text is parsed from PDFs also poses difficulty for the models: they need to handle special characters, tables, etc.

Below is an example of a number retrieval question, on the **Max Fitting Context** task. This question can be difficult for models because in a long financial document, there can be several similar tables that relate to the question, but only one contains the correct information.

In this case, the expected answer is 3.25 to 1.00.

Question

### What is the Total Net Leverage Ratio limit for unlimited RPs and investments?

3.25 to 1.00

CORRECT

---

## Additional Notes

### Context Window

Our testing across different context lengths reveals that the context window is an extremely significant factor in the model’s performance. You can find the context window for a given model on the provider’s website.

### Evaluation Methodology

All evaluations were conducted using Claude 4.5 Sonnet as the judge, with temperature set to 0.

### Retrieval-Augmented Generation (RAG)

As an alternative to including the entire document in the context window, RAG techniques are extremely common. This method breaks up long documents and databases into “chunks” which are first retrieved, and then passed to the model as context. We do not test RAG systems in this benchmark.