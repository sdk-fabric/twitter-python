"""
hide_reply_response automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union
from .hide_reply import HideReply


class HideReplyResponse(BaseModel):
    data: Optional[HideReply] = Field(default=None, alias="data")
    pass


