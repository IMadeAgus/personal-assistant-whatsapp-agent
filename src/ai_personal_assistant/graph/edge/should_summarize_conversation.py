from typing import Literal

from ai_personal_assistant.settings import settings
from ai_personal_assistant.graph.state import AIPersonalAssistantState


def should_summarize_conversation(
    state: AIPersonalAssistantState,
) -> Literal["summarize_conversation_node", "__end__"]:
    messages = state["messages"]

    if len(messages) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"

    return "__end__"
