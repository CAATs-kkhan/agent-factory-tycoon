% Agent Factory Tycoon — Game Concept Document
% Based on AgentFactory (Panaversity) — agentfactory.panaversity.org
% Prepared: 20 June 2026

---

# Agent Factory Tycoon

## *Build, Train & Run Your Own AI Workforce — One Digital Worker at a Time*

**An educational game concept that teaches Agentic AI, Digital FTEs, and Spec-Driven Development through play.**

Based on the AgentFactory live book — <https://agentfactory.panaversity.org/docs>

---

# Executive Summary

**Agent Factory Tycoon** is a cozy, mobile-first build-and-manage game that teaches real Agentic AI skills through play. The player runs a tiny startup and grows it by **building, training, and deploying Digital FTEs** — AI workers assembled from four parts (**Brain, Hands, Training, Shift**) — then watches them run the business 24/7. Without ever reading a manual, players absorb the core ideas of the AgentFactory curriculum: the Digital FTE, Spec-Driven Development, and the 10-80-10 human-in-the-loop rhythm.

**The problem it solves.** Agentic AI is one of the most valuable skills of the decade, but the on-ramp is intimidating — walls of theory, jargon, and setup. Agent Factory Tycoon removes that wall, turning the first hour of learning into something genuinely fun.

**How it plays.** A tight 60–90 second loop: a customer appears → you build a Digital FTE by dragging four parts together → you write its job on a fill-in-the-blank "Spec Card" → you press GO and watch it work → you verify the result → you earn coins, XP, and unlocks. Twenty-six short levels mirror AgentFactory's 26 real crash courses, so the game doubles as an on-ramp to the actual curriculum.

**Why it works.** The design is grounded in proven frameworks, not guesswork:

- **Fun** — Lazzaro's 4 Keys to Fun, Flow theory, and heavy "game feel" juice.
- **Easy** — one new concept per level, "show don't tell" onboarding, no punishing fail states.
- **Interactive** — direct-manipulation drag/drop, meaningful build choices, a living reactive world.
- **Beautiful** — a stylized 2.5D low-poly art direction (Unity + URP) that ships at 60fps on mid-range phones and in-browser.

**The hook.** A friendly mascot named **Nova** guides every step, and the signature "silly spec" gag teaches the hardest lesson — clear specifications — through laughter instead of lectures. Approved workers keep earning coins even while the player is offline, embodying the Digital FTE promise and driving retention.

**Target audience.** Total beginners, students, and professionals who want to understand Digital FTEs in 30 minutes of play.

**Status & ask.** This document is a complete game-design blueprint: concept, full 26-level map, four-pillar design spec, end-to-end Level 1 storyboards, and a character bio. The recommended next step is a small **MVP** proving the assemble → spec → verify loop; if Level 1 hits >90% completion and testers smile at the core loop, the concept is validated and ready to scale.

---

# Part 1 — Concept Paper

## 1. What Is a Concept Paper?

A concept paper is a short design blueprint that defines a game **before** building it: its idea, who it's for, what the player learns, how it plays, how it looks, and why people will love it. It is the "pitch + plan" that aligns everyone before a single line of code is written. This document is that blueprint.

## 2. The Core Idea (One Sentence)

> You run a tiny startup. To grow, you **build, train, and deploy Digital FTEs** (AI workers) by snapping together their **Brain, Hands, Training, and Shift** — and watch them run your business 24/7.

It is a **cozy build-and-manage game** (think *Stardew Valley* meets *Two Point Hospital*) where, without realizing it, the player learns real Agentic AI concepts.

## 3. Target Audience

| Player | Why they'll play |
|--------|------------------|
| Total beginners | Learn AI agents through play, zero jargon |
| Students | Fun on-ramp before the real crash courses |
| Professionals | Understand Digital FTEs in 30 minutes |

**Difficulty: deliberately easy.** Drag, drop, tap. No reading walls, no harsh fail-states — only "your agent could do better, try again."

## 4. Learning Objectives (Hidden Inside the Fun)

Each game mechanic secretly maps to a real AgentFactory concept:

| In the game you... | You're really learning... |
|--------------------|---------------------------|
| Assemble a worker from 4 parts | The Digital FTE anatomy: Brain, Hands, Training, Shift |
| Write a "job order" card | Spec-Driven Development (clear specs = good results) |
| Pick which model powers a worker | Choosing an engine (Claude / GPT / Gemini) |
| Plug in tool-chips | MCP & tools ("Hands") |
| Give a worker a skill-book | Agent Skills ("Training") |
| Set intent, watch, approve | The 10-80-10 rule |
| Manage a growing team | The Seven Invariants of an AI-native company |

## 5. Core Gameplay Loop (Easy & Addictive)

```
   1. A CUSTOMER appears with a request
   2. BUILD a Digital FTE (drag 4 parts)
   3. WRITE the job spec (fill-in-the-blank)
   4. PRESS GO -> agent works (cute animation)
   5. VERIFY the result -> approve / improve
   6. EARN coins + XP -> unlock new parts
   ... repeat, scale up ...
```

A full loop takes **60–90 seconds** — perfect for quick, satisfying sessions.

## 6. Game Mechanics That Make It Fun & Interactive

- **Drag-and-Drop Worker Builder** — Snap together glowing puzzle pieces: a **Brain** orb, **Hand** tools, a **Training** book, and a **Shift** clock. Pieces "click" with a satisfying sound and sparkle.
- **The Spec Card** — A fill-in-the-blank card: *"I want a worker that ___ when ___."* Vague answers make the agent do something silly (funny!); clear answers make it nail the task. Players *feel* why specs matter.
- **Live "Work" Animation** — After hitting GO, your little agent bustles around — typing, sorting mail, answering chats — with progress bars and emoji reactions.
- **Verify Mini-Game** — A quick "thumbs up / fix it" choice teaches that humans verify, agents execute.
- **Factory Builder / Idle Layer** — Approved workers keep earning coins even when you are offline (idle-game retention hook).
- **Progression & Unlocks** — 26 short levels mirror the 26 crash courses. Each unlock is a new part, tool, or worker type.

## 7. Visual & Audio Design (Good Graphics)

- **Art style:** clean, cheerful 3D isometric or polished 2.5D cartoon — bright, rounded, friendly (Two Point / Mini Metro charm). Reads great on mobile.
- **Characters:** adorable robot/agent mascots with expressive faces and idle animations.
- **UI:** large tap targets, minimal text, icon-first, soft shadows, smooth transitions.
- **Color:** energetic gradients (purple/teal "tech" palette) tied to AgentFactory branding.
- **Audio:** satisfying click/ding feedback, upbeat low-fi background music, celebratory chimes on success.
- **Juice:** screen-shake on big wins, confetti on level-up, particle sparkles on assembly.

## 8. Extra Functionalities (Powerful & Interactive)

- Leaderboards & daily challenges ("Build the best Support FTE today")
- Nova, the tutorial mascot — a friendly guide who helps for the first 3 levels, then steps back
- Themed campaigns — Sales city, Healthcare hospital, Legal tower
- Co-op / share — share your factory layout, compare agents with friends
- Accessibility — colorblind mode, one-hand play, adjustable text size
- "Real concept" cards — 1-tap link connecting each mechanic to the actual AgentFactory course
- Gentle notifications — "Your night-shift FTE earned 200 coins!"

## 9. Suggested Tech Stack

- **Engine:** Unity (best 2.5D/3D + mobile + web export) or Godot (free, lightweight)
- **Web build:** WebGL so it runs in-browser, matching AgentFactory's no-install labs
- **Platforms:** Web first, then iOS/Android
- **Backend (optional):** lightweight save/leaderboard service

## 10. MVP Scope (What to Build First)

1. One customer type + one worker to build
2. The 4-part drag-and-drop builder
3. The Spec Card mechanic
4. The work animation + verify step
5. Coins, XP, and 5 levels

If players smile at the **assembly + spec + verify** loop, the concept works — then scale up.

## 11. Why This Works

- **Easy:** drag, drop, tap — no manuals.
- **Fun:** cute agents, idle earnings, unlocks, leaderboards.
- **Good graphics:** bright, polished, mobile-friendly isometric world.
- **Interactive & powerful:** every tap teaches a real Agentic AI concept usable later in AgentFactory's actual courses.
- **Builds intuition** so the real 15-hour Digital FTE track feels familiar, not scary.

---

# Part 2 — Level 1 Walkthrough: "Your First Hire"

**Goal:** Build and deploy your very first Digital FTE — a Support Bot.
**Duration:** ~3 minutes · **Difficulty:** Tutorial (impossible to lose)

## Scene 0 — Opening (Cinematic, 8 seconds)

**Visual:** Camera pans over a tiny, empty startup office — one desk, a flickering "OPEN" sign, dust motes in sunlight. Upbeat low-fi music starts.

