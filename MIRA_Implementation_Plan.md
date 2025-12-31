# MIRA: Memory-Intelligent Routine Assistant

## Complete Implementation Plan for Sahil's Personal AI Productivity System

---

## Project Overview

**Name:** MIRA (Memory-Intelligent Routine Assistant)  
**Internal Memory System:** Smriti  
**Creator:** Sahil (Technical Co-founder, Amolee | Final Year B.Tech, IIT Kanpur)  
**Start Date:** January 2025  
**MVP Deadline:** 14 days from start

### What MIRA Does

MIRA is a personal AI productivity assistant that:

1. Captures tasks from voice notes and text messages
2. Learns your patterns, priorities, and context over time
3. Manages your calendar, tasks, and projects
4. Remembers decisions, people, and project context for years
5. Provides daily planning and proactive suggestions

### Core Philosophy

- **Suggestions first, automation later** — MIRA suggests, you decide
- **Learn from feedback** — Every interaction makes it smarter
- **Minimal input, maximum output** — Raw thoughts → structured action
- **Your data, your control** — Export anytime, backup always

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         INPUT LAYER                                 │
├─────────────────────────────────────────────────────────────────────┤
│  Telegram Bot          │  PWA Dashboard         │  File Uploads     │
│  • Voice messages      │  • Calendar view       │  • PDFs, Images   │
│  • Text commands       │  • Task management     │  • Notion exports │
│  • Quick capture /q    │  • Settings            │  • Context docs   │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      PROCESSING LAYER                               │
├─────────────────────────────────────────────────────────────────────┤
│  Voice Transcription          │  Document Processing                │
│  • Web Speech API (free)      │  • PDF text extraction              │
│  • Whisper.cpp (local backup) │  • Image OCR (Tesseract)            │
│                               │  • Notion markdown parsing          │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER (LangGraph)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐              │
│  │   Router    │───▶│   Agents    │───▶│  Executor   │              │
│  │             │    │             │    │             │              │
│  │ • Classify  │    │ • Task      │    │ • Calendar  │              │
│  │   intent    │    │ • Planning  │    │ • Notion    │              │
│  │ • Route to  │    │ • Memory    │    │ • Drive     │              │
│  │   agent     │    │ • Research  │    │ • Export    │              │
│  └─────────────┘    └─────────────┘    └─────────────┘              │
│                                                                     │
│  State Management: Conversation context, user preferences           │
│  Checkpointer: SQLite (persistent across sessions)                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      LLM LAYER (Intelligence)                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Primary: DeepSeek V3.2 ($0.28/M input, $0.42/M output)             │
│  • Task extraction                                                  │
│  • Prioritization                                                   │
│  • Daily planning                                                   │
│  • Pattern analysis                                                 │
│                                                                     │
│  Fallback: Gemini 3 Flash ($0.50/M input, $3.00/M output)           │
│  • When DeepSeek is down                                            │
│  • Complex reasoning tasks                                          │
│                                                                     │
│  Your Claude Pro: UNTOUCHED (for your personal work)                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      MEMORY LAYER (Smriti)                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐      │
│  │  Core Memory    │  │ Archival Memory │  │  Conversation   │      │
│  │  (Always in     │  │ (Vector Search) │  │    Memory       │      │
│  │   context)      │  │                 │  │                 │      │
│  │                 │  │                 │  │                 │      │
│  │ • User profile  │  │ • Decisions     │  │ • Chat history  │      │
│  │ • Projects      │  │ • Facts learned │  │ • Compressed    │      │
│  │ • People        │  │ • Documents     │  │   summaries     │      │
│  │ • Preferences   │  │ • Patterns      │  │                 │      │
│  │                 │  │                 │  │                 │      │
│  │ ~2-4 KB         │  │ LanceDB         │  │ SQLite          │      │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    INTEGRATION LAYER (MCP Servers)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Google Calendar          Notion              Google Drive          │
│  • Create events          • Update databases  • Search documents    │
│  • Find free slots        • Create pages      • Backup storage      │
│  • Get schedule           • Read content      • File uploads        │
│                                                                     │
│  Gmail (Phase 2)          Custom APIs         Webhooks              │
│  • Read emails            • Amolee backend    • Calendar changes    │
│  • Categorize             • Other tools       • Notion updates      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                       OUTPUT LAYER                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Telegram                 PWA                  Integrations         │
│  • Responses              • Dashboard          • Calendar events    │
│  • Notifications          • Visualizations     • Notion pages       │
│  • Morning briefing       • Export UI          • Drive backups      │
│  • Weekly review          • Settings           │                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Database Schema

### 1. SQLite: Structured Data (`mira.db`)

```sql
-- User Profile
CREATE TABLE user_profile (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    timezone TEXT DEFAULT 'Asia/Kolkata',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'active', -- active, paused, completed, archived
    priority INTEGER DEFAULT 5, -- 1-10
    deadline DATE,
    parent_project_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_project_id) REFERENCES projects(id)
);

-- Goals (Quarterly/Monthly)
CREATE TABLE goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    goal_type TEXT NOT NULL, -- vision, yearly, quarterly, monthly
    target_date DATE,
    progress_percentage INTEGER DEFAULT 0,
    project_id INTEGER,
    parent_goal_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (parent_goal_id) REFERENCES goals(id)
);

-- Tasks
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending', -- pending, in_progress, completed, cancelled
    priority TEXT DEFAULT 'medium', -- critical, high, medium, low
    estimated_minutes INTEGER,
    actual_minutes INTEGER,
    due_date DATE,
    due_time TIME,
    project_id INTEGER,
    goal_id INTEGER,
    recurring_pattern TEXT, -- daily, weekly:mon,wed,fri, monthly:15
    depends_on_task_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    created_from TEXT, -- voice, text, calendar, notion
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (goal_id) REFERENCES goals(id),
    FOREIGN KEY (depends_on_task_id) REFERENCES tasks(id)
);

-- People
CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    relationship TEXT, -- professor, co-founder, client, recruiter, friend
    organization TEXT,
    email TEXT,
    phone TEXT,
    preferences TEXT, -- JSON: communication style, availability, etc.
    notes TEXT,
    project_ids TEXT, -- JSON array of related project IDs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Decisions (Important for recall)
CREATE TABLE decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    context TEXT, -- why this decision was made
    alternatives_considered TEXT, -- JSON array
    outcome TEXT, -- good, bad, neutral, pending
    project_id INTEGER,
    people_involved TEXT, -- JSON array of people IDs
    decision_date DATE NOT NULL,
    review_date DATE, -- when to review this decision
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Feedback Log (For learning)
CREATE TABLE feedback_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    interaction_id TEXT NOT NULL, -- links to conversation
    feedback_type TEXT NOT NULL, -- thumbs_up, thumbs_down, correction
    original_suggestion TEXT,
    user_correction TEXT,
    category TEXT, -- prioritization, scheduling, task_extraction, etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pattern Log (For learning)
CREATE TABLE pattern_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_type TEXT NOT NULL, -- time_estimation, energy, recurring_task, preference
    pattern_key TEXT NOT NULL, -- e.g., "coding_tasks", "monday_morning"
    pattern_value TEXT NOT NULL, -- JSON with pattern data
    confidence_score REAL DEFAULT 0.5, -- 0-1, increases with more data
    sample_count INTEGER DEFAULT 1,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Time Blocks (Calendar sync)
CREATE TABLE time_blocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER,
    calendar_event_id TEXT, -- Google Calendar event ID
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    block_type TEXT DEFAULT 'task', -- task, meeting, focus, break
    status TEXT DEFAULT 'scheduled', -- scheduled, completed, cancelled, rescheduled
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);

-- Conversation History (Compressed)
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL, -- user, assistant
    content TEXT NOT NULL,
    summary TEXT, -- compressed version for long-term storage
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Daily Summaries (For pattern detection)
CREATE TABLE daily_summaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE UNIQUE NOT NULL,
    tasks_completed INTEGER DEFAULT 0,
    tasks_created INTEGER DEFAULT 0,
    focus_minutes INTEGER DEFAULT 0,
    meetings_count INTEGER DEFAULT 0,
    energy_rating INTEGER, -- 1-5, user-reported
    productivity_rating INTEGER, -- 1-5, user-reported
    summary_text TEXT,
    patterns_detected TEXT, -- JSON
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- System Config
CREATE TABLE system_config (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Backup Log
CREATE TABLE backup_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    backup_type TEXT NOT NULL, -- daily, weekly, manual
    backup_location TEXT NOT NULL, -- Google Drive path
    file_size_bytes INTEGER,
    status TEXT DEFAULT 'success', -- success, failed
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE INDEX idx_tasks_project ON tasks(project_id);
CREATE INDEX idx_decisions_project ON decisions(project_id);
CREATE INDEX idx_feedback_category ON feedback_log(category);
CREATE INDEX idx_pattern_type ON pattern_log(pattern_type);
CREATE INDEX idx_conversations_session ON conversations(session_id);
CREATE INDEX idx_daily_summaries_date ON daily_summaries(date);
```

