# thirdparty
from typing import Optional

from pydantic import BaseModel


class Client(BaseModel):
    phone_number: str
    operator_code: str
    tag: str
    timezone: str

    class Config:
        orm_mode = True

class ClientResponse(BaseModel):
    phone_number: Optional[str]
    operator_code: Optional[str]
    tag: Optional[str]
    timezone: Optional[str]

    class Config:
        orm_mode = True


class ClientUpdate(BaseModel):
    phone_number: Optional[str]


class ClientCreate(BaseModel):
    phone_number: str
    operator_code: Optional[str]
    tag: Optional[str]
    timezone: Optional[str]

    class Config:
        orm_mode = True
