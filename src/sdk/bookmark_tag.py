"""
BookmarkTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .bookmark_response import BookmarkResponse
from .fields import Fields
from .single_tweet import SingleTweet
from .tweet_collection import TweetCollection

class BookmarkTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, user_id: str, expansions: str, pagination_token: str, fields: Fields) -> TweetCollection:
        """
        Allows you to get an authenticated user&#039;s 800 most recent bookmarked Tweets.
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}
            query_params["expansions"] = expansions
            query_params["pagination_token"] = pagination_token
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/users/:user_id/bookmarks", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create(self, user_id: str, payload: SingleTweet) -> BookmarkResponse:
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/users/:user_id/bookmarks", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return BookmarkResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def delete(self, user_id: str, tweet_id: str) -> BookmarkResponse:
        try:
            path_params = {}
            path_params["user_id"] = user_id
            path_params["tweet_id"] = tweet_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/users/:user_id/bookmarks/:tweet_id", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return BookmarkResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


