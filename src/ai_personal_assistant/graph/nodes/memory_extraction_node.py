from ai_personal_assistant.graph.state import AIPersonalAssistantState
from ai_personal_assistant.modules.memory.long_term.memory_manager import (
    get_memory_manager,
)


async def memory_extraction_node(state: AIPersonalAssistantState):
    """Extract and store important information from the last message"""
    if not state["messages"]:
        return {}

    memory_manager = get_memory_manager()
    await memory_manager.extract_and_store_memories(state["messages"][-1])
    return {}
