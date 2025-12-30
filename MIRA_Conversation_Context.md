# MIRA Project: Complete Conversation Context
## For Claude's Future Reference

---

## Document Purpose
This document captures the complete context of planning sessions for the MIRA (Memory-Intelligent Routine Assistant) project. Use this to understand decisions made, user requirements, and project background.

---

## User Profile: Sahil

### Professional Context
- **Role:** Technical Co-founder of Amolee (jewelry e-commerce startup)
- **Education:** Final-year B.Tech Civil Engineering, IIT Kanpur (graduating May 2026)
- **Location:** Jaipur, India (startup) / IIT Kanpur (studies)
- **Seeking:** AI/ML and full-stack development roles

### Technical Expertise
- AI/ML: YOLOv8, computer vision, structural defect detection
- Full-stack: React, Next.js, Python
- Experience: Cortex Construction (ML Engineer), Goyama International (Research Intern)
- Projects: Automated DPR Generator, ArUco marker pose estimation

### Current Workload
1. **Amolee** - January 2025 launch (website, AI rendering, customer service)
2. **Academics** - B.Tech project, coursework
3. **Job Search** - Active placements and interviews
4. **Side Projects** - DPR pipeline, AI tools exploration

---

## Problem Statement

Sahil needs a personal AI assistant that:
1. Captures raw voice/text inputs and autonomously structures daily work
2. Learns patterns over time for intelligent prioritization
3. Integrates with Google Calendar, Notion, Google Drive
4. Works cross-platform (mobile + laptop)
5. Remembers decisions, context, and people for 2+ years
6. Operates within ₹2,000-2,200/month budget (~$24-26)

### Key Pain Points
- Context switching between founder/student/job-seeker roles
- Forgetting past decisions and their context
- Manual task organization from voice notes
- No system that learns personal patterns

---

## Critical Budget Discovery

### Initial Misconception
User thought Claude Pro ($20/month) included API access for building the assistant.

### Reality
- Claude Pro = Web/mobile/desktop Claude.ai access only
- Does NOT include separate API access
- Using Claude Code would share token limits with personal usage

### Solution
- Keep Claude Pro for personal work (untouched)
- Use separate, cheaper APIs for MIRA:
  - **DeepSeek V3.2:** $0.28/M input, $0.42/M output (primary)
  - **Gemini 3 Flash:** $0.50/M input, $3.00/M output (fallback)

---

## Architecture Decisions

### Why These Choices Were Made

| Decision | Choice | Reasoning |
|----------|--------|-----------|
| **Orchestration** | LangGraph | Graph-based workflows, checkpointing, state management. 86K GitHub stars. |
| **Memory Pattern** | Letta's 3-tier | Core (always in context) + Archival (vector search) + Conversation (compressed). Proven pattern. |
| **Vector DB** | LanceDB | Embedded, disk-first, no server needed. 2 years of data = ~125MB. |
| **Primary LLM** | DeepSeek V3.2 | 10-30x cheaper than Claude/GPT, frontier performance, 128K context. |
| **Fallback LLM** | Gemini 3 Flash | 1M context, fast, reliable backup. |
| **Interface** | Telegram Bot + PWA | Telegram: voice works, notifications reliable. PWA: rich dashboard, analytics. |
| **Voice** | Web Speech API | Free, browser-native. Fallback to Whisper.cpp. |

### Why NOT These Alternatives

| Rejected Option | Reason |
|-----------------|--------|
| React Native | Requires native toolchain, app store approval, separate web codebase |
| Tauri | Requires Rust knowledge, mobile support still maturing |
| Claude API for MIRA | Would consume Claude Pro quota, affecting personal work |
| Storing audio files | 2 years = ~11GB. Transcribe-then-delete = ~75MB |
| Single LLM provider | Risk of downtime. Fallback essential. |

---

## Name Decision

### Final Choice: **MIRA** (Memory-Intelligent Routine Assistant)

### Naming Strategy
- **User-facing:** MIRA (friendly, easy to say globally)
- **Internal memory system:** Smriti (Sanskrit for "memory")

