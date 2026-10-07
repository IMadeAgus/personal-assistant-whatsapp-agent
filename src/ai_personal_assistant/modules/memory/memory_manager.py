from gotrue import Optional
from pydantic import BaseModel, Field


class MemoryAnalysis(BaseModel):
    """Result of analyzing a message for memory-worthy content."""

    is_important: bool = Field(
        ...,
        description="Whether the message is important enough to be stored as a memory",
    )
    formatted_memory: Optional[str] = Field(..., description="The formatted memory to be stored")


class MemoryManager:

    def __init__(self):
        self.vector_store = get_vector_store()
        
        