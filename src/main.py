import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import config

def main():
    """Main application entry point"""

    print("MIRA - Memory-Intelligent Routine Assistant")
    print("=" * 50)

    # Validate configuration
    try:
        config.validate()
        print("✅ Configuration validated")
    except ValueError as e:
        print(f"❌ Configuration error:\n{e}")
        print("\nPlease check your .env file and ensure all required keys are set.")
        return 1

    # Setup directories
    config.setup_directories()
    print("✅ Directories ready")

    # Check database
    if not Path(config.DATABASE_PATH).exists():
        print("\n⚠️  Database not found!")
        print("Please run: python scripts/setup_database.py")
        return 1

    print("✅ Database found")

    print("\n" + "=" * 50)
    print("MIRA is starting...")
    print("=" * 50 + "\n")

    # TODO: Initialize and start bot
    # from src.bot.handlers import MiraBot
    # bot = MiraBot()
    # bot.run()

    print("⚠️  Bot implementation not complete yet")
    print("\nNext steps:")
    print("1. Implement src/memory/core_memory.py (Day 3-4)")
    print("2. Implement src/integrations/llm.py (Day 5-6)")
    print("3. Implement src/bot/handlers.py (Day 7-8)")
    print("4. Implement src/agents/graph.py (Day 9-10)")

    return 0

if __name__ == "__main__":
    sys.exit(main())
