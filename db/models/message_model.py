# thirdparty
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# project
from db.models.broadcast_model import BroadcastModel
from db.models.client_model import ClientModel
Base = declarative_base()



class MessageModel(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, index=True)
    broadcast_id = Column(Integer, ForeignKey('broadcasts.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))

    broadcast = relationship("BroadcastModel", back_populates="messages")
    client = relationship("ClientModel", back_populates="messages")
