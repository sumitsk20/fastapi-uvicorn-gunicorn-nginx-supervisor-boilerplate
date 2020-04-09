import logging
import sys
from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret


config = Config(".env")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config(
    "SECRET_KEY", default="UBzPj7Qj29K4z4aeCqZ40xi8dVdTbbch", cast=Secret
)
PROJECT_NAME: str = config("PROJECT_NAME", default="Ghoom Analytics")
VERSION: str = config("VERSION", default="1.0.0")
MONGO_URI: str = config("MONGO_URI", default="mongodb://127.0.0.1:27017")
MONGO_DB_NAME: str = config("MONGO_DB_NAME", default="demo_db")
MONGO_MAX_POOL_SIZE: int = config("MONGO_MAX_POOL_SIZE", default=2)
MONGO_MIN_POOL_SIZE: int = config("MONGO_MIN_POOL_SIZE", default=15)
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
# logging.basicConfig(
#     handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
# )
# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
