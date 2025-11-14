async def run_sequential_workflow():
    """
    A simplified test function that directly invokes the SequentialAgent.
    """

    # The query contains all the information needed for the entire sequence.
    query = "Find me the best sushi restaurant in Palo Alto, and then tell me how to get there from the downtown Caltrain station."

    print(f"\n{'='*60}\n🗣️  Processing Query: '{query}'\n{'='*60}")
    print(f"🚀 Handing off the entire task to the '{find_and_navigate_agent.name}'...")

    # 1. Create a single session for our sequential agent
    # The session will manage the state (like the 'destination' variable) across the sub-agent calls.
    session = await session_service.create_session(app_name=find_and_navigate_agent.name, user_id=my_user_id)

    # 2. Run the query
    # The SequentialAgent will automatically:
    #   - Call foodie_agent with the query.
    #   - Take its output and save it to the state as `state['destination']`.
    #   - Call transportation_agent, injecting the destination into its prompt.
    #   - Stream the final response from the transportation_agent.
    await run_agent_query(find_and_navigate_agent, query, session, my_user_id)

    print(f"\n--- ✅ '{find_and_navigate_agent.name}' Workflow Complete ---")


# Execute the simplified test
await run_sequential_workflow()