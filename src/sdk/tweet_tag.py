"""
TweetTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .fields import Fields
from .hide_reply import HideReply
from .hide_reply_response import HideReplyResponse
from .tweet import Tweet
from .tweet_collection import TweetCollection
from .tweet_create_response import TweetCreateResponse
from .tweet_delete_response import TweetDeleteResponse
from .tweet_entity import TweetEntity
from .user_collection import UserCollection

class TweetTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, ids: str, expansions: str, fields: Fields) -> TweetCollection:
        """
        Returns a variety of information about the Tweet specified by the requested ID or list of IDs.
        """
        try:
            path_params = {}

            query_params = {}
            query_params["ids"] = ids
            query_params["expansions"] = expansions
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/tweets", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, tweet_id: str, expansions: str, fields: Fields) -> TweetEntity:
        """
        Returns a variety of information about a single Tweet specified by the requested ID.
        """
        try:
            path_params = {}
            path_params["tweet_id"] = tweet_id

            query_params = {}
            query_params["expansions"] = expansions
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/tweets/:tweet_id", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetEntity.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create(self, payload: Tweet) -> TweetCreateResponse:
        """
        Creates a Tweet on behalf of an authenticated user.
        """
        try:
            path_params = {}

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/tweets", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetCreateResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def delete(self, tweet_id: str) -> TweetDeleteResponse:
        """
        Allows a user or authenticated user ID to delete a Tweet.
        """
        try:
            path_params = {}
            path_params["tweet_id"] = tweet_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/tweets/:tweet_id", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetDeleteResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def hide_reply(self, tweet_id: str, payload: HideReply) -> HideReplyResponse:
        """
        Hides or unhides a reply to a Tweet.
        """
        try:
            path_params = {}
            path_params["tweet_id"] = tweet_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/tweets/:tweet_id/hidden", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.put(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return HideReplyResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get_liking_users(self, tweet_id: str, expansions: str, max_results: int, pagination_token: str) -> UserCollection:
        """
        Allows you to get information about a Tweet’s liking users.
        """
        try:
            path_params = {}
            path_params["tweet_id"] = tweet_id

            query_params = {}
            query_params["expansions"] = expansions
            query_params["max_results"] = max_results
            query_params["pagination_token"] = pagination_token

            query_struct_names = []

            url = self.parser.url("/2/tweets/:tweet_id/liking_users", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return UserCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


