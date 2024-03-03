# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("14631157"))
    API_HASH = os.environ.get("aa7c2b3be68a7488abdb9de6ce78d311")
    BOT_TOKEN = os.environ.get("6898599695:AAE-rukB-OoPJgxOOOcKKuK_8gv55HiC4ww")
    LOGS_CHANNEL = int(os.environ.get("-1002106332206"))
    MONGODB_URL = os.environ.get("mongodb+srv://dilfilter123:dilfilter123@cluster0.tq9uv2k.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
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
