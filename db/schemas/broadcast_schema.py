# thirdparty
from pydantic import BaseModel
from typing import Dict, List, Optional

# stdlib
from datetime import datetime

from db.schemas.message_schema import MessageDetail


class Broadcast(BaseModel):
    start_time: datetime
    message_text: str
    client_filter: str
    end_time: datetime


class BroadcastCreate(BaseModel):
    start_time: datetime
    message_text: str
    client_filter: str
    end_time: datetime

    class Config:
        orm_mode = True


class BroadcastStatistics(BaseModel):
    broadcast_id: int
    total_messages: int
    status_counts: Dict[str, int]  # Dict, where key==status ,value==numver of massages with this status

    class Config:
        orm_mode = True


class BroadcastDetailStatistics(BaseModel):
    broadcast_id: int
    message_details: List[MessageDetail]

    class Config:
        orm_mode = True


class BroadcastUpdate(BaseModel):
    start_time: Optional[datetime]
    message_text: Optional[str]
    client_filter: Optional[str]
    end_time: Optional[datetime]