### 2. LanceDB: Vector Memory (Archival/Smriti)

```python
# Schema for LanceDB tables

# Documents table - for uploaded files, decisions, notes
documents_schema = {
    "id": "string",
    "content": "string",
    "embedding": "vector[384]",  # all-MiniLM-L6-v2
    "doc_type": "string",  # decision, note, file, conversation_summary
    "source": "string",  # filename, notion_page, conversation_id
    "project_id": "int",
    "created_at": "timestamp",
    "metadata": "string"  # JSON with additional info
}

# Facts table - learned facts about user
facts_schema = {
    "id": "string",
    "fact": "string",
    "embedding": "vector[384]",
    "category": "string",  # preference, pattern, decision, context
    "confidence": "float",
    "source_conversation_id": "string",
    "created_at": "timestamp",
    "last_accessed": "timestamp",
    "access_count": "int"
}

# People context - detailed info about people
people_context_schema = {
    "id": "string",
    "person_id": "int",  # links to SQLite people table
    "context": "string",
    "embedding": "vector[384]",
    "interaction_type": "string",  # meeting, email, decision, preference
    "created_at": "timestamp"
}
```

---

## Phase 1: MVP (Days 1-14)

### Day 1-2: Project Setup & Infrastructure

**Tasks:**

- [ ] Create GitHub repository: `mira-assistant`
- [ ] Set up Python virtual environment
- [ ] Install core dependencies
- [ ] Create project structure
- [ ] Set up environment variables
- [ ] Create SQLite database with schema
- [ ] Initialize LanceDB

**Project Structure:**

```
mira-assistant/
├── .env                      # API keys (never commit)
├── .env.example              # Template for env vars
├── .gitignore
├── README.md
├── requirements.txt
├── docker-compose.yml        # For local development
│
├── src/
│   ├── __init__.py
│   ├── config.py             # Configuration management
│   ├── main.py               # Entry point
│   │
│   ├── bot/                  # Telegram bot
│   │   ├── __init__.py
│   │   ├── handlers.py       # Message handlers
│   │   ├── commands.py       # Command handlers (/q, /today, etc.)
│   │   └── keyboards.py      # Inline keyboards for feedback
│   │
│   ├── agents/               # LangGraph agents
│   │   ├── __init__.py
│   │   ├── router.py         # Intent classification & routing
│   │   ├── task_agent.py     # Task extraction & management
│   │   ├── planning_agent.py # Daily planning & scheduling
│   │   ├── memory_agent.py   # Memory retrieval & storage
│   │   └── graph.py          # LangGraph workflow definition
│   │
│   ├── memory/               # Smriti - Memory system
│   │   ├── __init__.py
│   │   ├── core_memory.py    # Always-in-context memory
│   │   ├── archival.py       # LanceDB operations
│   │   ├── conversation.py   # Conversation history
│   │   └── consolidation.py  # Memory compression
│   │
│   ├── integrations/         # External services
│   │   ├── __init__.py
│   │   ├── calendar.py       # Google Calendar MCP
│   │   ├── notion.py         # Notion MCP
│   │   ├── drive.py          # Google Drive (backup)
│   │   └── llm.py            # DeepSeek/Gemini wrapper
│   │
│   ├── processing/           # Input processing
│   │   ├── __init__.py
│   │   ├── voice.py          # Voice transcription
│   │   ├── documents.py      # PDF, image, text processing
│   │   └── notion_import.py  # Notion export parsing
│   │
│   ├── learning/             # Pattern detection & feedback
│   │   ├── __init__.py
│   │   ├── feedback.py       # Feedback collection
│   │   ├── patterns.py       # Pattern detection
│   │   └── recommendations.py # Recommendation engine
│   │
│   └── utils/
│       ├── __init__.py
│       ├── database.py       # SQLite operations
│       ├── backup.py         # Backup to Drive
│       ├── export.py         # Export to JSON/Notion
│       └── queue.py          # Offline request queue
│
├── data/
│   ├── mira.db               # SQLite database
│   ├── lancedb/              # LanceDB storage
│   └── backups/              # Local backup before upload
│
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_memory.py
│   └── test_integrations.py
│
├── scripts/
│   ├── setup_database.py     # Initialize DB
│   ├── onboarding.py         # Day 1 setup wizard
│   └── backup_cron.py        # Daily backup script
│
└── docs/
    ├── SETUP.md
    ├── COMMANDS.md
    └── ARCHITECTURE.md
```

**Dependencies (requirements.txt):**

```
# Core
python-telegram-bot==21.0
langgraph==0.2.0
langchain==0.3.0
langchain-community==0.3.0

# LLM Providers
openai==1.0.0  # DeepSeek uses OpenAI-compatible API
google-generativeai==0.8.0

# Database
lancedb==0.15.0
sentence-transformers==3.0.0

# Document Processing
pypdf2==3.0.0
python-docx==1.1.0
pytesseract==0.3.10
Pillow==10.0.0

# Utilities
python-dotenv==1.0.0
pydantic==2.5.0
httpx==0.27.0
apscheduler==3.10.0  # For scheduled tasks

# MCP
mcp==1.0.0
fastmcp==0.1.0
```

### Day 3-4: Core Memory System (Smriti)

**Implementation: `src/memory/core_memory.py`**

