import asyncio
from fastapi import FastAPI

from core import settings
from core.db.utility import setup_database_connection, close_database_connection
from core.middlewares.utility import setup_middlewares
from server.routes import setup_routes


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
    )

    @application.on_event("startup")
    async def handle_startup_events():
        await setup_database_connection(application)
        await setup_middlewares(application)
        await setup_routes(application)

    @application.on_event("shutdown")
    async def handle_shutdown_events():
        await close_database_connection()

    return application


app = get_application()
