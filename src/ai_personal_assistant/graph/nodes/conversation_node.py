from ai_personal_assistant.graph.state import AIPersonalAssistantState
from ai_personal_assistant.graph.utils.chains import get_character_response_chain
from langchain_core.messages import AIMessage


async def conversation_node(state: AIPersonalAssistantState, config: RunnableConfig):
    current_activity = ScheduleContextGenerator.get_current_activity()
    memory_context = state.get("memory_context", "")

    chain = get_character_response_chain(state.get("summary", ""))

    response = await chain.ainvoke(
        {
            "messages": state["messages"],
            "current_activity": current_activity,
            "memory_context": memory_context,
        },
        config,
    )
    return {"messages": HumanMe(content=response)}
