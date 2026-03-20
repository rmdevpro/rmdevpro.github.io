Title: Using Knowledge Graphs as mid-chain correction in CoT reasoning — has anyone implemented this?

Body:

I've been building multi-agent ecosystems for the past 8 months and use knowledge graphs extensively for context engineering. While working through a problem with another engineer, I started thinking about a use case I haven't seen implemented in practice.

The idea: insert a KG query between each step of a chain-of-thought reasoning loop. Not as input to the chain (which is what most KG+LLM work does), but as a corrective/guiding mechanism. Before the model commits to its next reasoning step, the system checks the graph for relevant operational history. If the proposed step matches a pattern that previously led to a bad outcome, the system intervenes — essentially saying "this approach failed last time in this context, reconsider."

The flip side works too — injecting known-good patterns midstream when the graph recognizes a context where a specific approach has succeeded before.

I looked around for implementations and found academic work like CoT-RAG and Graph Chain-of-Thought, but those focus on structuring reasoning input — giving the model better context to reason with. What I'm describing is correcting reasoning output between steps based on observed operational history. Different problem.

The training signal question is interesting too. For technical domains it's obvious — logs, test results, system failures. For documented practice, the constraints are already written — policies, architecture docs, legal requirements. But for conversational or subjective domains, you'd probably need a secondary LLM observing the interaction and deciding if there's a lesson worth encoding into the graph.

Has anyone built something like this? Or is there a reason this doesn't work as cleanly as I'm imagining?

Wrote it up in more detail here if anyone's interested: https://open.substack.com/pub/jmorrissettermdc/p/knowledge-graphs-as-real-time-correction