### Why MIRA Won
- Both Smriti and Mira liked by user
- MIRA works as both a name AND acronym
- Smriti preserved as internal reference (meaningful connection)
- "Hey Mira" is natural in voice commands

---

## User's Explicit Requirements

### Phase 1 MVP Must-Haves (from user)

1. **File/Photo Context Upload**
   - User wants to bootstrap system with existing knowledge
   - Upload PDFs, images, Notion exports
   - System extracts and stores context

2. **Recommendation System with Feedback**
   - 👍/👎 on every suggestion
   - System learns from corrections
   - Patterns detected automatically

3. **Goal Tracking Layer**
   - Vision → Yearly → Quarterly → Monthly → Tasks
   - Alignment check: "Are tasks moving toward goals?"

4. **Confirmation Mode**
   - NEVER auto-execute calendar/notion changes without approval
   - Start with suggestions only
   - Graduate to auto-execute after 2+ weeks of trust

5. **Quick Capture**
   - `/q buy milk` → instant task, no conversation
   - Voice notes for hands-free capture

6. **Export Function**
   - Always able to get data out
   - JSON and Notion formats

7. **Weekly Review**
   - Sunday evening summary
   - Pattern insights
   - Goal progress check

### Risk Handling (user emphasized)

| Risk | Mitigation |
|------|------------|
| Spend too much time building | Strict 2-week MVP deadline, then freeze |
| LLM gives bad advice | Confirmation required for all actions |
| Data loss | Daily automated backups to Google Drive |
| DeepSeek API goes down | Fallback to Gemini |
| Stop using it | Reminder after 7 days, ask why after 14 days |
| Over-reliance | Assistant suggests, YOU decide |

### Technical Safeguards (user emphasized)

| Issue | Solution |
|-------|----------|
| Error handling | Confirmation for destructive actions |
| Backup strategy | Daily backup to Google Drive |
| Security | Environment variables, never commit keys, encrypt sensitive memory |
| Offline mode | Local queue that syncs when online |
| Rate limits | Request queuing and caching |

### Product Safeguards (user emphasized)

| Issue | Solution |
|-------|----------|
| Cold start problem | Day 1 onboarding with file uploads and questions |
| Trust calibration | Suggestions only initially, auto-execute after 2 weeks |
| Feedback mechanism | Simple 👍/👎 on each suggestion |
| Weekly review | Sunday evening summary |
| Exit strategy | Export to JSON/Notion anytime |

### Personal Workflow Considerations

| Consideration | Implication |
|---------------|-------------|
| Quick capture outside Telegram | PWA fallback for meetings |
| Shared context with co-founder | Eventually add team features |
| Academic deadlines | Hard deadlines flagged specially |
| Interview prep mode | Different workflow when in interview season |

---

## Timeline Commitment

### User's Constraints
- Amolee launch: January 2025 (1 month away at time of planning)
- Available time: 15-20 hours/week for building
- Must not let building hurt Amolee launch

### Agreed Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Week 1-2 | 14 days | MVP: Telegram bot, voice/text capture, basic memory, feedback system |
| Week 3-4 | 14 days | Calendar + Notion integration, onboarding wizard |
| Month 2 | 4 weeks | Pattern detection, weekly review, goal tracking |
| Month 3 | 4 weeks | Polish, advanced features, optimization |

### User's Commitments (answered "yes" to all)

1. ✅ Commit to 2-week MVP, no scope creep
2. ✅ Use it daily even when imperfect
3. ✅ Resist adding features until March
4. ✅ Give feedback (👍/👎) consistently
5. ✅ Stop if not helping by Week 4

---

## Budget Breakdown (Final)

| Component | Monthly Cost (₹) |
|-----------|-----------------|
| Claude Pro (personal work only) | ₹1,670 ($20) |
| DeepSeek V3.2 API (~500K tokens) | ₹350 (~$4) |
| Gemini Flash (fallback, ~100K tokens) | ₹100 (~$1) |
| Google Cloud (Calendar/Drive API) | ₹0 (free tier) |
| Hosting (Vercel/Railway free tier) | ₹0 |
| **Total** | **₹2,120 (~$25)** ✅ |

