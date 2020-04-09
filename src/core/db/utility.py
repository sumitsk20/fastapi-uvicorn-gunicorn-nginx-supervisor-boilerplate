from fastapi import FastAPI
from core.db.mongodb import MongoDBClient
import asyncio


def get_client():
    event_loop = asyncio.get_running_loop()
    client = MongoDBClient(event_loop)
    return client


def get_connection():
    client = get_client()
    return client.conn


def get_db():
    client = get_client()
    return client.conn.db


async def setup_database_connection(application: FastAPI) -> None:
    client = get_client()
    application.conn = client.conn


async def close_database_connection() -> None:
    client = get_client()
    client.conn.closeConnection()
