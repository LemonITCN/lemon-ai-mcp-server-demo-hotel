from datetime import datetime
from typing import Optional
from uuid import uuid4

from sqlmodel import SQLModel, Field


def generate_id_str():
    return uuid4().hex


class BaseModel(SQLModel):
    id: str = Field(default_factory=generate_id_str, primary_key=True)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
    )
    updated_at: Optional[datetime] = Field(
        default=None,
    )
    deleted_at: Optional[datetime] = None
