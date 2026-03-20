# Knowledge Graphs vs LoRAs: Teaching LLMs Without Retraining

I was speaking with a fellow engineer who was thinking about how to apply LoRAs to the image models available in Google Cloud. He was having trouble getting the results he needed — the image content wasn't cooperating with the fine-tuning approach. It's a familiar problem. LoRAs are powerful in theory, but in practice they come with significant training overhead and the difficulty of finding the right weights. I've largely moved away from them in favor of knowledge graphs.

## The Problem with LoRAs

LoRAs work by adjusting model weights to encode learned preferences. The issue is that this requires a training cycle — you need data, you need compute, you need to iterate on weights, and the results are baked into the model. When your preferences change, or when you encounter a new case the LoRA didn't train for, you're back to square one.

For real-time teaching — where the system needs to learn good and bad behaviors as they happen — this cycle is too slow.

## Why Knowledge Graphs

A knowledge graph takes a standard vector database (which uses semantic proximity — "Block of Text A is near Block of Text B because the math says they're similar") and moves it into a higher-dimensional space where you define actual relationships.

Instead of proximity, you're encoding a specific matrix: "John likes coffee" or "Blue chairs complement green rooms." This is a fundamentally different kind of memory. The system doesn't just know that two things are related — it knows *how* they're related.

The practical advantage is enormous. You point a model at an image or message, have it extract the useful logic, and encode those good/bad choices directly into the graph. The model now has a persistent memory of preferences for all future prompts — without ever touching the base weights.

The best part is that it's instant. You are teaching the system good and bad behaviors in real time.

## Bridging to Image Work

While I'm focusing purely on text right now, the approach bridges naturally to image work. Instead of trying to cram a massive Base64 string into the graph — which would just bloat the database — you store the image's URI or a feature embedding as a node. Then you let a vision-language model define the edges based on specific outcomes.

For example, the graph could encode:

- `[Image A] --(incompatible_with)--> [Modern House Aesthetic]`
- `[Image B] --(failed_execution)--> [Software Procedure XYZ]`

It turns images into logic-bound entities in the matrix, allowing the system to "remember" why a specific image failed a procedural requirement without ever needing to touch the base model weights.

## The Practical Workflow

I asked Gemini about the practical mechanics of this setup and the response was worth sharing. Here is how you actually bridge the gap between the graph and the prompt:

### Context Injection

Instead of just saying "Generate a picture of a cat," you query your knowledge graph first.

1. **Retrieval** — look up the "Cat" node
2. **Traversal** — the graph shows linked nodes: `[:LIKES]->(Cardboard_Box)`, `[:COLOR]->(Ginger)`, `[:STYLE]->(Cyberpunk)`
3. **Assembly** — programmatically stitch these into the prompt: "A ginger cat sitting inside a cardboard box in a cyberpunk setting"

### Solving the Hallucination Problem

LLMs often guess at relationships. A knowledge graph provides ground truth.

- **Without KG:** "A photo of the CEO of TechCorp." The LLM might guess a random face.
- **With KG:** You pull the specific face embedding or description stored in your graph. The prompt becomes: "A photo of [Specific Name], who has [Specific Features from KG], wearing a [Brand from KG] suit."

### Spatial Prompting via Scene Graphs

Image generators often struggle with "who is doing what to whom." By extracting a scene graph from your database, you can use positional keywords:

- **Graph data:** `(Sun)-[:BEHIND]->(Mountain)`, `(Cabin)-[:AT_FOOT_OF]->(Mountain)`
- **Prompt result:** "A landscape where the sun is partially hidden behind a jagged mountain, with a small wooden cabin nestled at the very base of the slope"

This is far more precise than "a cabin and a mountain at sunset."

### Style Consistency via Persistent Memory

If you maintain a "Visual DNA" in your memory layer, you can enforce style consistency across all prompts automatically:

- **Memory:** "User prefers high-contrast, noir lighting and 35mm film grain"
- **Augmentation:** Every image prompt automatically appends: "...shot on 35mm film, noir lighting, high contrast"

No manual repetition. The system remembers.

### Automated Multi-Modal Prompting

If you have an image and want to generate a similar one with a twist:

1. Search the graph for the nearest neighbor vector
2. Pull the textual tags attached to that vector node
3. Use those tags as the base for your new prompt

## The Technical Bridge

The glue is typically a graph retriever — something like LangChain's or LlamaIndex's graph integration. It converts a Cypher query result into a natural language string that is prepended to the user's input. The model never knows the difference. It just receives a richer, more grounded prompt.

The shift from LoRAs to knowledge graphs is really a shift from "retrain the model to know this" to "give the model the right context so it doesn't need to know this." One is expensive and slow. The other is instant and grows with use.

---

*This is a standalone post, not part of the [Conversationally Cognizant AI concept paper series](https://jmorrissette-rmdc.github.io/projects/concept-papers.html). The concept papers are released daily — see the [release schedule](https://jmorrissette-rmdc.github.io/projects/concept-papers.html) for the full list.*
