from fastapi import APIRouter, status
from core.db.utility import get_db
from utils.http_response import SuccessResponse

router = APIRouter()
db = get_db()


@router.post("/export-csv")
async def export_csv_handler():
    # call some service method here, write your business logic in service function
    return SuccessResponse({"hello": "world"})


@router.get("/get-collections")
async def get_collections():
    collections = await db.list_collections()
    content = list(collections)
    return SuccessResponse(content)
