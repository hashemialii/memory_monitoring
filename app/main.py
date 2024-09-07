# import threading
# from fastapi import FastAPI, Query
# from typing import List
# from app.models import MemoryInfo
# from app.database import create_tables
# from app.crud import get_last_n_records, clear_memory_info
# from scripts.collect_ram_info import collect_ram_info
#
#
# def lifespan():
#     clear_memory_info()
#     create_tables()      # Create tables again (if not already exists)
#     threading.Thread(target=collect_ram_info).start()
#
#
# app = FastAPI(on_startup=[lifespan])
#
#
# @app.get("/")
# def read_root():
#     return {
#         "message": [
#             "Welcome to the RAM monitoring API",
#             "If you would like to try it, visit:",
#             "http://127.0.0.1:8000/memory/?n=10"
#         ]
#     }
#
#
# # list comprehension
# @app.get("/memory/", response_model=List[MemoryInfo])
# def read_memory_info(n: int = Query(10, description="Number of records to retrieve")):
#     records = get_last_n_records(n)
#     return [
#         {
#             "id": record[0],
#             "timestamp": record[1],
#             "total": record[2],
#             "free": record[3],
#             "used": record[4],
#         }
#         for record in records
#     ]


import asyncio
from fastapi import FastAPI, Query
from typing import List
from app.models import MemoryInfo
from app.database import create_tables
from app.crud import get_last_n_records, clear_memory_info
from scripts.collect_ram_info import run_continuous_collection


def lifespan():
    clear_memory_info()
    create_tables()  # Create tables again (if not already exists)
    asyncio.create_task(run_continuous_collection(1))


app = FastAPI(on_startup=[lifespan])


@app.get("/")
def read_root():
    return {
        "message": [
            "Welcome to the RAM monitoring API",
            "If you would like to try it, visit:",
            "http://127.0.0.1:8000/memory/?n=10"
        ]
    }


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


