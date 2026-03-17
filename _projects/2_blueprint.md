---
layout: page
title: Blueprint — Multi-Agent Workbench
description: A browser-based workbench for directing multiple AI CLI agents simultaneously, with shared tooling and ecosystem independence
img: assets/img/blueprint-architecture.jpg
importance: 2
category: main
---

## What Blueprint Is

Blueprint is a multi-agent CLI workbench — a new category of tool that sits adjacent to the IDE but is distinct from it. Where the IDE is built for one developer working with one codebase, Blueprint is an environment for a human directing a team of AI agents simultaneously.

The architect watches what each agent is doing, decides what to do next, and intervenes when needed. The agents execute; the human directs.

## Design

**CLI Agents** — full interactive terminals connected to dedicated execution environments (Claude Code, Gemini CLI) running in isolated containers with SSH and PTY access. Each agent runs in its own persistent session that survives browser close and reconnect. CLI agents inherit the deep agentic investment of their respective Tier 1 providers — Blueprint coordinates them rather than replacing them.

**Chat Agents** — lightweight ReAct interfaces backed by any OpenAI-compatible endpoint. For models and endpoints without a CLI tool — smaller models, locally hosted models, experimental endpoints.

**Agent Teams** — named workspaces of 1-4 agents with shared task lists, team notes, and a common working directory. Persistent across sessions.

**Shared Tool Layer** — all agents in a team share an MCP server providing: inter-agent messaging, shared task list, shared notes, core document injection at team start, and a lightweight Advisory Quorum (parallel generation from Claude + Gemini + OpenAI, Lead synthesis, one review round).

## Ecosystem Independence

Blueprint is designed to work when nothing else does. When the system being built is broken, the workbench must still run. All backing services are self-contained. External API calls go directly to model providers. The memory integration is optional and degrades gracefully.

## Status

Blueprint is in active development. The core workbench functionality is operational; ongoing work focuses on stability and feature completion.
