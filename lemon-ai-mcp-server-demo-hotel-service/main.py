import uvicorn

from lemon_service.config.server_config import SERVER_CONFIG_HOST, SERVER_CONFIG_PORT
from lemon_service.core import app
from lemon_service.core.db_engine import auto_create_tables
from lemon_service.core.setup_logger import setup_logging

if __name__ == "__main__":
    setup_logging()
    auto_create_tables()

    # 启动服务
    uvicorn.run(app, host=SERVER_CONFIG_HOST, port=SERVER_CONFIG_PORT, log_config=None)
