# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession

# project
from db.models.message_model import MessageModel
from db.schemas.message_schema import MessageCreate, MessageUpdate


async def create_message_internal(session: AsyncSession, message: MessageCreate):
    new_message = MessageModel(content=message.content)
    session.add(new_message)
    await session.flush()
    return new_message


async def delete_message_internal(session: AsyncSession, message_id: int):
    message = await session.get(MessageModel, message_id)
    if not message:
        raise ValueError("Message not found")
    session.delete(message)
    await session.flush()


async def get_message_by_id_internal(session: AsyncSession, message_id: int) -> MessageModel:
    message = await session.get(MessageModel, message_id)
    if not message:
        raise ValueError("Message not found")
    return message


async def update_message_internal(session: AsyncSession, message_id: int, message_data: MessageUpdate) -> MessageModel:
    message = await session.get(MessageModel, message_id)
    if not message:
        raise ValueError("Message not found")

    # Обновляем атрибуты сообщения
    for key, value in message_data.dict().items():
        setattr(message, key, value)

    await session.commit()
    return message

