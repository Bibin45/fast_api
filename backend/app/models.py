from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, TypeVar, Generic
from bson import ObjectId
import uuid

# Custom ObjectId validator
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v,field=None):
        if isinstance(v, str) and ObjectId.is_valid(v):
            return ObjectId(v)
        elif isinstance(v, ObjectId):
            return v
        raise ValueError('Invalid ObjectId')
    
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")

# Generic type for response model
T = TypeVar("T")


# Todo Model
class TodoModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    model_config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True,json_encoders = {ObjectId: str})

# Model for updating Todo
class UpdateTodoModel(BaseModel):
    name: Optional[str]
    description: Optional[str]

    model_config = ConfigDict(arbitrary_types_allowed=True)

# Generic Response Model
class ResponseModal(BaseModel, Generic[T]):
    status: str  # Response status
    message: str  # Response message
    data: Optional[T]  # Response data (optional)

    model_config = ConfigDict(arbitrary_types_allowed=True)
