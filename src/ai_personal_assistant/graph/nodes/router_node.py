from ai_personal_assistant.graph.state import AIPersonalAssistantState
from ai_personal_assistant.graph.utils.chains import get_router_chain


async def router_node(state: AIPersonalAssistantState):
    chain = get_router_chain()
    response = await chain.ainvoke(
        {"messages": state["messages"][-settings.ROUTER_MESSAGES_TO_ANALYZE :]}
    )
    return {"workflow": response.response_type}
