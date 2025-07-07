import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/metrics")
async def metrics():
    return {
        "cpu": random.randint(10, 90),
        "mem": f"{random.randint(20, 80)}%",
        "disk": f"{random.randint(30, 70)}%",
        "uptime": f"{random.randint(0, 5)}d "
        f"{random.randint(0, 23)}h "
        f"{random.randint(0, 59)}m "
        f"{random.randint(0, 59)}s",
    }
