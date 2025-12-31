# MIRA: Memory-Intelligent Routine Assistant

Personal AI productivity assistant that learns your patterns and helps manage tasks, calendar, and decisions.

## Quick Start

### 1. Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```
# Edit .env and add your API keys:
# - TELEGRAM_BOT_TOKEN (from @BotFather)
# - DEEPSEEK_API_KEY
# - GEMINI_API_KEY
```

### 4. Initialize Database

```bash
python scripts/setup_database.py
```

### 5. Run MIRA

```bash
python src/main.py
```

## Project Structure

```
mira-assistant/
├── src/
│   ├── bot/          # Telegram bot handlers
│   ├── agents/       # LangGraph agents
│   ├── memory/       # Smriti memory system
│   ├── integrations/ # External services
│   ├── learning/     # Pattern detection
│   └── utils/        # Database, backup, etc.
├── data/
│   ├── mira.db       # SQLite database
│   ├── lancedb/      # Vector store
│   └── backups/      # Local backups
├── scripts/          # Setup and utility scripts
└── tests/            # Test files
```

## Telegram Commands

- `/start` - Welcome and onboarding
- `/q <task>` - Quick task capture
- `/today` - Daily briefing
- `/plan` - Generate daily plan
- `/decide <decision>` - Log important decision
- `/remember <query>` - Search memory
- `/export` - Export your data
- `/help` - Show all commands

## Development Status

**Phase 1 MVP (Days 1-14)**: In Progress

- [x] Project setup
- [x] Virtual environment
- [x] Database schema
- [ ] Core memory system
- [ ] LLM integration
- [ ] Telegram bot
- [ ] Basic agents
- [ ] Feedback system

## Tech Stack

- **Bot**: python-telegram-bot
- **Agents**: LangGraph
- **LLMs**: DeepSeek V3.2 (primary), Gemini Flash (fallback)
- **Memory**: LanceDB (vector) + SQLite (structured)
- **Embeddings**: sentence-transformers

## License

Personal project - not for distribution

---

Built by Sahil | Started January 2025
