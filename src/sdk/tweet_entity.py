"""
tweet_entity automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from .tweet_details import TweetDetails
class TweetEntity(BaseModel):
    data: Optional[TweetDetails] = Field(default=None, alias="data")
    pass