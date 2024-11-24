from pydantic import BaseModel

class DataSchema(BaseModel):
    name: str
    age: int
    date_of_birth: str

    class Config:
        orm_mode = True
