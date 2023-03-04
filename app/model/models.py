from pydantic import BaseModel


class SuggesticRequest(BaseModel):
    items: list
