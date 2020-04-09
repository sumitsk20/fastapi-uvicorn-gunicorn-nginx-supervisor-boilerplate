

async def setup_routes(application):
    from apps.csv_export_app.routes import router as csv_export_app_router
    application.include_router(csv_export_app_router, prefix="/api/v1", tags=["v1"])
