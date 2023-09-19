# # thirdparty
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from db.db_setup import get_session
from db.schemas.message_schema import MessageCreate, MessageResponse, MessageUpdate
from services.message_service import create_message_internal, delete_message_internal, get_message_by_id_internal, \
    update_message_internal

message_router = APIRouter(tags=["3. MESSAGE"], prefix="/message")



@message_router.post("/messages/", response_model=MessageCreate)
async def create_new_message(message: MessageCreate, session: AsyncSession = Depends(get_session)):
    """
    Create a new message
    """
    message_data = await create_message_internal(session=session, message=message)
    return message_data


@message_router.delete("/messages/{message_id}/", response_model=None)
async def delete_message_by_id(message_id: int, session: AsyncSession = Depends(get_session)):
    """
    Delete a message by its ID
    """
    try:
        await delete_message_internal(session=session, message_id=message_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"status": "Message deleted successfully"}


@message_router.get("/messages/{message_id}/", response_model=MessageResponse)
async def get_message_by_id(message_id: int, session: AsyncSession = Depends(get_session)):
    """
    Get a message by its ID
    """
    try:
        message = await get_message_by_id_internal(session=session, message_id=message_id)
        return message
    except ValueError:
        raise HTTPException(status_code=404, detail="Message not found")


@message_router.put("/messages/{message_id}/", response_model=MessageResponse)
async def update_message_by_id(
        message_id: int,
        message_data: MessageUpdate,
        session: AsyncSession = Depends(get_session)
):
    """
    Update a message by its ID
    """
    try:
        updated_message = await update_message_internal(
            session=session,
            message_id=message_id,
            message_data=message_data
        )
        return updated_message
    except ValueError:
        raise HTTPException(status_code=404, detail="Message not found")