**Nova** — your friendly guide mascot — pops in. Nova is a small, hovering orb of light that glows in the game's signature violet-and-teal, with two big expressive eyes and a wisp of a "spark tail." She is upbeat, a little cheeky, and endlessly encouraging — half mentor, half hype-friend. (Nova appears throughout the game as the player's companion and tutor, celebrating wins, cracking gentle jokes, and nudging with just-in-time hints — never lecturing.)

> "Welcome, boss! This is YOUR company. Problem is... you're the only one here, and the customers are already lining up. Let's hire some help — the AI kind. Tap anywhere to begin!"

**Player action:** Tap screen.

**Concept taught:** A company's value comes from its *workforce*, not just its tools. (Thesis: Digital FTEs are the unit of business value.)

## Scene 1 — A Customer Arrives

**Customer (Mia):** "Hi! I bought a backpack but it arrived with a broken zipper. Can someone help me return it?"

**Nova:** "A customer needs help! You COULD answer this yourself... every single time... forever. Or — we build a worker who handles it 24/7. Let's build one!"

**Player action:** Tap **[ Build a Worker ]**.

**Concept taught:** The difference between *you doing the work* vs. *manufacturing a worker who does it* (Mode 1 vs. Mode 2).

## Scene 2 — The Worker Builder (Core Mechanic)

A clean assembly bench appears: a glowing empty robot silhouette with 4 empty slots, and 4 trays of puzzle pieces.

**Part 1 — The BRAIN:** Drag the purple Brain orb into the head slot (click + sparkle; eyes light up).
*Concept: Brain = the reasoning model (Claude/GPT/Gemini).*

**Part 2 — The HANDS:** Drag the Orders and Chat tool-chips into the hand slots.
*Concept: Hands = MCP + tools that let an agent act on real systems.*

**Part 3 — The TRAINING:** Drag the "Returns Policy" skill-book; the robot reads it.
*Concept: Training = Agent Skills (domain knowledge + SOPs).*

**Part 4 — The SHIFT:** Drag the 24/7 clock; the robot powers up and waves (confetti).
*Concept: Shift = autonomous 24/7 operation. "A tool waits for a prompt; a Digital FTE runs on its own."*

## Scene 3 — The Spec Card (The Clever Teaching Moment)

A "Job Order" card slides up with fill-in-the-blank slots and tappable word-tiles.

**Card:** *"My worker should [____] when [____], then [____]."*

**Trick — try the silly path first:** tapping "panic" + "eat lunch" makes the robot spin in circles and throw papers (sad trombone). Nova laughs: "See? Unclear instructions = chaos. Let's give it a REAL spec."

**Correct path:** *"My worker should **help the customer** when **a return request arrives**, then **confirm the refund**."* The card glows green.

**Concept taught:** Spec-Driven Development — "Vague requirements produce flawed results faster; clear specs produce excellent results quickly." The single most important lesson, taught through play.

## Scene 4 — Press GO (Work Animation)

**Player action:** Tap the giant **[ GO ]** button.

The Support Bot springs to life — reads Mia's message, checks the order, looks up the policy, and types a reply with a gear-filled progress bar.

**Support Bot to Mia:** "So sorry about the zipper, Mia! I've approved your return and a refund is on the way."

**Concept taught:** The agent *composes* its Brain + Hands + Training to deliver an outcome — the full Digital FTE in action.

## Scene 5 — Verify (Human-in-the-Loop)

A panel shows the Bot's reply with two buttons: **[ Approve ]** and **[ Improve ]**.

**Nova:** "One golden rule, boss: the agent does the work, but YOU verify the outcome. Does this answer look good?"

**Player action:** Tap **Approve.** Mia sends a heart and a 5-star rating; coins rain down.

**Concept taught:** The 10-80-10 rule — "Humans define intent. Agents execute. Humans verify outcomes."

## Scene 6 — Rewards & The Idle Hook

Reward banner: **+50 Coins**, **+100 XP (Level 1 Complete!)**, **Unlocked: Night Shift** (your bot earns coins while you are away).

**Nova:** "Amazing! Your first Digital FTE is officially on the job — even after you log off. Ready to grow your factory?"

**Concept taught:** Autonomous workers create value continuously (the idle-earning loop and retention hook).

## Scene 7 — Optional "Learn the Real Thing" Card

A dismissible card: "What you just did has a real name: building a **Digital FTE**. Want the real-world version? See AgentFactory Course 15: 'From Agent to Digital FTE.'"

**Concept taught:** Bridges the game to the actual AgentFactory crash courses — turning fun into a real learning funnel.

## Level 1 Concept Map (Summary)

| Scene | Player Action | Real Concept Learned |
|-------|--------------|----------------------|
| 0 | Tap to start | Workforce = business value |
| 1 | Build a worker | Mode 1 vs Mode 2 |
| 2 | Drag 4 parts | Digital FTE anatomy: Brain, Hands, Training, Shift |
| 3 | Fill the Spec Card | Spec-Driven Development |
| 4 | Press GO | Agent composes capabilities |
| 5 | Approve result | 10-80-10 rule (verify) |
| 6 | Collect rewards | Autonomous 24/7 value |
| 7 | Optional link | Bridge to real courses |

---

# Part 3 — Full 26-Level Progression Map

The 26 levels are organized into 4 game "Worlds" mirroring AgentFactory's three curriculum tiers (Foundations, General Agents, Manufacturing) plus a Production/Scale endgame.

> **Note on accuracy:** All 26 course titles below are the exact, verified titles from the AgentFactory "Getting Started" crash-course list. The game level names and mechanics are an original design that maps each course to a playable level.

## World 1 — "The Startup Garage" (Foundations · Courses 1–6)

| Lvl | Game Level Name | Mirrors Course | What You Do | Concept Learned | Unlock |
|----|-----------------|----------------|-------------|-----------------|--------|
| 1 | Your First Hire | 1. What AI Actually Is | Build your first Support Bot (4 parts) | What an AI agent is | Night Shift (idle coins) |
| 2 | The Magic Words | 2. AI Prompting in 2026 | Tune a prompt-dial for better replies | Prompting = clear instructions | Prompt Tuner |
| 3 | Markdown Builder | 3. Markdown In, HTML Out | Snap markdown blocks into a webpage | Structured input to clean output | Page Builder |
| 4 | Code You Never Write | 4. Code You Never Write | Describe what you want; agent writes it | AI as your coder | Auto-Builder bench |
| 5 | Plug It In | 5. Skills & Connectors | Connect tool-chips & skill-books | Skills & Connectors (MCP basics) | Connector slots |
| 6 | Think Like a Boss | 6. How to Think in the AI Era | Choose intent cards; agent executes | Human sets intent, AI executes | World 2 unlocked |

## World 2 — "The Open Floor" (General Agents · Courses 7–9)

| Lvl | Game Level Name | Mirrors Course | What You Do | Concept Learned | Unlock |
|----|-----------------|----------------|-------------|-----------------|--------|
| 7 | Code Companion | 7. Agentic Coding Crash Course: Claude Code and OpenCode | Pair with a coding agent to fix a bug | Agentic coding | Coder Bot |
| 8 | The Knowledge Worker | 8. Cowork Crash Course | Deploy a Cowork bot to draft docs & emails | Knowledge-work agents | Cowork desk |
| 9 | The Perfect Spec | 9. Spec-Driven Development | Master the Spec Card (specify-clarify-plan-build) | Spec-Driven Development | MODE CHOICE |

**Mode Fork after Level 9:** the player picks a playstyle (replayable to do both): Mode 1 ("use AI to do your work" side-levels) or Mode 2 (the Manufacturing campaign, Worlds 3–4, the main game).

## World 3 — "The Factory Floor" (Manufacturing · Courses 10–20)

| Lvl | Game Level Name | Mirrors Course | What You Do | Concept Learned | Unlock |
|----|-----------------|----------------|-------------|-----------------|--------|
| 10 | The Problem Solver | 10. Problem Solving with General Agents | Send a general agent to crack a tricky customer problem | Problem-solving with general agents (Seven Principles) | Solver Bot |
| 11 | The Claw | 11. OpenClaw with General Agents | Use OpenClaw to let an agent grab & control on-screen tasks | OpenClaw automation | OpenClaw arm |
| 12 | Snake Charmer | 12. Python in the AI Era | Drop a Python engine into a worker to crunch data | Python in the AI era | Python core |
| 13 | The Searchable Brain | 13. Give Your AI Searchable Context: RAG on Postgres with pgvector | Build a searchable knowledge vault the agent queries | RAG (searchable context) with pgvector | RAG vault |
| 14 | Build-A-Bot | 14. Build AI Agents Crash Course | Assemble a full custom agent | Building agents end-to-end | Custom Agent kit |
| 15 | From Worker to Employee | 15. From Agent to Digital FTE | Upgrade an agent into a 24/7 Digital FTE | The Digital FTE | FTE badge |
| 16 | The Nervous System | 16. From Digital FTE to Production Worker with a Nervous System | Wire workers to an event nervous system (Inngest) | Production worker; events, durability, flow | Event bus |
| 17 | Mission Control | 17. Building a Workforce with Paperclip | Hire/assign/govern via the Paperclip panel | Workforce management layer | Paperclip console |
| 18 | Hiring on Demand | 18. From Fixed to Dynamic Workforce | Auto-spawn workers when demand spikes | Runtime hiring under policy | Auto-hire |
| 19 | The Delegate | 19. From Founder Bottleneck to Owner Delegate | Give yourself a personal delegate agent | Each human gets a delegate | Delegate avatar |
| 20 | Quality Inspector | 20. Eval-Driven Development for AI Employees | Run agents through a testing gauntlet | Eval-Driven Development | Eval lab |

