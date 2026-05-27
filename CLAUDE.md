# rmdevpro.github.io — site for blueprintagentic.ai

This repo is the GitHub Pages source for **https://blueprintagentic.ai/** (CNAME → this repo). It is the single source of truth for the BlueprintAgentic.ai marketing site. There is no upstream working repo and no separate deploy step.

## Layout

```
index.html              home page
css/                    stylesheet
assets/                 images, logos
case-studies/           per-engagement detail pages
open-source/            workbench + agent platform + pluggable agents
CNAME                   blueprintagentic.ai
.work/                  local-only planning material (gitignored)
```

## Deploy pattern

Edit files in place, commit, push. GitHub Pages picks it up on the next build (~30–60s).

```
# verify after push:
until curl -sS https://blueprintagentic.ai/ | grep -q "<sentinel>"; do sleep 5; done
```

## Voice rules (load-bearing — read before editing copy)

The site is a **consulting practice brochure**, not an ecommerce catalog.

1. **List types of work as descriptors, not packaged offers.** "Fractional CIO/CTO", "AI strategy", "organizational transformation" — the way a law firm lists "M&A · Litigation · Tax". No SKUs, prices, durations, deliverables, or SLAs.
2. **No "how we work" / methodology copy.** No "we draft before we build", no "every engagement starts with X", no process-as-pitch language.
3. **Founder bio lives only in the Leadership section.** Don't restate bio facts (years of experience, patents, exits, MIT cert, fundraising history) inside service descriptions, card copy, or the hero sub. Service descriptions describe the work, not who is behind it.
4. **Don't introduce tools or sectors without verification.** Avoid tools that don't fit the agentic framing (e.g. Gemini lacks a native agentic desktop; Zapier/Make are flow automation, not agentic). Avoid vague sector lists that include industries with no actual experience.

## Interaction style

- Conversation only — never use `ExitPlanMode` or `AskUserQuestion`. All clarification happens through plain text.
- When you intend to rearrange, **rearrange — don't rewrite**. If a rewrite is needed to express an idea, propose it first.

## Work tracking

All forward work is tracked as GitHub issues on this repo. Planning docs and session transcripts do **not** live in the tree; they go in issue comments (historical) or `.work/` (in-flight local notes).
