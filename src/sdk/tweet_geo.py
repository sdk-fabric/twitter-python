"""
tweet_geo automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler, Tag
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Annotated, Union


class TweetGeo(BaseModel):
    place_id: Optional[str] = Field(default=None, alias="place_id")
    pass


