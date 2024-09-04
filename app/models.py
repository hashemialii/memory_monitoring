from pydantic import BaseModel


class MemoryInfo(BaseModel):
    id: int
    timestamp: str
    total: int
    free: int
    used: int

    class Config:
        from_attributes = True

