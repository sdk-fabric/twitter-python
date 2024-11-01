"""
Client automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .tweet_tag import TweetTag
from .usage_tag import UsageTag
from .user_tag import UserTag
from .bookmark_tag import BookmarkTag
from .search_tag import SearchTag
from .quote_tag import QuoteTag
from .trends_tag import TrendsTag
from .retweet_tag import RetweetTag

class Client(sdkgen.ClientAbstract):
    def __init__(self, base_url: str, credentials: sdkgen.CredentialsInterface):
        super().__init__(base_url, credentials)

    def tweet(self) -> TweetTag:
        return TweetTag(
            self.http_client,
            self.parser
        )

    def usage(self) -> UsageTag:
        return UsageTag(
            self.http_client,
            self.parser
        )

    def user(self) -> UserTag:
        return UserTag(
            self.http_client,
            self.parser
        )

    def bookmark(self) -> BookmarkTag:
        return BookmarkTag(
            self.http_client,
            self.parser
        )

    def search(self) -> SearchTag:
        return SearchTag(
            self.http_client,
            self.parser
        )

    def quote(self) -> QuoteTag:
        return QuoteTag(
            self.http_client,
            self.parser
        )

    def trends(self) -> TrendsTag:
        return TrendsTag(
            self.http_client,
            self.parser
        )

    def retweet(self) -> RetweetTag:
        return RetweetTag(
            self.http_client,
            self.parser
        )



    @staticmethod
    def build(token: str):
        return Client("https://api.twitter.com", sdkgen.HttpBearer(token))


    @staticmethod
    def buildAnonymous():
        return Client("https://api.twitter.com", sdkgen.Anonymous())
