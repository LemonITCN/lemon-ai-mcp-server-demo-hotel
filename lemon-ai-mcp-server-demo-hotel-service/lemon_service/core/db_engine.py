from sqlmodel import SQLModel, create_engine, Session

from lemon_service.config.db_config import DB_CONFIG_URL
from lemon_service.model import hotel, hotel_room_type, hotel_room, hotel_room_use_record, user, user_session

_ = (hotel, hotel_room_type, hotel_room, hotel_room_use_record, user, user_session)


def create_db_engine():
    """
    创建数据库引擎
    :return: 数据库引擎
    """
    engine = create_engine(DB_CONFIG_URL, echo=True)
    return engine


def create_db_session():
    """
    创建数据库会话
    :return: 数据库会话
    """
    return Session(create_db_engine())


def auto_create_tables() -> None:
    """
    自动创建数据库表
    """
    SQLModel.metadata.create_all(create_db_engine())
