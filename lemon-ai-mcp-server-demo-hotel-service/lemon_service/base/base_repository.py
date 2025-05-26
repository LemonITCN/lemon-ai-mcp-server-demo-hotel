from typing import Generic, TypeVar, Type, List, Optional
from uuid import UUID

from sqlmodel import select

from vrtalk_ai.base.base_model import BaseModel
from vrtalk_ai.core.db_engine import create_db_session

T = TypeVar("T", bound=BaseModel)


class BaseRepository(Generic[T]):
    model: Type[T]

    def __init__(self, model: Type[T]):
        self.model = model

    def get(self, id: str) -> Optional[T]:
        """根据 ID 获取记录"""
        with create_db_session() as session:
            return session.get(self.model, id)

    def get_all(self) -> List[T]:
        """获取所有记录"""
        with create_db_session() as session:
            return session.execute(select(self.model)).scalars().all()

    def upsert(self, obj: T) -> T:
        """如果对象存在则更新，否则插入"""
        with create_db_session() as session:
            obj_id = obj.id

            if not obj_id or (isinstance(obj_id, str) and not obj_id.strip()):
                # 没有 ID，新增
                session.add(obj)
                session.commit()
                session.refresh(obj)
                return obj
            else:
                # 有 ID，检查是否已存在
                existing = session.get(self.model, obj_id)
                if existing:
                    # 更新已有对象字段
                    for key, value in obj.dict(exclude_unset=True).items():
                        setattr(existing, key, value)
                    session.commit()
                    session.refresh(existing)
                    return existing
                else:
                    # 不存在，作为新对象添加
                    session.add(obj)
                    session.commit()
                    session.refresh(obj)
                    return obj

    def create(self, obj: T) -> T:
        """创建新记录"""
        with create_db_session() as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    def update(self, obj: T) -> Optional[T]:
        """根据对象的 ID 更新已有记录"""
        with create_db_session() as session:
            obj_id = getattr(obj, "id", None)
            if not obj_id:
                return None  # 没有 ID，无法更新

            existing = session.get(self.model, obj_id)
            if not existing:
                return None  # 数据库中找不到这个对象

            for key, value in obj.dict(exclude_unset=True).items():
                setattr(existing, key, value)

            session.commit()
            session.refresh(existing)
            return existing

    def delete(self, id: str) -> bool:
        """根据 ID 删除记录"""
        with create_db_session() as session:
            obj = session.get(self.model, id)
            if obj:
                session.delete(obj)
                session.commit()
                return True
            return False

    def query_by_fields(self, **kwargs) -> List[T]:
        """
        通用单表多字段查询：支持任意字段组合查询
        示例：repo.query_by_fields(name="Alice", age=20)
        """
        with create_db_session() as session:
            query = select(self.model)
            for key, value in kwargs.items():
                if hasattr(self.model, key) and value is not None:
                    query = query.where(getattr(self.model, key) == value)
            return session.exec(query).all()
