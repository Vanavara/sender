# thirdparty
from typing import Optional

from pydantic import BaseModel

# stdlib
from datetime import datetime


class Message(BaseModel):
    created_at: datetime
    status: str
    broadcast_id: int
    client_id: int

    class Config:
        orm_mode = True


class MessageCreate(BaseModel):
    status: str
    broadcast_id: int
    client_id: int

    class Config:
        orm_mode = True


class MessageUpdate(BaseModel):
    status: Optional[str]

    class Config:
        orm_mode = True


class MessageResponse(BaseModel):
    id: int
    created_at: datetime
    status: str
    broadcast_id: int
    client_id: int

    class Config:
        orm_mode = True


class MessageDetail(BaseModel):
    message_id: int
    status: str
    client_id: int
