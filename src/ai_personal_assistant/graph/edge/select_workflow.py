from email import message
from typing import Literal

from ai_personal_assistant import settings
from ai_personal_assistant.graph.state import AIPersonalAssistantState


def select_workflow(
    state: AIPersonalAssistantState,
) -> Literal["conversation_node", "__end__"]:
    workflow = state["workflow"]

    if workflow == "message":
        return "conversation_node"

    else:
        return "__end__"