## World 4 — "The Empire" (Production & Scale · Courses 21–26)

| Lvl | Game Level Name | Mirrors Course | What You Do | Concept Learned | Unlock |
|----|-----------------|----------------|-------------|-----------------|--------|
| 21 | To the Cloud | 21. Deploy Your Agent Harness to the Cloud | Ship your factory to the cloud (Docker/K8s/Dapr/Ray) | Cloud-native deployment | Cloud city |
| 22 | The Architect | 22. Choosing Agentic Architectures | Pick the right blueprint/architecture for each worker | Choosing agentic architectures | Architecture board |
| 23 | Show Me the Money | 23. Payment-Enabled Agents: ACP, AP2, x402, and MPP | Let agents handle real payments safely | Payment-enabled agents | Payments rail |
| 24 | The Recruiter | 24. Which AI Employees Should You Use in 2026? | Pick the best AI employee for each role | Selecting AI employees | Roster screen |
| 25 | Cheat Codes | 25. Cheatsheets | Unlock quick-reference power-up cards | Cheatsheets / quick reference | Cheatsheet deck |
| 26 | Master Engineer | 26. Agentic Engineering Fundamentals | Run a full autonomous company with all principles | Capstone: Agentic Engineering Fundamentals | Endgame + Prestige |

## Progression Design Notes

