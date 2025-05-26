import logging
import sys

from loguru import logger

from lemon_service.config.server_config import SERVER_CONFIG_LOG_LEVEL


class InterceptHandler(logging.Handler):
    """日志拦截处理器：将Python标准日志重定向到Loguru

    工作原理：
    1. 继承自logging.Handler
    2. 重写emit方法处理日志记录
    3. 将标准库日志转换为Loguru格式
    """

    def emit(self, record: logging.LogRecord) -> None:
        # 尝试获取日志级别名称
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 获取调用帧信息
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # 使用Loguru记录日志
        logger.opt(
            depth=depth,
            exception=record.exc_info
        ).log(
            level,
            record.getMessage()
        )


def setup_logging():
    """
    配置日志系统
    """
    # 步骤1：移除默认处理器
    logger.remove()

    # 步骤2：配置标准库日志
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # 步骤3：配置第三方库日志
    for logger_name in [
        "uvicorn",
        "fastapi",
    ]:
        _logger = logging.getLogger(logger_name)
        _logger.handlers = [InterceptHandler()]
        _logger.propagate = False

    # 步骤4：定义日志格式
    log_format = (
        # 时间信息
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        # 日志级别，居中对齐
        "<level>{level: ^8}</level> | "
        # 进程和线程信息
        "process [<cyan>{process}</cyan>]:<cyan>{thread}</cyan> | "
        # 文件、函数和行号
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        # 日志消息
        "<level>{message}</level>"
    )

    # 步骤5：配置控制台输出
    logger.add(
        sys.stdout,
        format=log_format,
        level=SERVER_CONFIG_LOG_LEVEL,
        enqueue=True,  # 启用异步写入
        backtrace=True,  # 显示完整的异常回溯
        diagnose=True,  # 显示变量值等诊断信息
        colorize=True  # 启用彩色输出
    )

    # 步骤6：配置文件输出
    logger.add(
        "logs/vrtalk_ai_{time}.log",  # 自动按时间命名的日志文件
        rotation="10 MB",  # 日志轮转：每10MB一个新文件
        retention="7 days",  # 日志保留：7天
        compression="zip",  # 压缩格式
        level=SERVER_CONFIG_LOG_LEVEL,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    logger.debug("LEMON日志系统初始化完成")
