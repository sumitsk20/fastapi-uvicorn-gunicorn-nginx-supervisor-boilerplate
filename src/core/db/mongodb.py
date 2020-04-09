from motor.motor_asyncio import AsyncIOMotorClient
from core.settings import (
    MONGO_URI,
    MONGO_DB_NAME,
    MONGO_MAX_POOL_SIZE,
    MONGO_MIN_POOL_SIZE,
)
from bson.codec_options import CodecOptions


class MongoDBClient(object):
    """
    Singleton client for interacting with MongoDB.
    """

    __instance = None

    def __new__(cls, io_loop) -> "MongoDBClient":

        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.codec_options = CodecOptions(tz_aware=True)
            conn = AsyncIOMotorClient(
                MONGO_URI,
                minPoolSize=MONGO_MIN_POOL_SIZE,
                maxPoolSize=MONGO_MAX_POOL_SIZE,
                io_loop=io_loop,
            )
            conn.db = conn[MONGO_DB_NAME]
            cls.__instance.conn = conn
        return cls.__instance

    def closeConnection(self):
        try:
            self.conn.close()
        except Exception as e:
            raise e