```python
"""
Core Memory - Always in context, ~2-4KB
This is what MIRA "knows" without searching
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json

@dataclass
class UserProfile:
    name: str
    timezone: str = "Asia/Kolkata"
    communication_style: str = "concise"  # concise, detailed, casual
    energy_peak_hours: List[int] = field(default_factory=lambda: [9, 10, 11])

@dataclass
class Project:
    id: int
    name: str
    status: str
    priority: int
    short_context: str  # 1-2 sentences

@dataclass
class Person:
    id: int
    name: str
    relationship: str
    key_preference: str  # Most important thing to remember

@dataclass
class CoreMemory:
    """
    This entire object is serialized and included in every LLM call.
    Must stay under 2-4KB to not waste tokens.
    """
    user: UserProfile
    active_projects: List[Project] = field(default_factory=list)  # Max 5
    key_people: List[Person] = field(default_factory=list)  # Max 10
    current_goals: List[str] = field(default_factory=list)  # Max 3
    recent_decisions: List[str] = field(default_factory=list)  # Max 5
    learned_preferences: Dict[str, str] = field(default_factory=dict)
    today_context: str = ""  # Updated daily

    def to_prompt(self) -> str:
        """Convert to string for LLM context"""
        return f"""
## About {self.user.name}
- Timezone: {self.user.timezone}
- Communication style: {self.user.communication_style}
- Peak energy hours: {self.user.energy_peak_hours}

## Active Projects (Priority Order)
{self._format_projects()}

## Key People
{self._format_people()}

## Current Goals
{self._format_goals()}

## Recent Important Decisions
{self._format_decisions()}

## Learned Preferences
{self._format_preferences()}

## Today's Context
{self.today_context}
"""

    def _format_projects(self) -> str:
        return "\n".join([
            f"- {p.name} [{p.status}]: {p.short_context}"
            for p in self.active_projects[:5]
        ])

    def _format_people(self) -> str:
        return "\n".join([
            f"- {p.name} ({p.relationship}): {p.key_preference}"
            for p in self.key_people[:10]
        ])

    def _format_goals(self) -> str:
        return "\n".join([f"- {g}" for g in self.current_goals[:3]])

    def _format_decisions(self) -> str:
        return "\n".join([f"- {d}" for d in self.recent_decisions[:5]])

    def _format_preferences(self) -> str:
        return "\n".join([
            f"- {k}: {v}"
            for k, v in list(self.learned_preferences.items())[:10]
        ])

    def update_from_feedback(self, category: str, learned: str):
        """Update preferences based on feedback"""
        self.learned_preferences[category] = learned

    def add_decision(self, decision: str):
        """Add a new decision, keep only recent 5"""
        self.recent_decisions.insert(0, decision)
        self.recent_decisions = self.recent_decisions[:5]

    def save(self, db_path: str):
        """Persist to SQLite"""
        # Implementation: serialize to JSON and store in system_config
        pass

    @classmethod
    def load(cls, db_path: str) -> 'CoreMemory':
        """Load from SQLite"""
        # Implementation: deserialize from system_config
        pass
```

**Implementation: `src/memory/archival.py`**

```python
"""
Archival Memory - LanceDB vector store
For decisions, documents, facts, patterns
"""

import lancedb
from sentence_transformers import SentenceTransformer
from datetime import datetime
from typing import List, Dict, Optional
import uuid

class ArchivalMemory:
    def __init__(self, db_path: str = "data/lancedb"):
        self.db = lancedb.connect(db_path)
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self._init_tables()

    def _init_tables(self):
        """Initialize LanceDB tables if not exist"""
        # Documents table
        if "documents" not in self.db.table_names():
            self.db.create_table("documents", data=[{
                "id": "init",
                "content": "initialization",
                "embedding": self.encoder.encode("initialization").tolist(),
                "doc_type": "system",
                "source": "init",
                "project_id": 0,
                "created_at": datetime.now().isoformat(),
                "metadata": "{}"
            }])

        # Facts table
        if "facts" not in self.db.table_names():
            self.db.create_table("facts", data=[{
                "id": "init",
                "fact": "initialization",
                "embedding": self.encoder.encode("initialization").tolist(),
                "category": "system",
                "confidence": 0.0,
                "source_conversation_id": "init",
                "created_at": datetime.now().isoformat(),
                "last_accessed": datetime.now().isoformat(),
                "access_count": 0
            }])

    def store_document(
        self,
        content: str,
        doc_type: str,
        source: str,
        project_id: int = 0,
        metadata: Dict = None
    ) -> str:
        """Store a document with its embedding"""
        doc_id = str(uuid.uuid4())
        embedding = self.encoder.encode(content).tolist()

        table = self.db.open_table("documents")
        table.add([{
            "id": doc_id,
            "content": content,
            "embedding": embedding,
            "doc_type": doc_type,
            "source": source,
            "project_id": project_id,
            "created_at": datetime.now().isoformat(),
            "metadata": json.dumps(metadata or {})
        }])

        return doc_id

    def store_fact(
        self,
        fact: str,
        category: str,
        confidence: float = 0.5,
        conversation_id: str = ""
    ) -> str:
        """Store a learned fact"""
        fact_id = str(uuid.uuid4())
        embedding = self.encoder.encode(fact).tolist()

        table = self.db.open_table("facts")
        table.add([{
            "id": fact_id,
            "fact": fact,
            "embedding": embedding,
            "category": category,
            "confidence": confidence,
            "source_conversation_id": conversation_id,
            "created_at": datetime.now().isoformat(),
            "last_accessed": datetime.now().isoformat(),
            "access_count": 0
        }])

        return fact_id

    def search_documents(
        self,
        query: str,
        doc_type: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """Search documents by semantic similarity"""
        query_embedding = self.encoder.encode(query).tolist()
        table = self.db.open_table("documents")

        results = table.search(query_embedding).limit(limit).to_list()

        if doc_type:
            results = [r for r in results if r["doc_type"] == doc_type]

        return results

    def search_facts(
        self,
        query: str,
        category: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """Search facts by semantic similarity"""
        query_embedding = self.encoder.encode(query).tolist()
        table = self.db.open_table("facts")

        results = table.search(query_embedding).limit(limit).to_list()

        if category:
            results = [r for r in results if r["category"] == category]

        # Update access count for retrieved facts
        for r in results:
            self._update_fact_access(r["id"])

        return results

    def _update_fact_access(self, fact_id: str):
        """Update last_accessed and access_count for a fact"""
        # Implementation: update the fact record
        pass

    def get_stale_facts(self, days_threshold: int = 180) -> List[Dict]:
        """Get facts not accessed in X days (for cleanup)"""
        # Implementation: query facts with old last_accessed
        pass

    def delete_fact(self, fact_id: str):
        """Delete a fact (for cleanup or correction)"""
        table = self.db.open_table("facts")
        table.delete(f'id = "{fact_id}"')
```

### Day 5-6: LLM Integration & Basic Agent

**Implementation: `src/integrations/llm.py`**

