# # stdlib
from typing import Optional, List

# thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from collections import Counter

# project
import settings
from db.db_setup import get_session
from db.models.broadcast_model import BroadcastModel
from db.models.message_model import MessageModel
from db.schemas.broadcast_schema import BroadcastCreate, BroadcastUpdate, BroadcastStatistics, BroadcastDetailStatistics
from services.broadcast_srvice import create_broadcast_internal, update_broadcast_internal, delete_broadcast_internal


broadcast_router = APIRouter(tags=["2. BROADCAST"], prefix="/broadcast")


@broadcast_router.post("/broadcasts/")
async def create_broadcast(
    broadcast: BroadcastCreate, session: AsyncSession = Depends(get_session)
):
    """
    Create a new broadcast
    """
    broadcast_data = await create_broadcast_internal(session=session, broadcast=broadcast)
    return broadcast_data


@broadcast_router.put("/broadcast/{broadcast_id}/", response_model=BroadcastCreate)
async def update_broadcast(
    broadcast_id: int,
    broadcast_data: BroadcastUpdate,
    session: AsyncSession = Depends(get_session)
):
    """
    Update a broadcast
    """
    updated_broadcast = await update_broadcast_internal(session, broadcast_id, broadcast_data)
    if not updated_broadcast:
        raise HTTPException(status_code=404, detail="Broadcast not found")
    return updated_broadcast


@broadcast_router.delete("/broadcast/{broadcast_id}/", response_model=dict)
async def delete_broadcast(
    broadcast_id: int,
    session: AsyncSession = Depends(get_session)
):
    """
    Delete a broadcast
    """
    result = await delete_broadcast_internal(session, broadcast_id)
    if not result:
        raise HTTPException(status_code=404, detail="Broadcast not found")
    return {"status": "success", "message": "Broadcast deleted successfully"}



@broadcast_router.get("/broadcasts/statistics/", response_model=List[BroadcastStatistics])
async def get_broadcast_statistics(session: AsyncSession = Depends(get_session)):
    """
    Get statistic
    """
    broadcasts = await session.query(BroadcastModel).all()
    statistics = []
    for broadcast in broadcasts:
        messages = await session.query(MessageModel).filter(MessageModel.broadcast_id == broadcast.id).all()
        total_messages = len(messages)
        status_counts = Counter([message.status for message in messages])
        statistics.append({
            "broadcast_id": broadcast.id,
            "total_messages": total_messages,
            "status_counts": status_counts
        })
    return statistics


@broadcast_router.get("/broadcasts/{broadcast_id}/statistics/", response_model=BroadcastDetailStatistics)
async def get_broadcast_detail_statistics(broadcast_id: int, session: AsyncSession = Depends(get_session)):
    """
    Get detailed statistic
    """
    broadcast = await session.query(BroadcastModel).filter(BroadcastModel.id == broadcast_id).first()
    if not broadcast:
        raise HTTPException(status_code=404, detail="Broadcast not found")

    messages = await session.query(MessageModel).filter(MessageModel.broadcast_id == broadcast.id).all()
    detailed_stats = []
    for message in messages:
        detailed_stats.append({
            "message_id": message.id,
            "status": message.status,
            "client_id": message.client_id
        })

    return {
        "broadcast_id": broadcast.id,
        "message_details": detailed_stats
    }
