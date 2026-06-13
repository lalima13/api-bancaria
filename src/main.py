from fastapi import FastAPI





app = FastAPI(
    title="Transactions API",
    version="1.0",
    summary="Microservice to maintain withdral and deposit operations from current account"
) 