```python
"""
LLM Provider Wrapper
Supports DeepSeek (primary) and Gemini (fallback)
"""

from openai import OpenAI
import google.generativeai as genai
from typing import List, Dict, Optional
import os
import time
from functools import wraps

class RateLimiter:
    """Simple rate limiter for API calls"""
    def __init__(self, calls_per_minute: int = 60):
        self.calls_per_minute = calls_per_minute
        self.calls = []

    def wait_if_needed(self):
        now = time.time()
        # Remove calls older than 1 minute
        self.calls = [c for c in self.calls if now - c < 60]

        if len(self.calls) >= self.calls_per_minute:
            sleep_time = 60 - (now - self.calls[0])
            if sleep_time > 0:
                time.sleep(sleep_time)

        self.calls.append(time.time())

class LLMProvider:
    def __init__(self):
        # DeepSeek (OpenAI-compatible API)
        self.deepseek = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com/v1"
        )

        # Gemini (fallback)
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.gemini = genai.GenerativeModel('gemini-1.5-flash')

        # Rate limiters
        self.deepseek_limiter = RateLimiter(calls_per_minute=60)
        self.gemini_limiter = RateLimiter(calls_per_minute=60)

        # Track which provider to use
        self.primary = "deepseek"
        self.deepseek_failures = 0

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        use_fallback: bool = False
    ) -> str:
        """
        Send chat completion request
        Messages format: [{"role": "system/user/assistant", "content": "..."}]
        """
        if use_fallback or self.deepseek_failures >= 3:
            return self._gemini_chat(messages, temperature, max_tokens)

        try:
            return self._deepseek_chat(messages, temperature, max_tokens)
        except Exception as e:
            print(f"DeepSeek error: {e}, falling back to Gemini")
            self.deepseek_failures += 1
            return self._gemini_chat(messages, temperature, max_tokens)

    def _deepseek_chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int
    ) -> str:
        """DeepSeek API call"""
        self.deepseek_limiter.wait_if_needed()

        response = self.deepseek.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Reset failure count on success
        self.deepseek_failures = 0

        return response.choices[0].message.content

    def _gemini_chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int
    ) -> str:
        """Gemini API call"""
        self.gemini_limiter.wait_if_needed()

        # Convert messages to Gemini format
        prompt = self._messages_to_prompt(messages)

        response = self.gemini.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )

        return response.text

    def _messages_to_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Convert OpenAI message format to single prompt for Gemini"""
        parts = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                parts.append(f"System Instructions:\n{content}\n")
            elif role == "user":
                parts.append(f"User: {content}\n")
            elif role == "assistant":
                parts.append(f"Assistant: {content}\n")
        return "\n".join(parts)

# Singleton instance
llm = LLMProvider()
```

### Day 7-8: Telegram Bot & Basic Commands

**Implementation: `src/bot/handlers.py`**

```python
"""
Telegram Bot Handlers
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)
import os
from datetime import datetime

from src.agents.graph import MiraGraph
from src.memory.core_memory import CoreMemory
from src.learning.feedback import FeedbackCollector

class MiraBot:
    def __init__(self):
        self.app = Application.builder().token(
            os.getenv("TELEGRAM_BOT_TOKEN")
        ).build()

        self.mira = MiraGraph()
        self.core_memory = CoreMemory.load("data/mira.db")
        self.feedback = FeedbackCollector()

        self._register_handlers()

    def _register_handlers(self):
        """Register all bot handlers"""
        # Commands
        self.app.add_handler(CommandHandler("start", self.cmd_start))
        self.app.add_handler(CommandHandler("q", self.cmd_quick_task))
        self.app.add_handler(CommandHandler("today", self.cmd_today))
        self.app.add_handler(CommandHandler("plan", self.cmd_plan))
        self.app.add_handler(CommandHandler("decide", self.cmd_decide))
        self.app.add_handler(CommandHandler("remember", self.cmd_remember))
        self.app.add_handler(CommandHandler("export", self.cmd_export))
        self.app.add_handler(CommandHandler("help", self.cmd_help))

        # Messages
        self.app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            self.handle_message
        ))
        self.app.add_handler(MessageHandler(
            filters.VOICE,
            self.handle_voice
        ))
        self.app.add_handler(MessageHandler(
            filters.Document.ALL | filters.PHOTO,
            self.handle_document
        ))

        # Callbacks (for inline keyboards)
        self.app.add_handler(CallbackQueryHandler(self.handle_callback))

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Welcome message and onboarding"""
        welcome = """
👋 Hi! I'm MIRA, your Memory-Intelligent Routine Assistant.

I help you:
• Capture and organize tasks from voice/text
• Plan your day intelligently
• Remember decisions and context
• Learn your patterns over time

**Quick Commands:**
/q <task> - Quick task capture
/today - Today's plan and tasks
/plan - Generate daily plan
/decide <decision> - Log important decision
/remember <query> - Search your memory
/export - Export your data

**Getting Started:**
Send me a voice note or text about what you're working on, and I'll help you organize it!

Would you like to start with onboarding to tell me about your projects?
        """

        keyboard = [
            [InlineKeyboardButton("✅ Start Onboarding", callback_data="onboarding_start")],
            [InlineKeyboardButton("⏭️ Skip for now", callback_data="onboarding_skip")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(welcome, reply_markup=reply_markup)

    async def cmd_quick_task(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Quick task capture: /q buy milk tomorrow"""
        if not context.args:
            await update.message.reply_text(
                "Usage: /q <task description>\nExample: /q call gem supplier tomorrow"
            )
            return

        task_text = " ".join(context.args)

        # Process through MIRA
        result = await self.mira.process_quick_task(task_text, self.core_memory)

        # Show result with feedback buttons
        keyboard = [
            [
                InlineKeyboardButton("👍", callback_data=f"fb_up_{result['task_id']}"),
                InlineKeyboardButton("👎", callback_data=f"fb_down_{result['task_id']}"),
                InlineKeyboardButton("✏️ Edit", callback_data=f"fb_edit_{result['task_id']}")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        response = f"""
✅ Task captured!

**{result['title']}**
📅 Due: {result['due_date'] or 'No deadline'}
🏷️ Priority: {result['priority']}
📁 Project: {result['project'] or 'Unassigned'}

{result['confirmation_note']}
        """

        await update.message.reply_text(
            response,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def cmd_today(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show today's plan and tasks"""
        briefing = await self.mira.get_daily_briefing(self.core_memory)

        response = f"""
🌅 **Good {'morning' if datetime.now().hour < 12 else 'afternoon'}, {self.core_memory.user.name}!**

**Today's Overview:**
{briefing['summary']}

**Priority Tasks:**
{self._format_tasks(briefing['priority_tasks'])}

**Scheduled:**
{self._format_schedule(briefing['schedule'])}

**Reminders:**
{briefing['reminders']}
        """

        await update.message.reply_text(response, parse_mode='Markdown')

    async def cmd_plan(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Generate suggested daily plan"""
        plan = await self.mira.generate_plan(self.core_memory)

        keyboard = [
            [
                InlineKeyboardButton("✅ Accept Plan", callback_data="plan_accept"),
                InlineKeyboardButton("🔄 Regenerate", callback_data="plan_regen")
            ],
            [
                InlineKeyboardButton("✏️ Modify", callback_data="plan_modify")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        response = f"""
📋 **Suggested Plan for Today:**

{plan['formatted_plan']}

**Reasoning:**
{plan['reasoning']}

Would you like me to block these times in your calendar?
        """

        await update.message.reply_text(
            response,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def cmd_decide(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Log an important decision"""
        if not context.args:
            await update.message.reply_text(
                "Usage: /decide <decision description>\n"
                "Example: /decide Set ring collection price at ₹15,000-25,000 range"
            )
            return

        decision_text = " ".join(context.args)
        result = await self.mira.log_decision(decision_text, self.core_memory)

        response = f"""
📝 **Decision Logged**

{result['formatted_decision']}

I'll remember this. You can recall it anytime with:
/remember {result['keywords']}
        """

        await update.message.reply_text(response, parse_mode='Markdown')

    async def cmd_remember(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Search memory for past context"""
        if not context.args:
            await update.message.reply_text(
                "Usage: /remember <query>\n"
                "Example: /remember ring pricing decision"
            )
            return

        query = " ".join(context.args)
        results = await self.mira.search_memory(query, self.core_memory)

        if not results:
            await update.message.reply_text(
                "I couldn't find anything matching that query. "
                "Try different keywords or be more specific."
            )
            return

        response = f"""
🔍 **Found {len(results)} relevant items:**

{self._format_memory_results(results)}
        """

        await update.message.reply_text(response, parse_mode='Markdown')

    async def cmd_export(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Export user data"""
        keyboard = [
            [
                InlineKeyboardButton("📄 JSON", callback_data="export_json"),
                InlineKeyboardButton("📝 Markdown", callback_data="export_md")
            ],
            [
                InlineKeyboardButton("📊 Notion", callback_data="export_notion")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "Choose export format:",
            reply_markup=reply_markup
        )

    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show help"""
        help_text = """
**MIRA Commands:**

**Task Management:**
/q <task> - Quick task capture
/today - Today's briefing
/plan - Generate daily plan

**Memory:**
/decide <decision> - Log decision
/remember <query> - Search memory

**Data:**
/export - Export your data

**Tips:**
• Send voice notes for hands-free capture
• Upload documents to add context
• Use 👍/👎 to help me learn
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        text = update.message.text

        # Process through MIRA
        response = await self.mira.process_message(text, self.core_memory)

        # Add feedback buttons if action was taken
        if response.get('action_taken'):
            keyboard = [
                [
                    InlineKeyboardButton("👍", callback_data=f"fb_up_{response['id']}"),
                    InlineKeyboardButton("👎", callback_data=f"fb_down_{response['id']}")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
        else:
            reply_markup = None

        await update.message.reply_text(
            response['message'],
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def handle_voice(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle voice messages"""
        voice = update.message.voice

        # Download voice file
        file = await context.bot.get_file(voice.file_id)
        voice_path = f"data/temp/voice_{voice.file_id}.ogg"
        await file.download_to_drive(voice_path)

        # Transcribe
        transcript = await self.mira.transcribe_voice(voice_path)

        # Process transcript
        response = await self.mira.process_message(transcript, self.core_memory)

        # Clean up temp file
        os.remove(voice_path)

        # Response with transcript shown
        full_response = f"""
🎤 *Heard:* "{transcript}"

{response['message']}
        """

        keyboard = [
            [
                InlineKeyboardButton("👍", callback_data=f"fb_up_{response['id']}"),
                InlineKeyboardButton("👎", callback_data=f"fb_down_{response['id']}")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            full_response,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle document/photo uploads for context"""
        # Get file
        if update.message.document:
            file = await context.bot.get_file(update.message.document.file_id)
            filename = update.message.document.file_name
        else:
            file = await context.bot.get_file(update.message.photo[-1].file_id)
            filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Download
        file_path = f"data/temp/{filename}"
        await file.download_to_drive(file_path)

        # Process and add to memory
        result = await self.mira.process_document(file_path, self.core_memory)

        response = f"""
📎 **Document processed:** {filename}

{result['summary']}

**Added to memory:**
{result['facts_extracted']}

I'll use this context in future conversations.
        """

        await update.message.reply_text(response, parse_mode='Markdown')

    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard callbacks"""
        query = update.callback_query
        await query.answer()

        data = query.data

        if data.startswith("fb_up_"):
            item_id = data.replace("fb_up_", "")
            self.feedback.record(item_id, "thumbs_up")
            await query.edit_message_reply_markup(reply_markup=None)

        elif data.startswith("fb_down_"):
            item_id = data.replace("fb_down_", "")
            await query.message.reply_text(
                "What should I have done differently?",
                reply_to_message_id=query.message.message_id
            )
            # Next message from user will be the correction
            context.user_data['pending_correction'] = item_id

        elif data == "onboarding_start":
            await self._start_onboarding(query, context)

        elif data == "plan_accept":
            # Block calendar
            await self._accept_plan(query, context)

        # ... more callback handlers

    def _format_tasks(self, tasks: list) -> str:
        """Format task list for display"""
        if not tasks:
            return "No tasks for today! 🎉"

        return "\n".join([
            f"{'✅' if t['done'] else '⬜'} {t['title']} "
            f"({'⚡' if t['priority'] == 'high' else '📌'})"
            for t in tasks
        ])

    def _format_schedule(self, schedule: list) -> str:
        """Format schedule for display"""
        if not schedule:
            return "No scheduled events"

        return "\n".join([
            f"🕐 {s['time']} - {s['title']}"
            for s in schedule
        ])

    def _format_memory_results(self, results: list) -> str:
        """Format memory search results"""
        formatted = []
        for i, r in enumerate(results, 1):
            formatted.append(
                f"{i}. **{r['type']}** ({r['date']})\n"
                f"   {r['content'][:200]}..."
            )
        return "\n\n".join(formatted)

    def run(self):
        """Start the bot"""
        print("🤖 MIRA is starting...")
        self.app.run_polling()
```

