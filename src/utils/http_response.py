from fastapi import status
from typing import Any
from fastapi.responses import StreamingResponse, JSONResponse, Response
import json
from bson.json_util import dumps
import orjson


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        try:
            return orjson.dumps(content, option=orjson.OPT_SERIALIZE_UUID)
        except orjson.JSONEncodeError as encode_error:
            raise encode_error
        except Exception as other_error:
            raise other_error


class SuccessResponse(ORJSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        new_content = {"statusCode": status.HTTP_200_OK, "data": content}
        return super().render(content=new_content)


class ErrorResponse(ORJSONResponse):
    media_type = "application/json"

    def render(
        self,
        error: Exception = None,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        message: str = "Bad Request",
    ) -> bytes:
        new_content = {
            "statusCode": status_code,
            "error": error,
            "message": message or error.message,
        }
        return super().render(content=new_content)
