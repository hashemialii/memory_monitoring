from fastapi import FastAPI, Query
from typing import List
from app.crud import get_last_n_records
from app.models import MemoryInfo
from app.database import create_tables

app = FastAPI()


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/memory/", response_model=List[MemoryInfo])
def read_memory_info(n: int = Query(10, description="Number of records to retrieve")):
    records = get_last_n_records(n)
    return [
        {
            "id": record[0],
            "timestamp": record[1],
            "total": record[2],
            "free": record[3],
            "used": record[4],
        }
        for record in records
    ]