### Day 9-10: LangGraph Agent & Routing

**Implementation: `src/agents/graph.py`**

```python
"""
MIRA LangGraph Workflow
Main orchestration for all agent activities
"""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, List, Optional, Literal
from datetime import datetime

from src.integrations.llm import llm
from src.memory.core_memory import CoreMemory
from src.memory.archival import ArchivalMemory

class MiraState(TypedDict):
    """State that flows through the graph"""
    # Input
    user_input: str
    input_type: str  # text, voice, document

    # Context
    core_memory: str  # Serialized core memory
    retrieved_context: List[str]

    # Processing
    intent: str  # task, question, planning, decision, memory_query, chat
    entities: dict  # Extracted entities (dates, people, projects)

    # Output
    response: str
    actions_taken: List[dict]
    requires_confirmation: bool
    confirmation_prompt: str

    # Feedback
    interaction_id: str

class MiraGraph:
    def __init__(self):
        self.archival = ArchivalMemory()
        self.checkpointer = SqliteSaver.from_conn_string("data/mira.db")
        self.graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow"""
        workflow = StateGraph(MiraState)

        # Add nodes
        workflow.add_node("classify_intent", self.classify_intent)
        workflow.add_node("retrieve_context", self.retrieve_context)
        workflow.add_node("task_agent", self.task_agent)
        workflow.add_node("planning_agent", self.planning_agent)
        workflow.add_node("memory_agent", self.memory_agent)
        workflow.add_node("decision_agent", self.decision_agent)
        workflow.add_node("chat_agent", self.chat_agent)
        workflow.add_node("prepare_response", self.prepare_response)

        # Set entry point
        workflow.set_entry_point("classify_intent")

        # Add edges
        workflow.add_edge("classify_intent", "retrieve_context")

        # Conditional routing based on intent
        workflow.add_conditional_edges(
            "retrieve_context",
            self.route_to_agent,
            {
                "task": "task_agent",
                "planning": "planning_agent",
                "memory_query": "memory_agent",
                "decision": "decision_agent",
                "chat": "chat_agent"
            }
        )

        # All agents lead to response preparation
        workflow.add_edge("task_agent", "prepare_response")
        workflow.add_edge("planning_agent", "prepare_response")
        workflow.add_edge("memory_agent", "prepare_response")
        workflow.add_edge("decision_agent", "prepare_response")
        workflow.add_edge("chat_agent", "prepare_response")

        workflow.add_edge("prepare_response", END)

        return workflow.compile(checkpointer=self.checkpointer)

    async def classify_intent(self, state: MiraState) -> MiraState:
        """Classify user intent"""
        prompt = f"""
Classify the user's intent into one of these categories:
- task: Creating, updating, or asking about tasks
- planning: Daily planning, scheduling, time management
- memory_query: Asking about past decisions, context, or information
- decision: Logging or discussing a decision
- chat: General conversation, questions, or requests

User input: {state['user_input']}

Respond with just the category name.
"""

        intent = llm.chat([
            {"role": "system", "content": "You are an intent classifier. Respond with only the category name."},
            {"role": "user", "content": prompt}
        ]).strip().lower()

        # Extract entities (dates, people, projects)
        entities = await self._extract_entities(state['user_input'])

        return {
            **state,
            "intent": intent,
            "entities": entities
        }

    async def retrieve_context(self, state: MiraState) -> MiraState:
        """Retrieve relevant context from memory"""
        # Search archival memory based on input
        docs = self.archival.search_documents(state['user_input'], limit=3)
        facts = self.archival.search_facts(state['user_input'], limit=3)

        context = []
        for doc in docs:
            context.append(f"[Document: {doc['source']}] {doc['content'][:500]}")
        for fact in facts:
            context.append(f"[Fact] {fact['fact']}")

        return {
            **state,
            "retrieved_context": context
        }

    def route_to_agent(self, state: MiraState) -> str:
        """Route to appropriate agent based on intent"""
        intent = state.get("intent", "chat")
        if intent in ["task", "planning", "memory_query", "decision", "chat"]:
            return intent
        return "chat"

    async def task_agent(self, state: MiraState) -> MiraState:
        """Handle task-related requests"""
        system_prompt = f"""
You are MIRA's task management agent. Your job is to:
1. Extract task details from user input
2. Suggest priority and deadline
3. Link to relevant projects
4. Identify dependencies

User Context:
{state['core_memory']}

Retrieved Context:
{chr(10).join(state['retrieved_context'])}

Always respond in this JSON format:
{{
    "task_title": "...",
    "description": "...",
    "priority": "critical/high/medium/low",
    "due_date": "YYYY-MM-DD or null",
    "due_time": "HH:MM or null",
    "project": "project name or null",
    "depends_on": "task description or null",
    "reasoning": "why you made these choices",
    "confirmation_needed": true/false,
    "confirmation_question": "..."
}}
"""

        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['user_input']}
        ])

        # Parse JSON response and create task
        # ... implementation

        return {
            **state,
            "response": response,
            "actions_taken": [{"type": "task_created", "details": "..."}],
            "requires_confirmation": True
        }

    async def planning_agent(self, state: MiraState) -> MiraState:
        """Handle planning and scheduling requests"""
        system_prompt = f"""
You are MIRA's planning agent. Your job is to:
1. Understand the user's planning needs
2. Consider their energy patterns and preferences
3. Create realistic time blocks
4. Account for buffer time

User Context:
{state['core_memory']}

Retrieved Context:
{chr(10).join(state['retrieved_context'])}

Current time: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['user_input']}
        ])

        return {
            **state,
            "response": response,
            "requires_confirmation": True,
            "confirmation_prompt": "Should I block these times in your calendar?"
        }

    async def memory_agent(self, state: MiraState) -> MiraState:
        """Handle memory queries"""
        system_prompt = f"""
You are MIRA's memory agent. Your job is to:
1. Search through stored knowledge
2. Find relevant past decisions and context
3. Present information clearly

User Context:
{state['core_memory']}

Retrieved Context:
{chr(10).join(state['retrieved_context'])}

Synthesize the retrieved context to answer the user's question.
If you don't have enough information, say so clearly.
"""

        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['user_input']}
        ])

        return {
            **state,
            "response": response,
            "requires_confirmation": False
        }

    async def decision_agent(self, state: MiraState) -> MiraState:
        """Handle decision logging"""
        system_prompt = f"""
You are MIRA's decision agent. Your job is to:
1. Extract the key decision from user input
2. Identify context and alternatives considered
3. Link to relevant projects/goals
4. Suggest a review date if appropriate

User Context:
{state['core_memory']}

Format the decision clearly and confirm with the user.
"""

        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['user_input']}
        ])

        # Store decision in archival memory
        self.archival.store_document(
            content=state['user_input'],
            doc_type="decision",
            source="user_input"
        )

        return {
            **state,
            "response": response,
            "actions_taken": [{"type": "decision_logged"}],
            "requires_confirmation": False
        }

    async def chat_agent(self, state: MiraState) -> MiraState:
        """Handle general conversation"""
        system_prompt = f"""
You are MIRA, a personal AI assistant. Be helpful, concise, and friendly.

User Context:
{state['core_memory']}

Retrieved Context:
{chr(10).join(state['retrieved_context'])}
"""

        response = llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": state['user_input']}
        ])

        return {
            **state,
            "response": response,
            "requires_confirmation": False
        }

    async def prepare_response(self, state: MiraState) -> MiraState:
        """Prepare final response for user"""
        import uuid

        return {
            **state,
            "interaction_id": str(uuid.uuid4())
        }

    async def _extract_entities(self, text: str) -> dict:
        """Extract entities from text"""
        prompt = f"""
Extract entities from this text:
"{text}"

Return JSON with:
- dates: list of dates mentioned (in YYYY-MM-DD format)
- people: list of people mentioned
- projects: list of projects mentioned
- times: list of times mentioned (in HH:MM format)
"""

        response = llm.chat([
            {"role": "system", "content": "Extract entities as JSON."},
            {"role": "user", "content": prompt}
        ])

        try:
            import json
            return json.loads(response)
        except:
            return {"dates": [], "people": [], "projects": [], "times": []}

    async def process_message(self, text: str, core_memory: CoreMemory) -> dict:
        """Process a user message through the graph"""
        initial_state = {
            "user_input": text,
            "input_type": "text",
            "core_memory": core_memory.to_prompt(),
            "retrieved_context": [],
            "intent": "",
            "entities": {},
            "response": "",
            "actions_taken": [],
            "requires_confirmation": False,
            "confirmation_prompt": "",
            "interaction_id": ""
        }

        # Run through graph
        config = {"configurable": {"thread_id": "main"}}
        result = await self.graph.ainvoke(initial_state, config)

        return {
            "message": result["response"],
            "action_taken": len(result["actions_taken"]) > 0,
            "id": result["interaction_id"],
            "requires_confirmation": result["requires_confirmation"],
            "confirmation_prompt": result["confirmation_prompt"]
        }

    async def process_quick_task(self, text: str, core_memory: CoreMemory) -> dict:
        """Quick task creation bypassing intent classification"""
        # Direct to task agent
        # ... implementation
        pass

    async def get_daily_briefing(self, core_memory: CoreMemory) -> dict:
        """Generate daily briefing"""
        # ... implementation
        pass

    async def generate_plan(self, core_memory: CoreMemory) -> dict:
        """Generate daily plan"""
        # ... implementation
        pass

    async def log_decision(self, text: str, core_memory: CoreMemory) -> dict:
        """Log a decision"""
        # ... implementation
        pass

    async def search_memory(self, query: str, core_memory: CoreMemory) -> list:
        """Search memory"""
        # ... implementation
        pass

    async def process_document(self, file_path: str, core_memory: CoreMemory) -> dict:
        """Process uploaded document"""
        # ... implementation
        pass

    async def transcribe_voice(self, voice_path: str) -> str:
        """Transcribe voice to text"""
        # For MVP: use Web Speech API on client side
        # Fallback: use Whisper API
        pass
```

