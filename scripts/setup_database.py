import sqlite3
import os

def create_database(db_path: str = "data/mira.db"):
    # 1. Ensure directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # We add 'PRAGMA' commands to optimize engine performance
    schema_script = """
    -- Performance & Integrity Settings
    PRAGMA journal_mode = WAL;
    PRAGMA foreign_keys = ON;

    -- TABLES
    CREATE TABLE IF NOT EXISTS user_profile (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        timezone TEXT DEFAULT 'Asia/Kolkata',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'active',
        priority INTEGER DEFAULT 5,
        deadline DATE,
        parent_project_id INTEGER REFERENCES projects(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        goal_type TEXT NOT NULL,
        target_date DATE,
        progress_percentage INTEGER DEFAULT 0,
        project_id INTEGER REFERENCES projects(id),
        parent_goal_id INTEGER REFERENCES goals(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending',
        priority TEXT DEFAULT 'medium',
        estimated_minutes INTEGER,
        actual_minutes INTEGER,
        due_date DATE,
        due_time TIME,
        project_id INTEGER REFERENCES projects(id),
        goal_id INTEGER REFERENCES goals(id),
        recurring_pattern TEXT,
        depends_on_task_id INTEGER REFERENCES tasks(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP,
        created_from TEXT
    );

    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        relationship TEXT,
        organization TEXT,
        email TEXT,
        phone TEXT,
        preferences TEXT,
        notes TEXT,
        project_ids TEXT, -- Consider a junction table for better normalization later
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        context TEXT,
        alternatives_considered TEXT,
        outcome TEXT,
        project_id INTEGER REFERENCES projects(id),
        people_involved TEXT,
        decision_date DATE NOT NULL,
        review_date DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS feedback_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        interaction_id TEXT NOT NULL,
        feedback_type TEXT NOT NULL,
        original_suggestion TEXT,
        user_correction TEXT,
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS pattern_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pattern_type TEXT NOT NULL,
        pattern_key TEXT NOT NULL,
        pattern_value TEXT NOT NULL,
        confidence_score REAL DEFAULT 0.5,
        sample_count INTEGER DEFAULT 1,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS time_blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER REFERENCES tasks(id),
        calendar_event_id TEXT,
        start_time TIMESTAMP NOT NULL,
        end_time TIMESTAMP NOT NULL,
        block_type TEXT DEFAULT 'task',
        status TEXT DEFAULT 'scheduled',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS daily_summaries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE UNIQUE NOT NULL,
        tasks_completed INTEGER DEFAULT 0,
        tasks_created INTEGER DEFAULT 0,
        focus_minutes INTEGER DEFAULT 0,
        meetings_count INTEGER DEFAULT 0,
        energy_rating INTEGER,
        productivity_rating INTEGER,
        summary_text TEXT,
        patterns_detected TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS system_config (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS backup_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        backup_type TEXT NOT NULL,
        backup_location TEXT NOT NULL,
        file_size_bytes INTEGER,
        status TEXT DEFAULT 'success',
        error_message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- INDEXES (Crucial for O(log n) search speed)
    CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
    CREATE INDEX IF NOT EXISTS idx_tasks_due_date ON tasks(due_date);
    CREATE INDEX IF NOT EXISTS idx_tasks_project ON tasks(project_id);
    CREATE INDEX IF NOT EXISTS idx_decisions_project ON decisions(project_id);
    CREATE INDEX IF NOT EXISTS idx_feedback_category ON feedback_log(category);
    CREATE INDEX IF NOT EXISTS idx_pattern_type ON pattern_log(pattern_type);
    CREATE INDEX IF NOT EXISTS idx_conversations_session ON conversations(session_id);
    CREATE INDEX IF NOT EXISTS idx_daily_summaries_date ON daily_summaries(date);
    """

    try:
        # 3. Use Context Manager for safety
        with sqlite3.connect(db_path) as conn:
            conn.executescript(schema_script)
            print(f"✅ Database built successfully at: {db_path}")
            print("✅ Performance mode: WAL enabled")
            
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    create_database()