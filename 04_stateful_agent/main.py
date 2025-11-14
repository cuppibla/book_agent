async def run_variety_test():
    print(f"\n{'='*60}\n🗓️ PLANNING A VARIED DAY IN KYOTO 🗓️\n{'='*60}")

    # 1. Create a session and initialize the state to None
    itinerary_session = await session_service.create_session(
        app_name=master_planner.name,
        user_id=my_user_id,
        state={"last_activity_type": "None"} # Initial state
    )

    # --- Turn 1: Morning ---
    query1 = "I'm in Kyoto. Plan a morning activity for me."
    print(f"\n🗣️ TURN 1 (Morning): '{query1}'")
    # Expected: It should likely choose a cultural activity (museum_expert) for Kyoto.
    await run_agent_query(master_planner, query1, itinerary_session, my_user_id)

    # --- Turn 2: Afternoon ---
    # It just did a museum. It MUST NOT do another one, even if Kyoto is famous for them.
    # It should switch to Food or Outdoor.
    query2 = "Great! Now plan an afternoon activity for me."
    print(f"\n🗣️ TURN 2 (Afternoon - Variety Check): '{query2}'")
    await run_agent_query(master_planner, query2, itinerary_session, my_user_id)

    print(f"\n{'='*60}\n🏁 PLANNING COMPLETE 🏁\n{'='*60}")

await run_variety_test()