### Day 11-12: Feedback & Learning System

**Implementation: `src/learning/feedback.py`**

```python
"""
Feedback Collection & Learning
"""

from datetime import datetime
from typing import Optional
import sqlite3
import json

class FeedbackCollector:
    def __init__(self, db_path: str = "data/mira.db"):
        self.db_path = db_path

    def record(
        self,
        interaction_id: str,
        feedback_type: str,  # thumbs_up, thumbs_down, correction
        original_suggestion: str = "",
        user_correction: str = "",
        category: str = ""
    ):
        """Record feedback for an interaction"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO feedback_log
            (interaction_id, feedback_type, original_suggestion, user_correction, category, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            interaction_id,
            feedback_type,
            original_suggestion,
            user_correction,
            category,
            datetime.now().isoformat()
        ))

        conn.commit()
        conn.close()

        # Trigger learning if needed
        if feedback_type in ["thumbs_down", "correction"]:
            self._trigger_learning(interaction_id, category, user_correction)

    def _trigger_learning(self, interaction_id: str, category: str, correction: str):
        """Update patterns based on feedback"""
        # This is called when user provides negative feedback
        # We update the pattern_log to remember the correction
        pass

    def get_accuracy_stats(self, category: Optional[str] = None, days: int = 30) -> dict:
        """Get feedback statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = """
            SELECT
                feedback_type,
                COUNT(*) as count
            FROM feedback_log
            WHERE created_at > datetime('now', ?)
        """
        params = [f'-{days} days']

        if category:
            query += " AND category = ?"
            params.append(category)

        query += " GROUP BY feedback_type"

        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        stats = {r[0]: r[1] for r in results}

        total = sum(stats.values())
        positive = stats.get('thumbs_up', 0)

        return {
            "total_interactions": total,
            "positive": positive,
            "negative": stats.get('thumbs_down', 0),
            "corrections": stats.get('correction', 0),
            "accuracy_rate": positive / total if total > 0 else 0
        }


class PatternLearner:
    """Learn patterns from user behavior"""

    def __init__(self, db_path: str = "data/mira.db"):
        self.db_path = db_path

    def learn_time_estimation(self, task_type: str, estimated: int, actual: int):
        """Learn from time estimation accuracy"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        pattern_key = f"time_estimation_{task_type}"

        # Get existing pattern
        cursor.execute(
            "SELECT pattern_value, sample_count FROM pattern_log WHERE pattern_key = ?",
            (pattern_key,)
        )
        result = cursor.fetchone()

        if result:
            data = json.loads(result[0])
            sample_count = result[1]

            # Update running average of estimation accuracy
            ratio = actual / estimated if estimated > 0 else 1
            data['avg_ratio'] = (data['avg_ratio'] * sample_count + ratio) / (sample_count + 1)
            data['samples'].append({'estimated': estimated, 'actual': actual})
            data['samples'] = data['samples'][-50:]  # Keep last 50

            cursor.execute("""
                UPDATE pattern_log
                SET pattern_value = ?, sample_count = sample_count + 1, last_updated = ?
                WHERE pattern_key = ?
            """, (json.dumps(data), datetime.now().isoformat(), pattern_key))
        else:
            # Create new pattern
            data = {
                'avg_ratio': actual / estimated if estimated > 0 else 1,
                'samples': [{'estimated': estimated, 'actual': actual}]
            }
            cursor.execute("""
                INSERT INTO pattern_log (pattern_type, pattern_key, pattern_value, sample_count, last_updated)
                VALUES (?, ?, ?, ?, ?)
            """, ('time_estimation', pattern_key, json.dumps(data), 1, datetime.now().isoformat()))

        conn.commit()
        conn.close()

    def get_time_multiplier(self, task_type: str) -> float:
        """Get learned time multiplier for a task type"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT pattern_value FROM pattern_log WHERE pattern_key = ?",
            (f"time_estimation_{task_type}",)
        )
        result = cursor.fetchone()
        conn.close()

        if result:
            data = json.loads(result[0])
            return data.get('avg_ratio', 1.0)

        return 1.0  # Default: no adjustment

    def detect_recurring_tasks(self) -> list:
        """Detect tasks that occur regularly"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Find tasks with similar titles that repeat weekly
        cursor.execute("""
            SELECT
                title,
                COUNT(*) as occurrences,
                GROUP_CONCAT(strftime('%w', created_at)) as weekdays
            FROM tasks
            WHERE created_at > datetime('now', '-30 days')
            GROUP BY title
            HAVING COUNT(*) >= 3
        """)

        results = cursor.fetchall()
        conn.close()

        recurring = []
        for title, count, weekdays in results:
            weekday_list = weekdays.split(',')
            # Check if same weekday appears multiple times
            from collections import Counter
            weekday_counts = Counter(weekday_list)
            most_common = weekday_counts.most_common(1)[0]

            if most_common[1] >= 2:  # Same weekday at least twice
                recurring.append({
                    'title': title,
                    'suggested_day': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][int(most_common[0])],
                    'confidence': most_common[1] / count
                })

        return recurring

    def learn_energy_pattern(self, hour: int, productivity_score: int):
        """Learn energy patterns by hour"""
        # Similar implementation to time estimation
        pass

    def get_best_hours_for_task(self, task_type: str) -> list:
        """Get best hours for a task type based on learned patterns"""
        # Returns list of hours sorted by productivity
        pass
```

