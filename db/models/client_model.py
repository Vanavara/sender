# thirdparty
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ClientModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True)
    operator_code = Column(String, nullable=True)
    tag = Column(String, nullable=True)
    timezone = Column(String, nullable=True)

    messages = relationship("MessageModel", back_populates="client")