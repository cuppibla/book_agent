# --- A Helper Function to Run Our Agents ---
# We'll use this function throughout the notebook to make running queries easy.

async def run_agent_query(agent: Agent, query: str, session: Session, user_id: str, is_router: bool = False):
    """Initializes a runner and executes a query for a given agent and session."""
    print(f"\n🚀 Running query for agent: '{agent.name}' in session: '{session.id}'...")

    runner = Runner(
        agent=agent,
        session_service=session_service,
        app_name=agent.name
    )

    final_response = ""
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=Content(parts=[Part(text=query)], role="user")
        ):
            if not is_router:
                # Let's see what the agent is thinking!
                print(f"EVENT: {event}")
            if event.is_final_response():
                final_response = event.content.parts[0].text
    except Exception as e:
        final_response = f"An error occurred: {e}"

    if not is_router:
     print("\n" + "-"*50)
     print("✅ Final Response:")
     display(Markdown(final_response))
     print("-"*50 + "\n")

    return final_response

# --- Initialize our Session Service ---
# This one service will manage all the different sessions in our notebook.
session_service = InMemorySessionService()
my_user_id = "adk_adventurer_001"

# --- Scenario 2: Testing Adaptation and Memory ---

async def run_adaptive_memory_demonstration():
    print("### 🧠 DEMO 2: AGENT THAT ADAPTS (SAME SESSION) ###")

    # Create ONE session that we will reuse for the whole conversation
    trip_session = await session_service.create_session(
        app_name=multi_day_agent.name,
        user_id=my_user_id
    )
    print(f"Created a single session for our trip: {trip_session.id}")

    # --- Turn 1: The user initiates the trip ---
    query1 = "Hi! I want to plan a 2-day trip to Lisbon, Portugal. I'm interested in historic sites and great local food."
    print(f"\n🗣️ User (Turn 1): '{query1}'")
    await run_agent_query(multi_day_agent, query1, trip_session, my_user_id)

    # --- Turn 2: The user gives FEEDBACK and asks for a CHANGE ---
    # We use the EXACT SAME `trip_session` object!
    query2 = "That sounds pretty good, but I'm not a huge fan of castles. Can you replace the morning activity for Day 1 with something else historical?"
    print(f"\n🗣️ User (Turn 2 - Feedback): '{query2}'")
    await run_agent_query(multi_day_agent, query2, trip_session, my_user_id)

    # --- Turn 3: The user confirms and asks to continue ---
    query3 = "Yes, the new plan for Day 1 is perfect! Please plan Day 2 now, keeping the food theme in mind."
    print(f"\n🗣️ User (Turn 3 - Confirmation): '{query3}'")
    await run_agent_query(multi_day_agent, query3, trip_session, my_user_id)

await run_adaptive_memory_demonstration()