### Day 13-14: Onboarding, Backup & Polish

**Implementation: `scripts/onboarding.py`**

```python
"""
Onboarding Wizard - Collect initial knowledge from user
"""

ONBOARDING_QUESTIONS = [
    {
        "id": "name",
        "question": "What should I call you?",
        "type": "text",
        "storage": "user_profile.name"
    },
    {
        "id": "timezone",
        "question": "What's your timezone? (e.g., Asia/Kolkata)",
        "type": "text",
        "default": "Asia/Kolkata",
        "storage": "user_profile.timezone"
    },
    {
        "id": "projects",
        "question": """Tell me about your main projects/areas of work.

For example:
- Amolee (jewelry startup, launching Jan 2025)
- Final year coursework at IIT Kanpur
- Job preparation

List your projects, one per line:""",
        "type": "multiline",
        "storage": "projects"
    },
    {
        "id": "goals",
        "question": """What are your top 3 goals for the next 3 months?

For example:
1. Launch Amolee website successfully
2. Complete B.Tech project
3. Secure AI/ML job offer

List your goals:""",
        "type": "multiline",
        "storage": "goals"
    },
    {
        "id": "people",
        "question": """Who are the key people you work with?

For example:
- Prof. Kothari (project supervisor, prefers detailed updates)
- [Co-founder name] (Amolee partner)

List key people with any important notes:""",
        "type": "multiline",
        "storage": "people"
    },
    {
        "id": "work_hours",
        "question": "When do you usually work? (e.g., 9 AM - 11 PM)",
        "type": "text",
        "storage": "preferences.work_hours"
    },
    {
        "id": "peak_energy",
        "question": "When do you have the most energy/focus? (e.g., morning, evening)",
        "type": "text",
        "storage": "preferences.peak_energy"
    },
    {
        "id": "communication",
        "question": "How should I communicate with you? (concise / detailed / casual)",
        "type": "choice",
        "options": ["concise", "detailed", "casual"],
        "storage": "preferences.communication_style"
    }
]

DOCUMENT_PROMPTS = [
    {
        "id": "notion_export",
        "prompt": """📚 **Document Upload (Optional)**

If you have existing project notes or Notion exports, you can upload them now.

Send any documents (PDF, images, text files) that would help me understand your work better.

Or send /skip to continue without uploading.""",
        "type": "document"
    }
]
```

**Implementation: `src/utils/backup.py`**

