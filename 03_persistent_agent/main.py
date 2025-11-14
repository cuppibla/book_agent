import os
from pathlib import Path
from google.adk.sessions import DatabaseSessionService

# --- Configuration for Persistent Sessions ---
SESSIONS_DIR = Path(os.path.expanduser("~")) / ".adk_codelab" / "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)
SESSION_DB_FILE = SESSIONS_DIR / "trip_planner.db"
SESSION_URL = f"sqlite:///{SESSION_DB_FILE}"

session_service = DatabaseSessionService(db_url=SESSION_URL)

# REPLACE THIS:
session = await session_service.create_session(app_name=root_agent.name, user_id="user_01")
print(f"--- Session-Aware Trip Planner (Session ID: {session.id}) ---")
print("Agent: Hello! Let's plan a trip. Where to?")

# WITH THIS:
session_id = "my_persistent_trip" # A fixed ID for our trip
session = await session_service.get_session(
    app_name=root_agent.name, user_id="user_01", session_id=session_id
)
if session:
    print(f"Agent: Welcome back! Resuming our trip planning session ({session_id}).")
else:
    print(f"Agent: Hello! Let's start planning a new trip ({session_id}). Where to?")
    session = await session_service.create_session(
        app_name=root_agent.name, user_id="user_01", session_id=session_id
    )
print(f"--- Persistent Trip Planner ---")