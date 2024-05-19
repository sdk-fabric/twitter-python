"""
UserTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .fields import Fields
from .like_response import LikeResponse
from .pagination import Pagination
from .single_tweet import SingleTweet
from .tweet_collection import TweetCollection
from .user import User
from .user_collection import UserCollection

class UserTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, ids: str, expansions: str, fields: Fields) -> UserCollection:
        """
        Returns a variety of information about one or more users specified by the requested IDs.
        """
        try:
            path_params = {}

            query_params = {}
            query_params["ids"] = ids
            query_params["expansions"] = expansions
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/users", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return UserCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get(self, user_id: str, expansions: str, fields: Fields) -> User:
        """
        Returns a variety of information about a single user specified by the requested ID.
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}
            query_params["expansions"] = expansions
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/users/:user_id", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return User.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get_timeline(self, user_id: str, exclude: str, expansions: str, pagination: Pagination, fields: Fields) -> TweetCollection:
        """
        Allows you to retrieve a collection of the most recent Tweets and Retweets posted by you and users you follow. This endpoint can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date.
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}
            query_params["exclude"] = exclude
            query_params["expansions"] = expansions
            query_params["pagination"] = pagination
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('pagination')
            query_struct_names.append('fields')

            url = self.parser.url("/2/users/:user_id/timelines/reverse_chronological", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def get_liked_tweets(self, user_id: str, expansions: str, max_results: int, pagination_token: str, fields: Fields) -> TweetCollection:
        """
        Tweets liked by a user
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}
            query_params["expansions"] = expansions
            query_params["max_results"] = max_results
            query_params["pagination_token"] = pagination_token
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/users/:user_id/liked_tweets", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TweetCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def remove_like(self, user_id: str, tweet_id: str) -> LikeResponse:
        """
        Allows a user or authenticated user ID to unlike a Tweet.
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id
            path_params["tweet_id"] = tweet_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/users/:user_id/likes/:tweet_id", path_params)

            headers = {}

            response = self.http_client.delete(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return LikeResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def create_like(self, user_id: str, payload: SingleTweet) -> LikeResponse:
        """
        Causes the user ID identified in the path parameter to Like the target Tweet.
        """
        try:
            path_params = {}
            path_params["user_id"] = user_id

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/users/:user_id/likes", path_params)

            headers = {}
            headers["Content-Type"] = "application/json"

            response = self.http_client.post(url, headers=headers, params=self.parser.query(query_params, query_struct_names), json=payload.model_dump(by_alias=True))

            if response.status_code >= 200 and response.status_code < 300:
                return LikeResponse.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))

    def find_by_name(self, usernames: str, expansions: str, fields: Fields) -> UserCollection:
        """
        Returns a variety of information about one or more users specified by their usernames.
        """
        try:
            path_params = {}

            query_params = {}
            query_params["usernames"] = usernames
            query_params["expansions"] = expansions
            query_params["fields"] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url("/2/users/by", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return UserCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