```python
"""
Backup System - Daily backup to Google Drive
"""

import sqlite3
import shutil
import os
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class BackupManager:
    def __init__(self, db_path: str = "data/mira.db"):
        self.db_path = db_path
        self.backup_dir = "data/backups"
        os.makedirs(self.backup_dir, exist_ok=True)

    def create_local_backup(self) -> str:
        """Create local backup of database"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{self.backup_dir}/mira_backup_{timestamp}.db"

        # Copy SQLite database
        shutil.copy2(self.db_path, backup_path)

        # Also backup LanceDB
        lancedb_backup = f"{self.backup_dir}/lancedb_backup_{timestamp}"
        shutil.copytree("data/lancedb", lancedb_backup)

        return backup_path

    def upload_to_drive(self, backup_path: str, drive_folder_id: str) -> bool:
        """Upload backup to Google Drive"""
        try:
            creds = Credentials.from_authorized_user_file('credentials/google_token.json')
            service = build('drive', 'v3', credentials=creds)

            file_metadata = {
                'name': os.path.basename(backup_path),
                'parents': [drive_folder_id]
            }
            media = MediaFileUpload(backup_path, resumable=True)

            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()

            return True
        except Exception as e:
            print(f"Backup upload failed: {e}")
            return False

    def cleanup_old_backups(self, keep_days: int = 7):
        """Remove local backups older than X days"""
        cutoff = datetime.now().timestamp() - (keep_days * 24 * 60 * 60)

        for filename in os.listdir(self.backup_dir):
            filepath = os.path.join(self.backup_dir, filename)
            if os.path.getmtime(filepath) < cutoff:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                else:
                    shutil.rmtree(filepath)

    def run_daily_backup(self, drive_folder_id: str):
        """Run complete daily backup routine"""
        # Create local backup
        backup_path = self.create_local_backup()

        # Upload to Drive
        success = self.upload_to_drive(backup_path, drive_folder_id)

        # Log result
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO backup_log (backup_type, backup_location, status, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            'daily',
            backup_path,
            'success' if success else 'failed',
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()

        # Cleanup old local backups
        self.cleanup_old_backups()

        return success
```

---

## Phase 2: Enhanced Features (Week 3-6)

### Week 3-4: Google Calendar & Notion Integration

**Tasks:**

- [ ] Set up Google Calendar MCP server
- [ ] Implement calendar event creation
- [ ] Implement free slot finding
- [ ] Set up Notion MCP server
- [ ] Implement Notion database sync
- [ ] Add calendar webhook for change detection

### Week 5-6: Weekly Review & Pattern Detection

**Tasks:**

- [ ] Implement weekly summary generation
- [ ] Build pattern detection algorithms
- [ ] Add recurring task suggestions
- [ ] Implement time estimation learning
- [ ] Create goal alignment check

**Implementation: Weekly Review System**

```python
class WeeklyReview:
    def generate_review(self, user_id: int) -> dict:
        """Generate weekly review for Sunday evening"""

        # Tasks completed vs planned
        tasks_stats = self._get_task_stats()

        # Time spent by project
        project_time = self._get_project_time()

        # Patterns detected
        patterns = self._detect_patterns()

        # Goal progress
        goal_progress = self._check_goal_alignment()

        # Suggestions for next week
        suggestions = self._generate_suggestions()

        return {
            "summary": self._format_summary(tasks_stats, project_time),
            "patterns": patterns,
            "goal_progress": goal_progress,
            "suggestions": suggestions,
            "questions": [
                "How was your energy this week? (1-5)",
                "Any tasks that should become recurring?",
                "What should be different next week?"
            ]
        }
```

---

## Phase 3: Advanced Features (Month 2-3)

### Month 2: Goal Tracking & Proactive Alerts

**Features:**

- Goal hierarchy (Vision → Yearly → Quarterly → Monthly)
- Progress tracking
- Deadline risk detection
- Meeting prep automation

### Month 3: Multi-Project Coordination

**Features:**

- Project switching detection
- Context-aware suggestions
- Interview prep mode
- Energy-based scheduling

---

## Risk Mitigation

### Built-in Safeguards

| Risk                 | Mitigation            | Implementation                                  |
| -------------------- | --------------------- | ----------------------------------------------- |
| **LLM wrong output** | Confirmation required | `requires_confirmation` flag in agent responses |
| **Data loss**        | Daily backups         | `BackupManager.run_daily_backup()` scheduled    |
| **DeepSeek down**    | Gemini fallback       | `LLMProvider` auto-switches on failure          |
| **Rate limits**      | Request queuing       | `RateLimiter` class with wait_if_needed()       |
| **API key exposure** | Environment variables | `.env` file, never commit keys                  |
| **Over-reliance**    | Suggestions only      | All actions require user confirmation initially |
| **Stop using**       | Reminders             | Check last activity, send reminder after 7 days |

### Confirmation Levels

```python
class ConfirmationLevel:
    NONE = 0        # Just respond, no confirmation
    INFORM = 1      # Inform user of action taken
    CONFIRM = 2     # Ask before executing
    STRICT = 3      # Require explicit approval for each action

# Default levels by action type
ACTION_CONFIRMATION = {
    'create_task': ConfirmationLevel.INFORM,
    'update_task': ConfirmationLevel.INFORM,
    'delete_task': ConfirmationLevel.CONFIRM,
    'create_calendar_event': ConfirmationLevel.CONFIRM,
    'update_calendar_event': ConfirmationLevel.CONFIRM,
    'delete_calendar_event': ConfirmationLevel.STRICT,
    'create_notion_page': ConfirmationLevel.INFORM,
    'update_notion_page': ConfirmationLevel.CONFIRM,
    'log_decision': ConfirmationLevel.INFORM,
    'learn_pattern': ConfirmationLevel.NONE
}
```

---

## Budget Breakdown

| Component                              | Monthly Cost      |
| -------------------------------------- | ----------------- |
| Claude Pro (your personal use)         | ₹1,670 ($20)      |
| DeepSeek V3.2 API (~500K tokens/month) | ₹350 (~$4)        |
| Gemini Flash (fallback, ~100K tokens)  | ₹100 (~$1)        |
| Google Cloud (Calendar/Drive API)      | ₹0 (free tier)    |
| Hosting (Vercel/Railway free tier)     | ₹0                |
| **Total**                              | **₹2,120 (~$25)** |

---

## Success Metrics

### Week 2 (MVP Complete)

- [ ] Can capture tasks via voice and text
- [ ] Morning briefing works daily
- [ ] Basic memory retrieval works
- [ ] Feedback system collecting data

### Week 4 (Phase 1 Complete)

- [ ] Calendar integration working
- [ ] Notion sync working
- [ ] Onboarding wizard complete
- [ ] Daily backups running

### Month 2 (Phase 2 Complete)

- [ ] Pattern detection showing results
- [ ] Time estimation learning working
- [ ] Weekly review generating insights
- [ ] 80%+ feedback accuracy

### Month 3 (Phase 3 Started)

- [ ] Goal tracking active
- [ ] Proactive alerts working
- [ ] Multi-project coordination helpful

---

## Quick Reference: Daily Commands

```
/q <task>          Quick task capture
/today             Today's briefing
/plan              Generate daily plan
/decide <text>     Log a decision
/remember <query>  Search memory
/export            Export data
/feedback          View accuracy stats
/help              Show all commands

---

**Document Version:** 1.0
**Created:** December 2024
**Author:** Claude (for Sahil)
**Project:** MIRA - Memory-Intelligent Routine Assistant
```
