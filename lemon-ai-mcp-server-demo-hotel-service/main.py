import uvicorn
from fastapi import FastAPI

# from lemon_service.api.chat import chat_router
from lemon_service.config.server_config import SERVER_CONFIG_HOST, SERVER_CONFIG_PORT
from lemon_service.core.db_engine import auto_create_tables
from lemon_service.core.setup_logger import setup_logging

if __name__ == "__main__":
    setup_logging()
    auto_create_tables()

    app = FastAPI()

    # app.include_router(chat_router)
    # app.include_router(image_analysis_router)
    uvicorn.run(app, host=SERVER_CONFIG_HOST, port=SERVER_CONFIG_PORT, log_config=None)
