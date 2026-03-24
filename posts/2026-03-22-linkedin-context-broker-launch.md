Your LLM agents forget everything between invocations. What if they didn't have to?

Today I'm releasing the Context Broker — a standalone context engineering service that manages the infinite conversation and assembles purpose-built context windows so your agents arrive at every reasoning step with the right memory.

What it does:
- Stores every conversation message with deduplication
- Three-tier progressive compression (archival summaries, chunk summaries, recent verbatim)
- Knowledge graph extraction via Mem0 and Neo4j
- Hybrid search (vector + BM25 + reranking)
- MCP tools for any agentic framework
- OpenAI-compatible chat endpoint — plug in any chat UI

What it requires:
- Docker
- An OpenAI-compatible inference provider (OpenAI, Ollama, Gemini, anything)
- docker compose up

That's it. No ecosystem. No Swarm. No special infrastructure. Same tool I use in production, now standalone.

https://github.com/jmorrissette-RMDC/context-broker

This is the first of several tools from the Conversationally Cognizant AI framework being released as standalone deployable components.
