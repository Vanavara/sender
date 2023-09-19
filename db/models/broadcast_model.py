# thirdparty
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class BroadcastModel(Base):
    __tablename__ = "broadcasts"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, default=datetime.utcnow)
    message_text = Column(String)
    client_filter = Column(String)
    end_time = Column(DateTime)

    messages = relationship("MessageModel", back_populates="broadcast")
