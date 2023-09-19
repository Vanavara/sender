# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

# project
from db.models.broadcast_model import BroadcastModel
from db.schemas.broadcast_schema import BroadcastCreate, BroadcastUpdate


async def create_broadcast_internal(session: AsyncSession, broadcast: BroadcastCreate):
    start_time = broadcast.start_time.replace(tzinfo=None)
    end_time = broadcast.end_time.replace(tzinfo=None)

    new_broadcast = BroadcastModel(
        start_time=start_time,
        message_text=broadcast.message_text,
        client_filter=broadcast.client_filter,
        end_time=end_time,
    )

    session.add(new_broadcast)
    await session.flush()

    return new_broadcast


async def update_broadcast_internal(session: AsyncSession, broadcast_id: int, broadcast_data: BroadcastUpdate):
    broadcast = await session.get(BroadcastModel, broadcast_id)
    if not broadcast:
        return None

    broadcast.message_text = broadcast_data.message_text
    await session.flush()

    return broadcast


async def delete_broadcast_internal(session: AsyncSession, broadcast_id: int):
    broadcast = await session.get(BroadcastModel, broadcast_id)
    if not broadcast:
        return False

    await session.delete(broadcast)
    await session.flush()

    return True
