from ai_personal_assistant.graph.state import AICompanionState
from ai_personal_assistant.graph.utils.chains import (
    get_character_response_chain,
    get_router_chain,
)
from ai_personal_assistant.schedules.context_generation import ScheduleContextGenerator

from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage
from langchain_core.runnables import RunnableConfig


async def router_node(state: AICompanionState):
    chain = get_router_chain()
    response = await chain.ainvoke(
        {"messages": state["messages"][-settings.ROUTER_MESSAGES_TO_ANALYZE :]}
    )
    return {"workflow": response.response_type}


def context_injection_node(state: AICompanionState):
    schedule_context = ScheduleContextGenerator.get_current_activity()
    if schedule_context != state.get("current_activity", ""):
        apply_activity = True
    else:
        apply_activity = False
    return {"apply_activity": apply_activity, "current_activity": schedule_context}


async def conversation_node(state: AICompanionState, config: RunnableConfig):
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
    return {"messages": AIMessage(content=response)}
