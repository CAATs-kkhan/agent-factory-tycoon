# Game_Agentfactory

### ▶ [**Play online now**](https://caats-kkhan.github.io/agent-factory-tycoon/) — no install, runs in your browser

[![Play](https://img.shields.io/badge/▶%20Play-Agent%20Factory%20Tycoon-6D28D9?style=for-the-badge)](https://caats-kkhan.github.io/agent-factory-tycoon/)

Game design documents for **Agent Factory Tycoon** — a cozy, mobile-first educational game that teaches Agentic AI, Digital FTEs, and Spec-Driven Development through play. Based on the AgentFactory live book (Panaversity): <https://agentfactory.panaversity.org/docs>

## The Idea (one line)

You run a tiny startup and grow it by building, training, and deploying **Digital FTEs** (AI workers) from four parts — **Brain, Hands, Training, Shift** — then watch them run your business 24/7. Twenty-six short levels mirror AgentFactory's 26 real crash courses.

## Files in This Folder

| File | What it is |
|------|-----------|
| `Agent_Factory_Tycoon_Concept.docx` | The complete game design document (submission-ready, with Table of Contents). |
| `Agent_Factory_Tycoon_Concept.pdf` | PDF version for easy viewing/sharing (no Word needed). |
| `Agent_Factory_Tycoon_Concept.md` | The Markdown source for the document. Edit this, then regenerate the `.docx`. |
| `index.html` | **Playable Level 1 prototype.** Double-click to run in any browser — no install needed. |
| `README.md` | This file. |

## Play the Prototype

Double-click **`index.html`** (or open it in any browser). It's a self-contained, offline playable slice of Level 1's core loop:

**Level 1 — Your First Hire:** **Build** the worker (tap the 4 glowing parts) → **Spec** (fill the job card; try a silly spec for the gag) → **GO** (watch it work) → **Verify** (Approve or Improve) → **Reward** (coins, XP, Night Shift unlock).

**Level 2 — The Magic Words:** **tune a prompt** (Tone / Clarity / Expertise) by tapping chips and watch the reply quality climb from Poor → Okay → Great in a live preview, then send it to delight an angry customer and unlock the Prompt Tuner.

**Level 3 — Markdown Builder:** tap markdown blocks (heading, list, image) and watch them render into a live webpage; publish it to unlock the Page Builder.

**Level 4 — Code You Never Write:** describe a button (color + label), tap Generate, watch your agent "write" the code, then tap the real working button that appears. Unlocks the Auto-Builder.

**Level 5 — Plug It In:** pick the correct connectors (tools) a task needs — Calendar + Email — and run it to unlock Connector Slots.

**Level 6 — Think Like a Boss:** pick the best *intent* (a goal/outcome, not a task) for a slow-sales situation; completes the Foundations and unlocks World 2.

**Level 7 — Code Companion:** tap the buggy line of code; your coding agent fixes it and the tests go green. Unlocks Coder Bot.

**Level 8 — The Knowledge Worker:** deploy a Cowork bot to draft a follow-up email — tap the professional points (skip the bad ones) and watch the draft build live. Unlocks Cowork Desk.

**Level 9 — The Perfect Spec:** a spec-mastery round — fill a flawless Refund Bot spec. Unlocks Mode Select.

**Level 10 — The Problem Solver:** send in a general agent — tap the steps in the right order to solve a login problem. Unlocks Solver Bot.

**Levels 11–26 — the full campaign:** all remaining courses are playable through a data-driven level engine using four mechanic types (pick-one, multi-select, order-the-steps, build-a-preview):

| # | Level | Teaches |
|---|-------|---------|
| 11 | The Claw | OpenClaw automation |
| 12 | Snake Charmer | Python in the AI era |
| 13 | The Searchable Brain | RAG on pgvector |
| 14 | Build-A-Bot | building agents |
| 15 | From Worker to Employee | Agent → Digital FTE |
| 16 | The Nervous System | production events |
| 17 | Mission Control | workforce (Paperclip) |
| 18 | Hiring on Demand | dynamic workforce |
| 19 | The Delegate | owner delegate |
| 20 | Quality Inspector | eval-driven development |
| 21 | To the Cloud | cloud deployment |
| 22 | The Architect | choosing architectures |
| 23 | Show Me the Money | payment-enabled agents |
| 24 | The Recruiter | choosing AI employees |
| 25 | Cheat Codes | cheatsheets |
| 26 | Master Engineer | agentic engineering (capstone) |

Nova guides every step. Coins and XP carry across all **26 levels** (L1 → … → L26 → loops back). No Unity, no build step, no internet required.

**Level Select:** the start screen has a **📋 Level Select** button — tap it to jump straight to any of the 26 levels.

**Saved progress:** coins, XP, and completed levels are saved automatically in your browser (localStorage), so they persist between sessions. The Level Select grid shows a ✓ on completed levels and a running total; a **⟲ Reset** button there clears your progress.

## What's Inside the Document

- **Executive Summary** — the one-page pitch.
- **Part 1** — Concept Paper (idea, audience, gameplay loop, mechanics, MVP, why it works).
- **Part 2** — Level 1 Walkthrough (all 7 scenes in prose).
- **Part 3** — Full 26-Level Map (each level mapped to its real AgentFactory course).
- **Part 4** — Design Specification (Fun / Easy / Interactive / Graphics, grounded in named frameworks).
- **Parts 5-8** — Full Level 1 storyboards (Scenes 2-7: Worker Builder, Spec Card, Press GO, Verify, Rewards, Bridge).
- **Part 9** — Character Bio: Nova, the guide mascot.
- **Part 10** — 2-Week MVP Build Plan (developer-facing).
- **Sources** — AgentFactory documentation links.

## Key Concepts at a Glance

- **Digital FTE** = an AI worker with a Brain (model), Hands (MCP/tools), Training (skills), and Shift (24/7 autonomy).
- **Spec-Driven Development** = clear specs produce great results; taught via the "silly spec" gag.
- **10-80-10 rule** = humans set intent (10%), agents execute (80%), humans verify (10%).
- **Nova** = the player's friendly guide mascot (a glowing violet-and-teal orb).

## Regenerating the .docx from the Markdown

This document is built with [Pandoc](https://pandoc.org/). After editing the `.md`, run:

```
pandoc "Agent_Factory_Tycoon_Concept.md" -o "Agent_Factory_Tycoon_Concept.docx" --toc --toc-depth=2
```

(Run from inside this folder. The `--toc` flag rebuilds the Table of Contents.)

## Regenerating the PDF from the .docx

The PDF is produced from the `.docx` using Microsoft Word (which preserves formatting and the Table of Contents). After regenerating the `.docx`, refresh the PDF by running this PowerShell command from inside this folder:

```powershell
$src = (Resolve-Path "Agent_Factory_Tycoon_Concept.docx").Path
$pdf = Join-Path (Get-Location) "Agent_Factory_Tycoon_Concept.pdf"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($src, $false, $true)
    $doc.SaveAs([ref]$pdf, [ref]17)   # 17 = wdFormatPDF
    $doc.Close($false)
} finally {
    $word.Quit()
}
```

(Requires Microsoft Word installed. The `17` is Word's PDF export format code.)

## Status

Design blueprint complete. Recommended next step: build the **Level 1 MVP** (see Part 10) to validate the core assemble -> spec -> verify loop before scaling to all 26 levels.
