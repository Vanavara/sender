# stdlib
import logging

# thirdparty
import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from starlette.responses import RedirectResponse

# project
import settings
from routers.broadcast import broadcast_router
from routers.client import client_router
from routers.message import message_router

# Define a root router
root_router = APIRouter(prefix="/api/v1")

# Define an admin router
admin_router = APIRouter(prefix="/admin")

# Define a media router
media_router = APIRouter(prefix="/media")

# Define a FastAPI application
app = FastAPI(title="Sender API", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========ROUTER REGISTRATION===========#

# 1. CLIENT
root_router.include_router(client_router)
# 2. BROADCAST
root_router.include_router(broadcast_router)
# # 3. MESSAGE
root_router.include_router(message_router)

# Connect admin sub-routers to admin router
root_router.include_router(admin_router)

# Connect a root router to an application
app.include_router(root_router)
app.include_router(media_router)


# Redirect root URL to /docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /metrics") == -1


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


def openapi_specs():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Sender",
        version="0.0.1",
        description="Sender Open-API Specification",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_specs


if __name__ == "__main__":
    # update uvicorn access logger format
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = (
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] "
        "[trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s"
    )
    uvicorn.run(app, host="0.0.0.0", port=8001, log_config=log_config)
