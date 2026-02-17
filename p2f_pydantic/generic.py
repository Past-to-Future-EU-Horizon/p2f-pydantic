from pydantic import BaseModel

class Message(BaseModel):
    """This model will exclusively be used by the server, not by the client library. 

    :param BaseModel: Pydantic Base Model
    :type BaseModel: Pydantic.BaseModel
    """
    message: str