- **Difficulty curve:** Worlds 1–2 are tutorial-easy (can't lose). World 3 adds light strategy (managing multiple workers). World 4 adds optimization/endgame depth.
- **Pacing:** Levels 1–9 ~3 min each. Levels 10–26 grow to 5–8 min with the factory-management layer.
- **Replay value:** the Mode 1 / Mode 2 fork plus Prestige at Level 26 (restart with bonuses) keep players returning.
- **Learning funnel:** every milestone level gently links to the matching real AgentFactory course, turning the game into an on-ramp for the actual curriculum.

---

# Part 4 — Design Specification: Fun, Easy, Interactive, Beautiful

This section is not adjectives — it is a buildable spec. Each of the four pillars is grounded in an established, named design framework and turned into concrete decisions a developer can implement on day one.

## Pillar 1 — FUN (grounded in Lazzaro's "4 Keys to Fun" + Flow + Game Feel)

Nicole Lazzaro's research identifies four distinct sources of fun. A game that only hits one feels thin; *Agent Factory Tycoon* deliberately delivers all four.

| Key to Fun | What it is | How the game delivers it |
|------------|-----------|--------------------------|
| Easy Fun | Curiosity, novelty, play | New worker types, tools, and worlds drip-fed every level; free-explore sandbox mode |
| Hard Fun | Challenge, mastery, "fiero" (triumph) | Daily challenges, eval-scoring (Lvl 20), Prestige loop, optimizing a factory for max output |
| Serious Fun | Play with real-world meaning | Every mechanic teaches a real AgentFactory concept the player can actually use |
| People Fun | Social, sharing, competition | Leaderboards, shareable factory layouts, "beat my Support FTE" challenges |

### Flow: difficulty must track skill (Csikszentmihalyi)

Fun collapses when a game is too hard (anxiety) or too easy (boredom). We hold the player in the **flow channel** with:

- **Dynamic Difficulty Adjustment (DDA):** if a player retries a level 3+ times, Nova offers a hint and the next customer request gets simpler. If they breeze through, optional "expert orders" appear for bonus coins.
- **A clean ramp:** Worlds 1–2 are unloseable tutorials; challenge is introduced only after the core loop is automatic.

### Game Feel ("juice"): the single biggest multiplier on perceived fun

Every player action gets disproportionate, satisfying audiovisual feedback. This is the **mandatory juice checklist** for the MVP:

- Snap-to-slot with a spring overshoot (DOTween ease-out-back) + "click" SFX + a 6-particle sparkle burst
- Button presses scale to 0.92 then bounce back; coins fly to the counter on an arc and the counter rolls up
- Confetti + screen-flash on level-up; gentle screen-shake (max 4px) on big wins only
- The agent mascot has idle micro-animations (blink, breathe, look around) so the screen is never "dead"
- The "silly spec" gag (Level 1) — failure is *funny*, never punishing — is the emotional signature of the game

## Pillar 2 — EASY (grounded in Cognitive Load Theory, "Show-Don't-Tell," Fitts's Law, Krug)

### One new mechanic per level (Cognitive Load Theory)

The 26-level map already enforces this: each level introduces exactly **one** new concept. We never stack two new mechanics in the same level. This is the core reason the game stays easy as it deepens.

### Teach by doing, not by reading ("Show, Don't Tell")

Modeled on Nintendo's level-design philosophy (e.g., the wordless teaching of World 1-1 in Super Mario Bros.):

- **No text tutorials.** Nova speaks one sentence, then the *only* tappable thing on screen is the action we want to teach. The player learns by succeeding.
- **Just-in-time hints:** guidance appears at the moment of need, then disappears. Nothing is front-loaded.
- **Diegetic teaching:** the "silly spec" outcome teaches the spec lesson through consequence, not a tooltip.

### Forgiveness (remove anxiety)

- **No hard fail states, no timers in Worlds 1–2, no lost progress.** The worst outcome is "your agent could do better — tweak and retry."
- Auto-save after every loop; the player can never lose a worker they built.

### Reachability (Fitts's Law + Krug's "Don't Make Me Think")

- **Mobile-first thumb zones:** all primary controls sit in the bottom 40% of the screen; the GO button is the largest target on screen.
- **Minimum 48x48dp tap targets**, generous spacing, no precision dragging required (slots have magnetic snap).
- **Self-evident UI:** icons + one-word labels; if an element needs a paragraph to explain, it is redesigned.

### Accessibility (built in, not bolted on)

- Colorblind-safe palette (never color-only signaling — pair color with icon/shape)
- Adjustable text size; high-contrast mode
- One-handed portrait play; full captions for all spoken Nova lines
- Reduced-motion toggle (disables screen-shake/heavy particles)

## Pillar 3 — INTERACTIVE (grounded in Direct Manipulation + Player Agency)

### Direct manipulation, not menus

Players *touch the world*, not abstract menus. Every core verb is a physical gesture:

| Player intent | Gesture | Immediate response |
|---------------|---------|--------------------|
| Build a worker | Drag part to slot | Magnetic snap + sparkle + part animates on |
| Give a job | Tap word-tiles onto a card | Card fills, glows green when valid |
| Run the worker | Tap GO | Live work animation plays out |
| Judge the result | Tap Approve / Improve | NPC reacts (rating, emoji), economy updates |
| Grow the factory | Drag-place desks/rooms | Building snaps to grid, workers move in |

### Meaningful choices = agency

- **The Mode Fork (Level 9):** a genuine branch (Mode 1 vs Mode 2) that changes the next stretch of play and is replayable.
- **Build choices matter:** which Brain/tools/skills you pick changes how well the worker performs on a given order — there's a "right-ish" build to discover, not one forced answer.

### A living, reactive world

- NPC customers queue, tap their feet, and react in real time to good/bad service.
- Deployed workers visibly bustle around the factory floor between orders (the idle layer is *visible*, not just a number).

## Pillar 4 — GOOD GRAPHICS (a concrete, achievable, mobile-friendly art direction)

These are definitive choices, not options — chosen for charm, readability, and the ability to ship on web + mobile at 60fps.

### Chosen style: stylized **2.5D low-poly isometric**, rendered in 3D

Justification: low-poly reads beautifully at any resolution, is cheap to render on phones, animates with personality, and has mature ready-made asset libraries — so a small team can hit "good graphics" without a large art budget. Reference charm: *Two Point Hospital*, *Mini Motorways*, *Monument Valley*.

### Definitive color palette (tied to the AgentFactory brand)

| Role | Hex | Use |
|------|-----|-----|
| Primary Violet | #6D28D9 | Brand, headers, the "Brain" orb |
| Teal Accent | #14B8A6 | Interactive highlights, the "Hands" tools |
| Coin Gold | #FBBF24 | Rewards, currency, celebration |
| Success Green | #22C55E | Valid specs, approvals |
| Playful Red | #EF4444 | The funny "wrong" feedback (never harsh) |
| Cream Base | #FFF7ED | Backgrounds, calm canvas |
| Ink | #1E293B | Text, outlines |

Rule: warm tones (gold/green) signal reward; cool tones (violet/teal) signal interactivity; red is reserved for *playful* error only.

### Production pipeline (real, off-the-shelf)

- **Engine:** Unity 6 LTS with the Universal Render Pipeline (URP) — best balance of mobile performance + WebGL export to match AgentFactory's no-install labs.
- **Art assets:** Synty POLYGON / Kenney.nl low-poly packs as a base kit (fast, cohesive, low-cost), customized to brand.
- **Animation juice:** DOTween for UI/tween motion; skeletal mascot animation following Disney's 12 principles — lean on squash-and-stretch, anticipation, and follow-through for life.
- **Lighting & post:** baked global illumination + a soft directional key light; post-processing stack of gentle Bloom, slight Vignette, and Color Grading for a warm, polished look.
- **UI:** soft-shadow, rounded "claymorphic" components; TextMeshPro for crisp text at every resolution.

### Performance targets (so "good graphics" actually ships)

- 60fps on a mid-range 3–4-year-old Android phone
- Initial WebGL load under ~30 MB; assets streamed thereafter
- Aggressive static/dynamic batching and texture atlasing to keep draw calls low
- Reduced-motion and "lite graphics" toggles for low-end devices

## How We'll Know It Works (validation, not vibes)

| Pillar | Measured by | Target |
|--------|-------------|--------|
| Easy | Tutorial (Level 1) completion rate | > 90% finish without quitting |
| Fun | Day-1 retention / sessions per day | Players return same day; multiple short sessions |
| Interactive | Avg. actions per minute in the build loop | High touch frequency, low idle-confusion time |
| Graphics | Frame rate on target device + qualitative "delight" playtests | Stable 60fps; testers smile at the juice |
| Learning | Can a player, after World 1, correctly name the 4 FTE parts? | > 80% recall in a quick post-play quiz |

If Level 1 hits >90% completion and testers smile at the assemble-spec-verify loop, the concept is validated — then scale to all 26 levels.

---

# Part 5 — Storyboard: Scene 2, The Worker Builder

**Screen:** Portrait mobile · **Goal:** drag 4 parts into the worker · **Feel:** tactile, magnetic, celebratory

This is the core mechanic screen, drawn as a 6-frame sequence. Each frame lists the visual, the juice/animation, the audio, Nova's single line, and the concept it teaches.

## Persistent Screen Layout (the "stage")

```
+------------------------------------+
| < Back        LEVEL 1      o . . . | header: 4-dot part-progress tracker
+------------------------------------+
|            A S S E M B L Y          |
|                                     |
|              +-------+              |
|              : ? ?   :   <- BRAIN   | upper area =
|              +-------+      slot    | the worker
|           +-----------+             | (slots glow
|      (?)--|   B O D Y  |--(?)       | dashed when
|       ^   :  +-----+   :   ^        | empty)
|     HANDS : : ? ? :    :  HANDS     |
|           : +-----+    :            |
|           +---[ ? ? ]--+ <- TRAINING|
|              /        \             |
|             [  ? ?  ] <- SHIFT      |
|                                     |
+- - - - - - Nova hint - - - - - - - +
|  (o) "Drag the Brain into your      |
|       worker to give it a mind!"    |
+============ THUMB ZONE =============+
|   +----+  +----+  +----+  +----+    | draggable
|   | Br |  | Hn |  | Tr |  | Sh |    | part trays
|   +----+  +----+  +----+  +----+    | (bottom 40%,
|   Brain   Hands  Train.  Shift     | thumb-reachable)
+------------------------------------+
```

## Frame 1 — The Bench Opens

```
Header:  o . . .   (0 of 4 parts placed)
Worker:  empty silhouette, all 4 slots pulsing with a soft dashed glow
Nova:   "Every worker needs 4 parts. Let's start with the Brain!"
Trays:   [Brain] tray gently bounces up/down to invite the first drag;
         the other 3 trays are dimmed (greyed ~40%)
```

- **Juice:** the empty worker does a slow "breathe" scale (1.0 to 1.02). Only the Brain tray is lit, so attention has exactly one target.
- **Audio:** soft ambient hum plus a single gentle chime as the screen settles.
- **Concept:** there is a *structure* to an AI worker — four parts, introduced one at a time (one-new-thing rule).
- **Accessibility:** the active tray also shows an arrow plus label, not color alone.

## Frame 2 — Dragging the Brain (finger down)

```
              +-------+
              : (o)(o):  <- BRAIN slot now glows BRIGHT
              +-------+      (it is the live drop target)
                  ^
                [Brain] <- orb lifts off the tray, enlarges 1.15x,
                           trails sparkles, and follows the finger
Nova: "Drop it on the head!"
```

- **Juice:** on pick-up the orb pops (scale 1.0 to 1.15, ease-out-back) and casts a soft drop-shadow so it feels lifted. A faint dotted line connects orb to target slot. The matching slot brightens; non-matching slots stay dim, so the player cannot feel lost.
- **Audio:** a rising "whoop" pitch while held (tracks height) — playful, like lifting a magnet.
- **Concept:** the **Brain = the reasoning model** (Claude/GPT/Gemini). Head placement makes "thinking" literal.

## Frame 3 — SNAP! Brain Locks In

```
Header:  o o . .   (1 of 4)
              +-------+
              : (o_o) :  <- eyes blink ON; the worker now has a face
              +-------+
              *   *   *   <- 6-particle sparkle burst
Nova: "Nice! A mind online. Now give it Hands."
Trays:   [Brain] consumed/checked · [Hands] now lights up and bounces
```

- **Juice (the signature moment):** magnetic snap with a spring overshoot (DOTween ease-out-back), 6 sparkle particles, a tiny 3px screen-pulse, and the worker's eyes blink open — instantly giving it personality. The progress dot fills with a satisfying tick.
- **Audio:** a crisp "click-ding" — the core reward sound the whole game is built around.
- **Concept:** placement leads to immediate, visible consequence. The worker visibly became smarter.

## Frame 4 — Hands Attach

```
Header:  o o o .   (2 of 4)
           +-----------+
   [Ord][Ch]|   B O D Y  |[Ch][Ord]  <- tool-arms unfold
           :  (o_o)     :              (Orders + Chat)
           +-----------+
Nova: "Hands let it DO things — touch real systems."
```

- **Interaction:** the Hands tray holds multiple tool-chips (Orders, Chat). The player drags the two the job needs — a first taste of meaningful build choice. Each snaps with the same click-ding plus sparkle.
- **Juice:** little articulated arms unfold with squash-and-stretch and a mechanical "whirr."
- **Concept:** **Hands = MCP + tools** that let the agent act on real systems.

## Frame 5 — Training Book Absorbed

```
Header:  o o o .   (3 of 4, last dot about to fill)
           :  +-----+  :
           :  : Book :  :  <- book flips pages, then dissolves
           :  +-----+  :     into the worker (knowledge "learned")
Nova: "Training = what it KNOWS. Here's your Returns Policy."
```

- **Juice:** the skill-book opens, pages riffle (a quick flip animation), then it glows and dissolves *into* the worker — a visual metaphor for learning. The worker gives a small approving nod.
- **Audio:** a soft page-riffle plus a warm "absorb" shimmer.
- **Concept:** **Training = Agent Skills** (domain knowledge plus SOPs).

## Frame 6 — The Shift Clock: Worker Complete

```
Header:  o o o o   (4 of 4 — full!)
              [ 24/7 clock ] <- snaps to the base, hands spin once
              (o_o) party    <- worker powers up fully, waves
            *  * CONFETTI *  *
Nova: "Your first Digital FTE is ALIVE! Now give it a job."
                       [  CONTINUE  >  ]  <- appears, pulsing
```

- **Juice:** the final snap triggers a full celebration — confetti rain, a one-time gentle screen-shake (<=4px), the worker stands up, eyes go happy, and it gives a little wave. All four progress dots do a victory shimmer.
- **Audio:** a triumphant rising "power-up" arpeggio — the triumph/"fiero" beat (Hard Fun payoff).
- **Transition:** a single glowing **CONTINUE** button slides into the thumb zone — the only tappable element — leading into Scene 3 (the Spec Card).
- **Concept:** **Shift = autonomous 24/7 operation.** The worker is now a complete Digital FTE: Brain + Hands + Training + Shift.

## Designer Notes for This Screen

- **One target at a time:** only the next valid slot/tray is ever lit; everything else dims. This is how the screen stays easy despite four steps — the player is never hunting.
- **Magnetic, forgiving drops:** slots have a wide snap radius; near-misses still lock in. No precision required (Fitts's Law).
- **Wrong-part feedback is gentle:** dragging the Shift clock onto the head makes it bounce off with a soft "boing" and a smiling shake — no penalty.
- **Every snap = the same reward chord** (click-ding plus sparkle plus dot fill). Consistency builds the satisfying rhythm.
- **The face is the hook:** the worker gains eyes at the Brain step and emotion by the end — players bond with a character, not a form.
- **Reduced-motion mode:** confetti/shake replaced by a soft glow pulse; all timings and SFX preserved.

---

# Part 6 — Storyboard: Scene 3, The Spec Card (with Nova)

**Screen:** Portrait mobile · **Goal:** fill a fill-in-the-blank job order with word-tiles · **Teaches:** Spec-Driven Development · **Signature beat:** the "silly spec" gag

Same format as the Scene 2 storyboard: a 6-frame sequence, each beat noting visual, juice, audio, Nova's line, and the concept.

## Persistent Screen Layout (the "stage")

```
+------------------------------------+
| < Back      LEVEL 1     SPEC CARD   |
+------------------------------------+
|   Your worker stands ready, looking |
|   at you, waiting for orders        |
|              (o_o)?                  |
|                                     |
|   == JOB ORDER ==================   |
|   |  My worker should           |   |
|   |     +-------------+         |   | <- blank #1
|   |     |   _______   |         |   |
|   |     +-------------+         |   |
|   |  when                       |   |
|   |     +-------------+         |   | <- blank #2
|   |     |   _______   |         |   |
|   |     +-------------+         |   |
|   |  then                       |   |
|   |     +-------------+         |   | <- blank #3
|   |     |   _______   |         |   |
|   |     +-------------+         |   |
|   ==============================    |
+- - - - - - Nova hint - - - - - - - +
|  (o) "Tell your worker its JOB.     |
|       Tap a word to drop it in!"    |
+=========== WORD BANK ==============+
|  [help the customer] [a return     |
|   request arrives] [confirm the    | <- tappable
|   refund]  [panic]  [eat lunch]    |    word-tiles
|  [ignore everyone]                 |
+------------------------------------+
```

## Frame 1 — The Card Slides Up

```
Worker:  stands center-stage, tilts head, a "?" bubble floats above
Card:    JOB ORDER slides up from the bottom with a paper "whoosh";
         all 3 blanks pulse with a soft dashed glow
Nova:    "Tell your worker its JOB. Tap a word to drop it in!"
Bank:    6 word-tiles fan out like cards being dealt
```

- **Juice:** the card has a subtle paper texture and a gentle float/bob. Word-tiles deal in with a riffle (staggered 40ms each). Blank #1 glows brightest — the suggested starting point.
- **Audio:** paper "whoosh" plus a soft card-deal riffle.
- **Concept:** a worker needs *explicit instructions* — you are about to write its spec.
- **Accessibility:** blanks are numbered 1-2-3 and labeled, not just color-glowing.

## Frame 2 — Tapping a Word-Tile

```
Bank:   player taps [panic] ->
        tile lifts 1.1x, glows, and arcs up toward blank #1
        +-------------+
        |   panic >   |  <- flies into the slot
        +-------------+
Nova:   "Hmm... bold choice."
```

- **Interaction:** tap-to-fill (one-tap, no precise dragging — easy). The tile flies on an arc into the next open blank and snaps with a soft click. Tap a filled blank to pop the word back out and try again.
- **Juice:** arc tween (ease-out-back), tile snaps with a 4-particle puff. Nova's eyes follow the tile.
- **Audio:** light "pop-click" as it lands.
- **Concept:** specs are built piece by piece — and you can revise freely (no penalty for experimenting).

## Frame 3 — The "Silly Spec" (the signature gag)

```
Card filled (nonsense):
   My worker should  [ panic ]
   when              [ eat lunch ]
   then              [ ignore everyone ]
   -> card flashes amber, a [ TRY IT > ] button appears
Player taps TRY IT...

Worker reaction:
        (x_x)  <- eyes go spiral
       \(o_o)/   spins in circles, papers fly everywhere,
        _|_|_     trips over its own tool-arms
   *sad trombone: womp-womp-wommmp*
Nova (laughing): "HA! See? Fuzzy orders = total chaos.
                  Let's give it a REAL spec."
```

- **Juice:** full slapstick — the worker spins, juggles papers, a tiny rain-cloud appears over its head. Exaggerated squash-and-stretch. This is failure made delightful — never punishing.
- **Audio:** the famous sad-trombone "womp-womp," comedic boings, scattered paper rustle.
- **No penalty:** no coins lost, no life lost. The card simply shakes its head and resets the blanks, tiles flying back to the bank.
- **Concept (the core lesson, taught by consequence):** *vague/wrong specs produce chaos faster.* The player feels why clarity matters instead of being told — this is the heart of Spec-Driven Development.

## Frame 4 — Nova Coaches the Retry

```
Card:   blanks empty again, gently pulsing
Nova:   "A good spec answers: DO what? WHEN? then WHAT?
         The right words are glowing — give it a go!"
Bank:   the three CORRECT tiles now have a faint helpful shimmer
        [help the customer] [a return request arrives]
        [confirm the refund]   <- these subtly glow
```

- **Just-in-time help (DDA):** only on a *failed* attempt does Nova nudge by softly highlighting the sensible tiles. A first-try-correct player never sees the hint — preserving challenge for the capable.
- **Juice:** the helpful tiles do a slow breathing glow; the silly tiles fade slightly back.
- **Concept:** a clear spec has a shape — **action then trigger then outcome.**

## Frame 5 — The Perfect Spec

```
Card filled (clear):
   My worker should  [ help the customer ]
   when              [ a return request arrives ]
   then              [ confirm the refund ]
   -> every blank locks GREEN, card emits a warm glow
        =============================
        |  (check)  SPEC LOCKED IN!  |  <- green seal stamps on
        =============================
Worker:  nods confidently (o_o)v — "got it, boss!"
Nova:    "Crystal clear! THAT'S a spec a worker can nail."
```

- **Juice:** as the last correct tile lands, the whole card sweeps green left-to-right, a "SPEC LOCKED IN" wax-seal stamps down with a satisfying thump, and the worker straightens up and salutes. Coins shimmer in anticipation.
- **Audio:** a bright ascending "success" chord plus a stamp "ka-chunk."
- **Concept:** **clear specifications produce excellent results** — the validated, well-formed spec (action/trigger/outcome).

## Frame 6 — Hand-off to "GO"

```
Card:   slides up and "attaches" to the worker (it now carries its job)
A single glowing button slides into the thumb zone:
        +--------------------------+
        |    >   SEND IT TO WORK   |  <- only tappable element
        +--------------------------+
Nova:   "Spec's ready. Hit GO and watch your worker shine!"
```

- **Transition:** the locked card folds into the worker's "Training" area, visually linking spec to worker. The lone **SEND IT TO WORK** button leads into Scene 4 (Press GO / the work animation).
- **Audio:** a soft "ready" chime; button pulses invitingly.
- **Concept:** the spec now *drives* the worker — intent set, ready to execute (the start of the 10-80-10 loop).

## Designer Notes for This Screen

- **Tap, don't drag:** one-tap-to-fill keeps it effortless on mobile; tap a filled blank to undo. Zero precision required.
- **Failure is the best teacher here:** the silly-spec gag is the emotional and educational centerpiece — make the slapstick generous and the reset instant and friendly.
- **Hints are earned, not forced:** correct-tile glow appears only after a wrong attempt (Dynamic Difficulty) — capable players keep the challenge.
- **Shape over vocabulary:** the card visibly teaches the action-trigger-outcome pattern, which transfers directly to real Spec-Driven Development.
- **Consistent reward chord:** the green "lock-in" reuses the game's signature success sound, tying it to every other win.
- **Reduced-motion mode:** the slapstick spin becomes a gentle wobble plus cloud icon; sad-trombone and all SFX preserved.

---

# Part 7 — Storyboards: Scene 4 (Press GO) and Scene 5 (Verify)

These two scenes complete the Level 1 visual sequence. Scene 4 is the "80%" of the 10-80-10 loop — the agent executes. Scene 5 is the final "10%" — the human verifies. Same format as the earlier storyboards.

## Scene 4 — Press GO and the Live Work Animation

**Screen:** Portrait mobile · **Goal:** watch the worker execute the spec · **Teaches:** an agent composes Brain + Hands + Training to deliver an outcome

### Persistent Screen Layout (the "stage")

```
+------------------------------------+
| < Back      LEVEL 1     AT WORK     |
+------------------------------------+
|   Chat with Mia                     |
|   +------------------------------+  |
|   | Mia: my backpack zipper is   |  |
|   |      broken, can I return?   |  |
|   +------------------------------+  |
|                                     |
|        (o_o)   <- worker at desk    |
|       /[==]\      typing...         |
|        _||_                         |
|                                     |
|   [#### Working ... 60% ####----]   |
|   read -> check order ->            |
|   look up policy -> write reply     |
+- - - - - - Nova hint - - - - - - - +
|  (o) "Watch your worker go. You set |
|       it up great!"                 |
+------------------------------------+
```

### Frame 1 — Press GO

```
The SEND IT TO WORK button (from Scene 3) sits in the thumb zone, pulsing.
Player taps it:
   button squashes to 0.92x, then bounces back, emits a ring of sparks
   the worker snaps upright, cracks its knuckles (tool-arms flex)
Nova:  "Here we go!"
```

- **Juice:** button press with spring-back; a quick "power-on" sweep washes across the worker; the screen subtly zooms in on the worker's desk.
- **Audio:** a satisfying "ka-chink" press plus a rising "engine start" whir.
- **Concept:** the human sets intent and presses go — the agent now takes over (start of the 80%).

### Frame 2 — The Worker Reads (Brain + Chat)

```
   Mia's message highlights with a soft scan-line sweep
   +------------------------------+
   | Mia: ...broken... return? ...|  <- words light up as "read"
   +------------------------------+
        (o_o)  <- worker's eyes flick left-to-right (reading)
   Step ticker: [ READING THE REQUEST ]
```

- **Juice:** a scan-line passes over Mia's text; the worker's eyes track it. A small thought-bubble shows a tiny brain icon pulsing.
- **Audio:** soft "blip-blip" scanning tones.
- **Concept:** the **Brain** comprehends the request via the **Chat** tool (Hands).

### Frame 3 — The Worker Acts (Hands + Training)

```
   Tool icons light up in sequence as the worker uses them:
      [ Orders ] -> spins, finds Mia's order  (CHECK)
      [ Policy ] -> book glows, rule found     (CHECK)
   Step ticker: [ CHECKING ORDER ]  ->  [ LOOKING UP POLICY ]
        (o_o)  <- worker glances at each tool as it fires
```

- **Juice:** each tool-chip lights, does a little spin, then stamps a green CHECK. A connecting line briefly links Brain to each tool — showing the parts working together.
- **Audio:** mechanical "whirr-clunk" per tool, a soft "ding" on each check.
- **Concept:** **Hands (MCP/tools)** act on real systems; **Training (Skills)** supplies the rule. The Digital FTE composes its parts.

### Frame 4 — The Worker Composes the Reply

```
   A reply bubble types itself out, word by word:
   +------------------------------+
   | "So sorry about the zipper-  |  <- text appears live
   |  ..."                        |
   +------------------------------+
   [######## Working ... 90% ########--]
        (o_o)  /[==]\  <- hands "type" on a little keyboard
```

- **Juice:** live typewriter text; the progress bar fills with rolling gear icons; tiny key-tap particles fly off the worker's hands.
- **Audio:** gentle mechanical-keyboard clicks; the progress bar emits a soft rising hum as it nears 100%.
- **Concept:** the agent synthesizes everything it gathered into a single, grounded outcome.

### Frame 5 — Reply Sent, Hand-off to Verify

```
   Progress hits 100% -> a soft "ping"
   The finished reply slides into the chat as a draft (not yet sent to Mia)
        (o_o)v  <- worker leans back, done, looks to you
   A panel begins sliding up: "Review your worker's reply"
Nova:  "Nice work by your FTE! One last step - let's check it."
```

- **Juice:** progress bar flashes full-green; the worker exhales (small relief animation) and turns to face the player, handing off control.
- **Audio:** a completion "ping" and a soft swoosh as the Verify panel rises.
- **Concept:** the agent finished the 80% — now control returns to the human for the final 10%.

## Scene 5 — Verify (Approve or Improve)

**Screen:** Portrait mobile · **Goal:** approve a good result (or send it back to improve) · **Teaches:** the 10-80-10 rule — humans verify outcomes

### Persistent Screen Layout (the "stage")

```
+------------------------------------+
| < Back      LEVEL 1     VERIFY      |
+------------------------------------+
|   Your worker drafted a reply:      |
|   +------------------------------+  |
|   | "So sorry about the zipper,  |  |
|   |  Mia! I've approved your     |  |
|   |  return and a refund is on   |  |
|   |  the way."                   |  |
|   +------------------------------+  |
|                                     |
|   Does this look good, boss?        |
+- - - - - - Nova hint - - - - - - - +
|  (o) "The agent does the work, but  |
|       YOU verify. Golden rule!"     |
+========== THUMB ZONE ==============+
|   [   IMPROVE   ]   [   APPROVE   ] |
+------------------------------------+
```

### Frame 1 — The Verify Panel Slides Up

```
   The draft reply card settles center-screen with a gentle bob.
   Two buttons rise into the thumb zone:
      [ IMPROVE ] (amber, left)     [ APPROVE ] (green, right)
        (o_o)  <- worker waits beside the card, hopeful
Nova:  "The agent did the work - now YOU verify the outcome."
```

- **Juice:** the reply card has a subtle highlight outline inviting a read; the two buttons pulse alternately so neither is missed; the worker watches with hopeful eyes.
- **Audio:** soft panel swoosh; a quiet expectant tone.
- **Concept:** verification is a deliberate, named step — not an afterthought.

### Frame 2 — Nova Frames the Golden Rule

```
Nova (one beat, then steps aside):
   "Humans set intent. Agents execute. Humans verify.
    That's the rhythm of every great AI team."
   The two buttons remain; nothing else is tappable.
```

- **Just-in-time teaching:** Nova states the 10-80-10 rule once, exactly when the player is about to do it, then gets out of the way.
- **Concept:** **10-80-10** — the core operating loop of working with Digital FTEs.

### Frame 3 — The IMPROVE Branch (optional)

```
Player taps [ IMPROVE ]:
   a quick coaching popup: "What should it do better?"
   tap a fix-chip: [ warmer tone ] [ add refund ETA ] [ shorter ]
        (o_o)? -> (o_o) -> worker re-drafts in ~2s
   the reply updates; player returns to the Approve choice
Nova:  "Good eye! Small tweaks make a big difference."
```

- **Juice:** the worker nods, quickly re-types (a fast version of the Scene 4 typing), and the card refreshes with a soft glow.
- **No penalty:** improving is rewarded, not punished — it models healthy human-in-the-loop iteration.
- **Concept:** verification can mean *steering*, not just yes/no — the human refines the outcome.

### Frame 4 — The APPROVE Branch

```
Player taps [ APPROVE ]:
   green button stamps a big CHECK; the draft "sends" to Mia (swoosh)
   +------------------------------+
   | Mia: Thank you!! <3  *****    |  <- heart + 5-star rating
   +------------------------------+
        (o_o)  ->  (o_^)  <- worker beams, takes a little bow
   Coins arc from Mia's message to the counter: +50 (cha-ching!)
Nova:  "Boom! Happy customer, happy boss. That's the loop!"
```

- **Juice:** approve-stamp thump; Mia's heart pops and 5 stars fill one by one with rising chimes; coins fly on an arc and the counter rolls up; a small confetti puff.
- **Audio:** the signature "click-ding" success chord, star-fill arpeggio, coin "cha-ching."
- **Concept:** a verified, approved outcome closes the loop — value delivered.

### Frame 5 — Hand-off to Rewards

```
   The screen begins its transition to Scene 6 (Rewards):
   a banner peeks up - "+50 Coins ... +100 XP ..."
        (o_^)  <- worker waves, heads to its desk to keep working
Nova:  "Your first Digital FTE is officially on the job. Let's tally it up!"
```

- **Transition:** smooth wipe into the reward banner (Scene 6), with the worker walking off to the factory floor to begin its autonomous shift.
- **Concept:** one full loop complete (intent -> execute -> verify -> reward); the worker now runs on its own.

## Designer Notes for These Two Screens

- **Show the parts working together (Scene 4):** lighting up Brain -> Hands -> Training in sequence is the payoff for the assembly in Scene 2 — players literally see what they built come alive.
- **Never a dead screen:** the worker always has micro-animation (reading, typing, waiting, beaming) so the execute phase feels alive, not like a loading spinner.
- **Verify is a real choice (Scene 5):** Approve and Improve are both first-class, both rewarded — this teaches that verification is active, not a rubber stamp.
- **Consistent reward grammar:** the same click-ding, coin arc, and star chimes used everywhere tie Scene 5's payoff to every other win in the game.
- **Reduced-motion mode:** typing/confetti become soft fades; all audio cues and timings preserved.

---

# Part 8 — Storyboards: Scene 6 (Rewards) and Scene 7 (Learn the Real Thing)

These two scenes close out Level 1. Scene 6 is the celebration and progression payoff (coins, XP, the Night Shift unlock). Scene 7 is the optional bridge that connects the play to the real AgentFactory curriculum. Same format as the earlier storyboards.

## Scene 6 — Rewards and the Idle Hook

**Screen:** Portrait mobile · **Goal:** celebrate the win and unlock progression · **Teaches:** autonomous workers create value continuously (the Digital FTE promise)

### Persistent Screen Layout (the "stage")

```
+------------------------------------+
| < Back      LEVEL 1   COMPLETE!     |
+------------------------------------+
|         * * * LEVEL CLEAR * * *     |
|                                     |
|      +------------------------+     |
|      |  +50  Coins            |     |
|      |  +100 XP   -> LVL 1 UP |     |
|      |  [#########----] 80%   |     |  <- XP bar filling
|      +------------------------+     |
|                                     |
|   UNLOCKED:                         |
|      +------------------------+     |
|      | (moon) NIGHT SHIFT     |     |
|      | Your FTE earns coins   |     |
|      | while you are away!    |     |
|      +------------------------+     |
|                                     |
+- - - - - - Nova hint - - - - - - - +
|  (o) "Your worker keeps earning,    |
|       even after you log off!"      |
+========== THUMB ZONE ==============+
|        [   CONTINUE   >   ]         |
+------------------------------------+
```

### Frame 1 — The Victory Banner

```
   A "LEVEL CLEAR" banner drops from the top with a bounce.
   Confetti rains; the worker (now on the factory floor) waves up at you.
        (o_^)/  <- worker celebrating
Nova:  "You did it, boss - your first Digital FTE is live!"
```

- **Juice:** banner drop with spring-bounce; confetti burst; a brief triumphant zoom on the smiling worker.
- **Audio:** the triumphant "fiero" power-up arpeggio (the big-win chord).
- **Concept:** completion and triumph (Hard Fun payoff) — the player earned this.

### Frame 2 — Coins and XP Tally

```
   Rewards count up one by one (not all at once):
      +50 Coins   -> coins arc into the counter, which rolls up
      +100 XP     -> the XP bar fills left-to-right
   [############------] 80%  ->  [################] 100%  LEVEL UP!
```

- **Juice:** sequential reveal (coins first, then XP) so each lands as its own little hit; the XP bar fills and flashes gold on LEVEL UP; numbers roll rather than snap.
- **Audio:** coin "cha-ching" cascade, a rising tick as the XP bar fills, a "level-up" sting at 100%.
- **Concept:** visible progression — clear evidence of growth keeps players motivated (drip-fed mastery).

### Frame 3 — The Night Shift Unlock

```
   A new card flips into view with a shimmer:
      +------------------------+
      | (moon)  NIGHT SHIFT    |
      | Your FTE now earns     |
      | coins 24/7 - even      |
      | while you are away.    |
      +------------------------+
   The worker's desk gains a little clock that starts ticking.
Nova:  "This is the magic of a Digital FTE - it never sleeps."
```

- **Juice:** the unlock card flips in (3D card-flip) with a shimmer sweep; the worker's desk-clock begins a gentle tick; a soft "+coins/hr" tag appears.
- **Audio:** a magical "unlock" chime plus a soft ticking clock.
- **Concept:** **autonomous 24/7 operation** — the idle-earning hook *is* the Digital FTE promise (and the retention mechanic).

### Frame 4 — Hand-off

```
   A single glowing button slides into the thumb zone:
        [   CONTINUE   >   ]
   Tapping it begins the transition toward the next beat
   (the optional "Learn the Real Thing" card, then Level 2).
Nova:  "Ready to grow your factory? Let's keep going!"
```

- **Juice:** the CONTINUE button pulses invitingly; a subtle parallax of the factory floor hints at more to come.
- **Audio:** soft "ready" chime.
- **Concept:** momentum into the next loop — the core gameplay rhythm repeats and scales.

## Scene 7 — The "Learn the Real Thing" Bridge Card

**Screen:** Portrait mobile (a small, dismissible overlay) · **Goal:** connect the fun to the real AgentFactory curriculum · **Teaches:** what the player just did has a real name and a real course

### Persistent Screen Layout (the "stage")

```
+------------------------------------+
|        (the factory floor, dimmed)  |
|                                     |
|   +------ LEARN THE REAL THING --+  |
|   |                              |  |
|   |  What you just built has a   |  |
|   |  real name: a DIGITAL FTE.   |  |
|   |                              |  |
|   |  Want the real-world version?|  |
|   |  -> AgentFactory Course 15:  |  |
|   |     "From Agent to           |  |
|   |      Digital FTE"            |  |
|   |                              |  |
|   |  [ Maybe later ] [ Show me > ]| |
|   +------------------------------+  |
|                                     |
|  (o) Nova: "Curious how this works  |
|       for real? Peek anytime."      |
+------------------------------------+
```

### Frame 1 — The Card Gently Appears

```
   The factory floor dims softly; a friendly card slides up
   from the corner (NOT a full-screen takeover - easy to ignore).
        (o_o)  <- Nova peeks in from the side
Nova:  "Psst - want to see the real thing behind this game?"
```

- **Juice:** background dims to ~60%; the card eases in from a corner with a soft shadow; Nova pokes in playfully rather than blocking the screen.
- **Audio:** a gentle, curious "ding" - inviting, never interruptive.
- **Concept:** the game is a doorway, not a wall - the bridge is optional and low-pressure.

### Frame 2 — The Connection Is Made

```
   The card names the concept and maps it to a real course:
      "You just built a DIGITAL FTE."
      "-> AgentFactory Course 15: From Agent to Digital FTE"
   A small icon row shows the 4 parts the player assembled,
   labeled with their real names: Brain, Hands, Training, Shift.
```

- **Juice:** the four part-icons from Scene 2 slide in with their real-world labels - tying the game metaphor directly to the real concept.
- **Audio:** a soft "aha" chime.
- **Concept:** **serious fun** - the play has real-world meaning and a concrete next step in the actual curriculum.

### Frame 3 — The Two Choices

```
   Two buttons, equal weight:
        [ Maybe later ]            [ Show me > ]
   - Maybe later  -> card slides away, straight to Level 2
   - Show me      -> opens the AgentFactory course link in-app
                     (a gentle web view), then returns to the game
Nova:  "No rush - it'll be here whenever you're curious."
```

- **Juice:** both buttons are friendly and equal (no dark-pattern nudging); choosing either feels good. "Show me" opens a lightweight in-app view; "Maybe later" dismisses with a soft swoosh.
- **Audio:** a light confirm tap either way.
- **Concept:** respectful, opt-in learning funnel - turns enjoyment into genuine curiosity about AgentFactory's real courses.

### Frame 4 — Return to Play

```
   Either choice lands the player at the Level 2 entrance:
        "WORLD 1 - The Startup Garage  |  Level 2: The Magic Words"
        (o_o)  <- Nova: "On to the next hire!"
```

- **Transition:** smooth return to the World 1 map / Level 2 intro, keeping momentum.
- **Concept:** the loop continues - fun first, real learning always one tap away.

## Designer Notes for These Two Screens

- **Sequence the rewards (Scene 6):** never dump all rewards at once - coins, then XP, then the unlock, each as its own little hit. This stretches the satisfaction and teaches what each reward means.
- **The unlock is the lesson (Scene 6):** Night Shift is not just a reward - it is the literal demonstration of "a Digital FTE works 24/7." Make the ticking desk-clock visible and ongoing.
- **The bridge must never nag (Scene 7):** keep it a small, dismissible corner card with two equal choices. A learning funnel that feels like an ad breaks trust; one that feels like a friendly tip builds it.
- **Tie the metaphor to the real names (Scene 7):** showing Brain/Hands/Training/Shift with their real labels is the single highest-value teaching moment - it converts a game mechanic into a transferable concept.
- **Consistent reward grammar:** the same coin "cha-ching," XP tick, and unlock chime used here match every other win in the game.
- **Reduced-motion mode:** confetti and card-flips become soft fades; all audio cues and timings preserved.

---

# Part 9 — Character Bio: Nova, Your Guide

This section fully specifies Nova so an art, animation, and writing team can build her consistently. Nova is the player's companion and tutor across every scene; her job is to make a complex subject (Agentic AI) feel warm, easy, and fun.

## At a Glance

| Field | Detail |
|-------|--------|
| Name | Nova |
| Role | Guide mascot, tutor, hype-friend |
| Species | A small, sentient orb of light (a friendly "spark of intelligence") |
| Pronouns | She / her |
| First appears | Level 1, Scene 0 |
| Core job | Teach by encouraging, never by lecturing |
| One-line essence | "Half mentor, half best friend — the spark that believes in you." |

## Visual Design

- **Form:** a floating orb roughly the size of the player's worker's head, hovering with a gentle bob.
- **Color:** glows in the brand palette — a violet core (#6D28D9) with a teal aura (#14B8A6); brightens to gold (#FBBF24) when celebrating.
- **Face:** two large, expressive eyes (no mouth needed — emotion reads through the eyes and brow). She can squint, widen, sparkle, and do a happy "upturned" smile-eyes.
- **Signature feature:** a wispy "spark tail" that trails behind her movement and flicks when she's excited.
- **Scale & framing:** she lives in the corner or beside the worker, never blocking the play area; she pokes in from the side rather than covering the screen.
- **Silhouette test:** instantly recognizable as a glowing dot with eyes and a spark tail — clean at any resolution (matches the low-poly art direction).

## Personality

- **Upbeat & encouraging:** every player action is "great," "bold," or "crystal clear." She finds the good even in a silly mistake.
- **A little cheeky:** she teases gently (the "bold choice" line on a silly spec) but never mocks.
- **Concise:** she speaks one short line at a time — she trusts the player to learn by doing.
- **Calm under chaos:** when the worker melts down, Nova laughs with the player, not at them, and reframes it as a lesson.
- **Genuinely on your side:** she frames everything as "we" and "your worker," reinforcing that the player is the boss.

## Voice & Tone Rules (for writers)

- **Short.** One sentence per beat. If it needs two, cut it to one.
- **Second person, warm.** "You set it up great!" not "The setup is complete."
- **Show, don't lecture.** Point to the next action; let consequence teach the lesson.
- **Celebrate specifics.** "Crystal clear!" beats "Good job" — name what they did well.
- **Never punish.** Failure lines are playful and forward-looking ("Let's give it a REAL spec").
- **No jargon up front.** Real terms (Digital FTE, spec, MCP) are introduced only after the player has felt the concept.
- **Earned hints.** Nova only nudges with the answer after a player struggles — capable players keep the challenge.

## Sample Catchphrases

- Greeting: "Welcome, boss!"
- Encouragement: "You set it up great!" / "Crystal clear!"
- Gentle tease (on a silly choice): "Hmm... bold choice."
- Reframing a mistake: "HA! Fuzzy orders = chaos. Let's fix it together."
- The golden rule: "Humans set intent. Agents execute. Humans verify."
- Big win: "Boom! Happy customer, happy boss."
- The Digital FTE magic: "This one never sleeps."
- Sign-off into the next level: "On to the next hire!"

## Animation Set (for the animator)

| State | What Nova does |
|-------|----------------|
| Idle | Gentle bob and slow blink; spark tail drifts |
| Talking | Slight forward lean, eyes animate, tail flicks on emphasis |
| Excited / celebrating | Spins, brightens to gold, tail sparkles, tiny confetti |
| Teasing | One eye squints, a playful little wobble |
| Thinking / hinting | Eyes drift up, a small "?" or lightbulb spark above her |
| Reassuring (after a fail) | Softens color, leans in close, warm slow blink |
| Peeking in (Scene 7) | Slides in from a screen edge, only head/eyes visible |

## Accessibility for Nova

- **Captions:** every spoken line is fully captioned; Nova never communicates critical info by voice alone.
- **Color-independent emotion:** her feelings read through eye shape and motion, not just glow color (colorblind-safe).
- **Reduced motion:** spins and tail-sparkles become soft fades; her timing and lines are preserved.
- **Skippable:** her lines can be tapped-through; she never blocks or slows an experienced player.
- **Readable text:** caption text uses the UI's adjustable size and high-contrast settings.

## Why Nova Works

Nova turns a potentially intimidating topic into a friendly conversation. By being concise, encouraging, and consequence-driven, she embodies the game's three core promises — **easy** (one short nudge at a time), **fun** (she celebrates and teases), and **interactive** (she reacts live to what the player does). She is the emotional through-line that makes every scene feel personal.

---

# Part 10 — The 2-Week MVP Build Plan

This is a developer-facing plan to build a playable vertical slice of **Level 1** in two weeks. The goal is not a finished game — it is to **prove the core loop is fun**: assemble a worker, write a spec, press GO, verify, get rewarded. If playtesters smile at that loop, the concept is validated.

## Scope: What the MVP Includes (and Excludes)

**In scope (the vertical slice):**

- One full playthrough of Level 1, Scenes 0 through 6 (Scene 7 bridge optional)
- The 4-part drag-and-drop Worker Builder (Scene 2)
- The Spec Card with the "silly spec" gag and the correct path (Scene 3)
- The live work animation (Scene 4) and Verify/Approve (Scene 5)
- Rewards: coins, XP, and the Night Shift unlock (Scene 6)
- Nova as a guide (static art + text lines; full animation later)
- Core "juice": snap feedback, sparkle, click-ding, coin arc, confetti

**Out of scope (deliberately deferred):**

- Levels 2 through 26, the world map, the Mode fork
- The idle/factory-management layer beyond a single ticking clock
- Leaderboards, sharing, accounts, monetization
- Full Nova animation set, voice-over, multiple worker types
- Cloud save (local save only)

## Team Assumption

A small team of 2 to 3: one engineer (Unity/C#), one artist (2.5D/UI), and a shared design/audio role. The plan also works for a solo developer by treating each "role-day" as sequential.

## Technical Setup (Day 0 / pre-flight)

- Unity 6 LTS project with the Universal Render Pipeline (URP)
- DOTween for tween/juice; TextMeshPro for UI text
- Target builds: WebGL (primary, for no-install demos) and Android
- Source control (Git + Git LFS for art assets)
- A grey-box art kit (Kenney/Synty placeholders) so engineering never waits on final art

## Week 1 — Build the Core Loop (grey-box, fun-first)

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 1 | Project + scene skeleton | Unity project builds to WebGL; empty Level 1 scene with placeholder UI zones (header, worker stage, Nova bar, thumb zone) |
| 2 | Worker Builder mechanic | Drag-and-drop 4 parts into slots with magnetic snap; progress dots fill; grey-box art |
| 3 | Builder juice + Nova hints | Snap spring-overshoot, sparkle particles, click-ding SFX; Nova one-line hints drive the sequence; worker "gains eyes" on Brain |
| 4 | Spec Card mechanic | Tap-to-fill word-tiles into 3 blanks; validation (correct vs. silly); undo by tapping a filled blank |
| 5 | The "silly spec" gag + correct path | Slapstick fail animation + sad-trombone (no penalty, auto-reset); green "SPEC LOCKED IN" on the correct spec |

**End of Week 1 milestone:** a player can build a worker and write a valid spec, with satisfying feedback. Internal smoke-test the build → spec flow.

## Week 2 — Close the Loop, Polish, Playtest

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 6 | Press GO + work animation | GO button juice; sequential tool-light-up (Read → Check Order → Policy → Write); progress bar; typewriter reply |
| 7 | Verify / Approve | Verify panel; Approve and Improve buttons; customer reacts (heart + 5 stars); coin arc on approve |
| 8 | Rewards + Night Shift unlock | Sequenced reward tally (coins → XP → unlock); XP bar level-up; ticking desk-clock for the idle hook |
| 9 | Art pass | Replace grey-box with first real 2.5D assets: worker, Nova, customer, UI skin, brand palette, lighting + bloom |
| 10 | Audio + juice pass | Full SFX set (click-ding, coin cha-ching, star chimes, power-up, sad-trombone), music loop, confetti/screen-shake tuning |
| 11 | Accessibility + reduced-motion | Colorblind-safe checks, caption text, reduced-motion toggle, big tap targets verified |
| 12 | Build, bug-fix, instrument | Stable WebGL + Android builds; add lightweight analytics (loop completion, retries, drop-off points) |
| 13 | Playtest | 5 to 8 fresh players; observe Level 1 completion, where they hesitate, and whether they smile at the core loop |
| 14 | Iterate + report | Fix the top 3 friction points found in testing; write a short validation report against the success metrics |

**End of Week 2 milestone:** a polished, playable Level 1 vertical slice with real art, audio, and instrumentation — ready to demo and to greenlight (or not) full production.

## Definition of Done (MVP)

- A new player can complete Level 1 unaided, start to finish
- Every core interaction has its feedback (snap, sparkle, ding, coin arc, confetti)
- Runs at a stable 60fps on a mid-range Android phone and in-browser (WebGL)
- Reduced-motion and caption settings function
- Analytics capture loop-completion and drop-off

## Success Metrics (the validation bar)

| Pillar | Measured by | Target |
|--------|-------------|--------|
| Easy | Level 1 completion rate (fresh players) | > 90% finish unaided |
| Fun | "Was that fun?" + observed smiles/replays | Majority yes; spontaneous replay |
| Interactive | Time-to-first-action; actions per minute | Fast first action; low confusion time |
| Graphics/feel | Frame rate + qualitative delight | Stable 60fps; testers react to the juice |
| Learning | Post-play: name the 4 FTE parts | > 80% recall |

If these targets are met, the assemble → spec → verify loop is proven and the project is ready to scale to the full 26-level game. If not, the report pinpoints exactly which pillar needs rework before further investment.

## Key Risks and Mitigations

- **Risk: the core loop is not fun.** Mitigation: build it grey-box in Week 1 and smoke-test early — do not wait for art to learn this.
- **Risk: art slips the schedule.** Mitigation: ship on placeholder assets; the art pass is Day 9, after the loop is proven.
- **Risk: the spec lesson does not land.** Mitigation: the "silly spec" gag is the teaching device — playtest it specifically and tune the comedy and reset feel.
- **Risk: WebGL performance.** Mitigation: target low draw calls and atlased textures from Day 1; test in-browser every build, not just in the editor.

---

# Sources

- The Agent Factory Thesis — <https://agentfactory.panaversity.org/docs/thesis>
- Synthesis: The Digital FTE Vision — <https://agentfactory.panaversity.org/docs/General-Agents-Foundations/agent-factory-paradigm/synthesis-digital-fte-vision>
- Project / Simulation Labs — <https://agentfactory.panaversity.org/docs/simulation-labs>
- Getting Started: Crash Courses — <https://agentfactory.panaversity.org/docs/getting-started>
- About the AI Agent Factory — <https://agentfactory.panaversity.org/docs/about>
- GitHub: panaversity/agentfactory — <https://github.com/panaversity/agentfactory>
