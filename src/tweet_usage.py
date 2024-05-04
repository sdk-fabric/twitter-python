"""
tweet_usage automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
class TweetUsage(BaseModel):
    cap_reset_day: Optional[int] = Field(default=None, alias="cap_reset_day")
    project_cap: Optional[str] = Field(default=None, alias="project_cap")
    project_id: Optional[str] = Field(default=None, alias="project_id")
    project_usage: Optional[str] = Field(default=None, alias="project_usage")
    pass
