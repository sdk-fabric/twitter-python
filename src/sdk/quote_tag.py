"""
QuoteTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List
from typing import Dict
from typing import Any
from urllib.parse import parse_qs

from .errors import Errors
from .errors_exception import ErrorsException
from .fields import Fields
from .tweet_collection import TweetCollection

class QuoteTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_all(self, tweet_id: str, exclude: str, expansions: str, max_results: int, pagination_token: str, fields: Fields) -> TweetCollection:
        """
        Returns Quote Tweets for a Tweet specified by the requested Tweet ID.
        """
        try:
            path_params = {}
            path_params['tweet_id'] = tweet_id

            query_params = {}
            query_params['exclude'] = exclude
            query_params['expansions'] = expansions
            query_params['max_results'] = max_results
            query_params['pagination_token'] = pagination_token
            query_params['fields'] = fields

            query_struct_names = []
            query_struct_names.append('fields')

            url = self.parser.url('/2/tweets/:tweet_id/quote_tweets', path_params)

            options = {}
            options['headers'] = {}
            options['params'] = self.parser.query(query_params, query_struct_names)



            response = self.http_client.request('GET', url, **options)

            if response.status_code >= 200 and response.status_code < 300:
                data = TweetCollection.model_validate_json(json_data=response.content)

                return data

            statusCode = response.status_code
            if statusCode >= 0 and statusCode <= 999:
                data = Errors.model_validate_json(json_data=response.content)

                raise ErrorsException(data)

            raise sdkgen.UnknownStatusCodeException('The server returned an unknown status code: ' + str(statusCode))
        except RequestException as e:
            raise sdkgen.ClientException('An unknown error occurred: ' + str(e))



