from pydantic import BaseModel
from typing import Optional
from sqlalchemy.sql.sqltypes import TIMESTAMP

class NewPost(BaseModel):   
    post_id : Optional[int] = None
    title : str
    content : str
    published : bool = True

class ModifyPost(BaseModel):
    post_id : int
    title : Optional[str] = None
    content : Optional[str]=None

class PostOutput(BaseModel):
    post_id : int
    title : str
    content : str  

    class Config:
        from_attributes = True



    



