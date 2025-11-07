from pydantic import BaseModel


class Incident(BaseModel):
    description: str
    stat: str
    source: str
    datetime: str