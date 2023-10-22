from pydantic import BaseModel


class ticket(BaseModel):
    gate: str
    cost: int
    name: str
    