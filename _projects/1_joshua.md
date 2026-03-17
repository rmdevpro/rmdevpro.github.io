---
layout: page
title: Joshua26 Ecosystem
description: A distributed agentic AI ecosystem testing the hypothesis that StateGraphs are the right level of abstraction for autonomous agent cognition
img: assets/img/joshua-stamp.jpg
importance: 1
category: main
---

## The Research Hypothesis

> Agents can autonomously build and maintain a system structured as a collection of LangGraph StateGraphs, because the graph structure is the right level of abstraction for agent cognition.

Joshua26 is a working production system designed to test this hypothesis. It runs across three bare-metal Linux hosts connected by a Docker Swarm overlay network, with NFS shared storage and per-host local workspaces.

## Architecture

The fundamental building block is the **MAD** (Multipurpose Agentic Duo) — an autonomous actor that simultaneously serves its domain capabilities as an MCP server and consumes other agents as an intelligent client, with the same domain expertise governing both roles.

Two instantiations:

**pMAD (Persistent MAD)** — a system-domain agent with an infrastructure body. Always running. Governs a specific technical domain. Contains an Imperator — a resident LLM-backed agent that handles complex, multi-step, goal-directed operations within its domain. Examples: Hopper (engineering), Rogers (context), Sutherland (inference), Starret (version control).

**eMAD (Ephemeral MAD)** — a subject-domain agent with no infrastructure body. Exists only during execution of its StateGraph. Shares collective memory across all instances of its role. Installed as a Python package into a hosting pMAD at runtime via Alexandria (the internal PyPI proxy). Example: Hopper as an eMAD hosted by Kaiser.

## State 2 Architecture

The current target architecture for all pMADs:

```
[mad]               # nginx:alpine — sole network boundary (ingress AND egress)
[mad]-langgraph     # Python — LangGraph StateGraph + Imperator
[mad]-[technology]  # Official images — postgres, redis, etc. (if needed)
```

All programmatic logic lives in the LangGraph StateGraph. The Nginx gateway is pure configuration — no custom code. This makes the system readable and modifiable by agents: when an agent opens a pMAD codebase, all intelligence is in the graph.

## State 3 — Dynamic Intelligence Loading

Kaiser (the eMAD hosting pMAD) implements State 3: the infrastructure shell is stable and rarely rebuilt; intelligence travels as versioned Python packages installed at runtime from Alexandria. Zero-downtime eMAD deployment. The same eMAD library runs concurrently across multiple Kaiser instances.

## Deployed Services

| Service | Role | State |
|---------|------|-------|
| Rogers | Context Broker — conversation memory, knowledge graph, engineered context assembly | State 2 |
| Sutherland | Inference service — GPUStack cluster, local LLMs, alias routing | State 2 |
| Hopper | Engineering eMAD — autonomous SDLC (requirements → deployed software) | State 3 |
| Kaiser | eMAD host — dynamic intelligence loading via Alexandria | State 3 |
| Starret | Version control — git safety net, commit/push workflows | State 2 |
| Alexandria | Supply chain — PyPI, NPM, Docker registry caching proxies | State 2 |
| Henson | Human interaction hub — persona-driven agents, chat interfaces | State 2 |
| Apgar | Observability — ecosystem metrics, automated diagnostics | State 2 |
| Blueprint | Multi-agent workbench — parallel CLI agents, Advisory Quorum | State 2 |

## Source

The Joshua26 codebase and full documentation are available on GitHub. The concept papers describe the intellectual framework behind the architecture and are published as an ongoing research series on the [Blog](/blog/).
