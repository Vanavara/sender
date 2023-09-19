# stdlib
from typing import Optional
from typing import Annotated
#
# # thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Body
from fastapi import HTTPException

# project
import settings
from db.db_setup import get_session
from db.models.client_model import ClientModel
from db.schemas.client_schema import ClientCreate, ClientResponse, ClientUpdate
from services.client_service import create_client_internal, update_client_internal, delete_client_internal

client_router = APIRouter(tags=["1. CLIENT"], prefix="/client")


@client_router.post("/clients/", response_model=ClientResponse)
async def create_client(
    client: ClientCreate, session: AsyncSession = Depends(get_session)
):
    """
    Create a new client
    """
    client_data = await create_client_internal(session=session, client=client)
    return client_data


@client_router.put("/clients/{client_id}/")
async def update_client(
    client_id: int, client_update: ClientUpdate, session: AsyncSession = Depends(get_session)
):
    """
    Update client's data
    """
    existing_client = await session.get(ClientModel, client_id)
    if not existing_client:
        raise HTTPException(status_code=404, detail="Client not found")

    existing_client.phone_number = client_update.phone_number
    await session.commit()

    return existing_client


@client_router.delete("/clients/{client_id}/", response_model=dict)
async def remove_client(
    client_id: int, session: AsyncSession = Depends(get_session)
):
    """
    Delete a client by client_id
    """
    result = await delete_client_internal(session=session, client_id=client_id)
    if result["status"] == "error":
        raise HTTPException(status_code=404, detail=result["message"])
    return result
