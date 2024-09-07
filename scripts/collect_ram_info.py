# import time
# import psutil
# from app.crud import insert_memory_info
#
#
# def collect_ram_info():
#     while True:
#         memory = psutil.virtual_memory()
#         total = memory.total // (1024 ** 2)
#         free = memory.available // (1024 ** 2)
#         used = total - free
#         insert_memory_info(total, free, used)
#         time.sleep(2)
#
#
# if __name__ == "__main__":
#     collect_ram_info()


import asyncio
import psutil
from app.crud import insert_memory_info


async def collect_ram_info(sleep_duration):
    memory = psutil.virtual_memory()
    total = memory.total // (1024 ** 2)
    free = memory.available // (1024 ** 2)
    used = total - free
    insert_memory_info(total, free, used)
    await asyncio.sleep(sleep_duration)


async def run_continuous_collection(sleep_duration):
    while True:
        await collect_ram_info(sleep_duration)