---

## Technical Stack Summary

```
Input:        Telegram Bot (voice/text) + PWA (dashboard)
Processing:   Python 3.11+, LangGraph, sentence-transformers
LLM:          DeepSeek V3.2 (primary) + Gemini 3 Flash (fallback)
Memory:       SQLite (structured) + LanceDB (vectors)
Integrations: MCP servers for Calendar, Notion, Drive
Hosting:      Vercel/Railway free tier
Backup:       Google Drive (automated daily)
```

---

## Key Files Created

1. **MIRA_Implementation_Plan.md** - Complete technical specification with:
   - Architecture diagrams
   - Database schema (SQLite + LanceDB)
   - Full code implementations for Phase 1
   - All agent code (LangGraph)
   - Memory system (Smriti)
   - Feedback and learning system
   - Backup system
   - Onboarding wizard

2. **MIRA_Conversation_Context.md** (this file) - Decision context and rationale

---

## What MIRA Will Learn Over Time

### Automatic Learning (no user input needed)
- Task completion times → better time estimates
- Recurring task patterns → auto-suggest
- Document access patterns → project linking
- Response preferences → style adaptation

### Requires User Feedback
- Why task A was prioritized over B
- Whether decisions worked out well
- Context about people/relationships
- Energy patterns (unless health app connected)

### Learning Timeline
- Week 1-2: Teaching period (heavy input)
- Week 3-4: Basic patterns emerge
- Month 2-3: Meaningful predictions
- 6+ months: Deep personalization

---

## Success Criteria

### Week 2 (MVP)
- [ ] Voice and text task capture working
- [ ] Morning briefing generating
- [ ] Basic memory retrieval functional
- [ ] Feedback collection active

### Week 4 (Phase 1)
- [ ] Calendar integration complete
- [ ] Notion sync working
- [ ] Onboarding wizard functional
- [ ] Daily backups running

### Month 2 (Phase 2)
- [ ] Pattern detection showing results
- [ ] Time estimation improving
- [ ] Weekly review generating insights
- [ ] 80%+ feedback accuracy

---

## Honest Limitations Discussed

### What Won't Work Automatically
- Learning patterns without data (needs 4-6 weeks)
- Knowing importance without initial rules
- Zero input from user (needs occasional feedback)
- Perfect performance from Day 1
- Fully autonomous planning

### The Core Truth
> "The system learns from data you generate. No data = no learning. It's not magic, but it's genuinely intelligent with proper architecture and sufficient data."

---

## Next Steps After This Conversation

1. **Sahil creates:**
   - GitHub repository: `mira-assistant`
   - Telegram bot via BotFather
   - DeepSeek API account
   - Gemini API key
   - Google Cloud project for Calendar/Drive

2. **Day 1 tasks:**
   - Set up project structure
   - Initialize databases
   - Create basic Telegram bot

3. **Day 2 tasks:**
   - Implement core memory (Smriti)
   - Basic LLM integration

4. **Day 3-4 tasks:**
   - LangGraph agent setup
   - Intent classification

5. **Day 5-6 tasks:**
   - Feedback system
   - Document upload processing

6. **Day 7-14 tasks:**
   - Calendar integration
   - Polish and testing

---

## Document Metadata

- **Created:** December 31, 2024
- **Project:** MIRA - Memory-Intelligent Routine Assistant
- **User:** Sahil (IIT Kanpur / Amolee)
- **Assistant:** Claude Opus 4.5
- **Purpose:** Future context for continued development sessions

---

## How to Use This Document

When continuing MIRA development in future conversations:

1. **Reference this file** for architectural decisions
2. **Check Implementation Plan** for code details
3. **Respect user's constraints** (budget, timeline, commitments)
4. **Remember the philosophy:** Suggestions first, confirmation required, learning from feedback
5. **Name:** User-facing = MIRA, Internal memory = Smriti
