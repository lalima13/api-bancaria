from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status


@asynccontextmanager
async def lifespan(app: FastAPI):
        await database.connect()
        yield
        await database.disconnect()


tags_metadata = [
        {
                "name": "auth",
                "description": "Operations for authentication.",            
        },
        {
                "name": "account",
                "description": "Operations to maintain accounts.",       
        },
        {
                "name": "transaction",
                "description": "Operations to maintain transactions.",        
        },
]            



app = FastAPI(
    title="Transactions API",
    version="1.0",
    summary="Microservice to maintain withdral and deposit operations from current account",
    description="Transactions API is the microservice for recording current account transactions.",
    openapi_tags="tags_metadata",
    redoc_url="None",
    lifespan=lifespan,
) 