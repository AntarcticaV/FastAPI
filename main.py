import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from fastapi import FastAPI
import uvicorn
from core.router import set_routers
from core import setting

from prisma import Prisma
from prisma.models import Product
import asyncio


app = FastAPI(title= "Learn FastAPI")


@app.on_event("startup")
async def startup():
    set_routers(app)


@app.on_event("shutdown")
async def shutdown():
    pass


if __name__ == "__main__":
    # uvicorn.run("main:app", port=setting.POST, host=setting.HOST, reload=True)
    pass

async def main():
    db = Prisma()
    await db.connect()
    print(await db.product.find_first(where={"id": 1}))
    products = await db.product.find_many()
    await db.disconnect()
    
asyncio.run(main())