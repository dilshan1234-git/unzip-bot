# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    API_ID = int(os.environ.get("API_ID", "14631157"))
    API_HASH = os.environ.get("API_HASH", "aa7c2b3be68a7488abdb9de6ce78d311")
    BOT_TOKEN = os.environ.get("6880188560:AAHpk9t0uWT1CURv7NqJIJCZ3XsPyywGc8E")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002106332206")
    MONGODB_URL = os.environ.get("mongodb+srv://dilfilter123:dilfilter123@cluster0.tq9uv2k.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5380833276"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
