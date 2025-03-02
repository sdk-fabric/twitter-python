"""
user automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class User(BaseModel):
    created_at: Optional[str] = Field(default=None, alias="created_at")
    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    pinned_tweet_id: Optional[str] = Field(default=None, alias="pinned_tweet_id")
    username: Optional[str] = Field(default=None, alias="username")
    pass


