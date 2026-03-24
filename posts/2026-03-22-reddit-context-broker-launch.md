Title: Context Broker — standalone three-tier context assembly for LLM agents (docker compose up)

Body:

I've been building AI agent ecosystems for the past 8 months and one of the core components is a context broker — a service that manages the infinite conversation record and assembles purpose-built context windows for agents.

Today I'm releasing it as a standalone tool. docker compose up on any machine with Docker, point it at whatever inference provider you use (OpenAI, Ollama, Gemini, anything OpenAI-compatible), and you have:

- Conversation storage with deduplication
- Three-tier progressive compression (archival summary → chunk summaries → recent verbatim)
- Knowledge graph extraction via Mem0/Neo4j
- Hybrid search (vector ANN + BM25 + API-based reranking)
- MCP tools for programmatic access from any agentic framework
- OpenAI-compatible chat endpoint for conversational access

The context assembly strategy is configurable via build types — you can define how the context window is composed for different use cases (passthrough, standard-tiered, knowledge-enriched, or custom).

Built on LangGraph, PostgreSQL + pgvector, Neo4j, Redis. All backing services are OTS images. Only the application container is custom.

https://github.com/jmorrissette-RMDC/context-broker

Would be interested in feedback from anyone working on context engineering for agents.
