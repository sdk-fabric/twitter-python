"""
single_tweet automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class SingleTweet(BaseModel):
    tweet_id: Optional[str] = Field(default=None, alias="tweet_id")
    pass