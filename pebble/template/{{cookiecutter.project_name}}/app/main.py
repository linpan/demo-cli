from datetime import datetime
import uvicorn as uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy import text
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware
from loguru import logger
from fastapi.exceptions import RequestValidationError
from api.endpoints.api import api_router as api_router_v1
from app.utils.validation_error import APIValidationError

{%- if cookiecutter.enable_kafka == "True" %}
from app.utils.kafka_producerimport start_kafka, shutdown_kafka
{%- endif %}

{%- if (cookiecutter.orm == "tortoise") or (cookiecutter.orm == "beanie") %}
from app.db.init_db import get_db
{%- endif %}

{%- if cookiecutter.orm == "mongo" %}
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection
{%- endif %}

import sentry_sdk

from core.config import settings
from app.db.session import get_session

from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration


{%- if cookiecutter.enable_sentry == "True" %}
sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    traces_sample_rate=1.0,
    integrations=[
        StarletteIntegration(transaction_style="endpoint"),
        FastApiIntegration(transaction_style="endpoint"),
    ],
)
{%- endif %}


# Core Application Instance
app = FastAPI(
    default_response_class=ORJSONResponse,
)


@app.get("/demo", tags=["health"])
async def demo(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("select * from user"))
    await session.commit()
    print(result.fetchall())
    return 1


@app.get("/health", tags=["health"])
def healthcheck():
    return {"message": "ok", "timestamp": datetime.now().isoformat()}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routers
app.include_router(api_router_v1, prefix=settings.API_V1_STR)


# todo  if settings.USE_CORRELATION_ID:

@app.on_event("startup")
async def on_startup():

    logger.info("Application Started")
    {%- if (cookiecutter.orm == "tortoise") or (cookiecutter.orm == "beanie") %}
    await get_db()
    {%- endif %}

    {%- if cookiecutter.orm == "mongo" %}
    await connect_to_mongo()
    {%- endif %}

    {%- if cookiecutter.enable_kafka == "True" %}
    await start_kafka(app)
    {%- endif %}



@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Application Shutdown")
    {%- if cookiecutter.orm == "mongo" %}
    await close_mongo_connection()
    {%- endif %}

    {%- if cookiecutter.enable_kafka == "True" %}
    await shutdown_kafka()
    {%- endif %}

    {%- if cookiecutter.enable_redis == "True" %}
    await shutdown_redis(app)
    {%- endif %}

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(
    _,
    exc: RequestValidationError,
) -> ORJSONResponse:
    return ORJSONResponse(
        content=APIValidationError.from_pydantic(exc).dict(exclude_none=True),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5555)
