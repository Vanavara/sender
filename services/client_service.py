# stdlib
from datetime import datetime

# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

# project
from db.models.client_model import ClientModel
from db.schemas.client_schema import ClientCreate


import logging

logger = logging.getLogger(__name__)

async def create_client_internal(session: AsyncSession, client: ClientCreate):
    try:
        new_client = ClientModel(
            phone_number=client.phone_number,
            operator_code=client.operator_code,
            tag=client.tag,
            timezone=client.timezone,
        )

        session.add(new_client)
        await session.flush()

        return new_client
    except Exception as e:
        logger.error(f"Error while creating client: {e}")
        raise


async def update_client_internal(session: AsyncSession, client_id: int, phone_number: str):
    query = (
        update(ClientModel)
        .where(ClientModel.id == client_id)
        .values(phone_number=phone_number)
    )
    await session.execute(query)
    await session.commit()


async def delete_client_internal(session: AsyncSession, client_id: int):
    client = await session.get(ClientModel, client_id)
    if client:
        await session.delete(client)
        await session.commit()
        return {"status": "success", "message": "Client deleted successfully"}
    else:
        return {"status": "error", "message": "Client not found"}
