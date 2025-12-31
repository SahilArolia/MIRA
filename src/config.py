"""
MIRA Configuration Management
Loads settings from .env file and provides app-wide config
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""

    # Project paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    BACKUP_DIR = DATA_DIR / "backups"
    TEMP_DIR = DATA_DIR / "temp"

    # Database
    DATABASE_PATH = os.getenv("DATABASE_PATH", "data/mira.db")
    LANCEDB_PATH = os.getenv("LANCEDB_PATH", "data/lancedb")

    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # LLM APIs
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # App Settings
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Rate Limits
    DEEPSEEK_CALLS_PER_MINUTE = int(os.getenv("DEEPSEEK_CALLS_PER_MINUTE", "60"))
    GEMINI_CALLS_PER_MINUTE = int(os.getenv("GEMINI_CALLS_PER_MINUTE", "60"))

    @classmethod
    def validate(cls):
        """Validate that required config is present"""
        errors = []

        if not cls.TELEGRAM_BOT_TOKEN:
            errors.append("TELEGRAM_BOT_TOKEN not set")
        if not cls.DEEPSEEK_API_KEY:
            errors.append("DEEPSEEK_API_KEY not set")
        if not cls.GEMINI_API_KEY:
            errors.append("GEMINI_API_KEY not set")

        if errors:
            raise ValueError(f"Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors))

        return True

    @classmethod
    def setup_directories(cls):
        """Create necessary directories"""
        cls.DATA_DIR.mkdir(exist_ok=True)
        cls.BACKUP_DIR.mkdir(exist_ok=True)
        cls.TEMP_DIR.mkdir(exist_ok=True)

# Create config instance
config = Config()
