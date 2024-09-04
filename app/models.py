from pydantic import BaseModel


class MemoryInfo(BaseModel):
    id: int
    timestamp: int
    total: int
    free: int
    used: int

    class Config:
        from_attributes = True
