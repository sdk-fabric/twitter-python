"""
TrendsTag automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import requests
import sdkgen
from requests import RequestException
from typing import List

from .trend_collection import TrendCollection

class TrendsTag(sdkgen.TagAbstract):
    def __init__(self, http_client: requests.Session, parser: sdkgen.Parser):
        super().__init__(http_client, parser)


    def get_by_woeid(self, woeid: str) -> TrendCollection:
        """
        The Trends lookup endpoint allow developers to get the Trends for a location, specified using the where-on-earth id (WOEID).
        """
        try:
            path_params = {}
            path_params["woeid"] = woeid

            query_params = {}

            query_struct_names = []

            url = self.parser.url("/2/trends/by/woeid/:woeid", path_params)

            headers = {}

            response = self.http_client.get(url, headers=headers, params=self.parser.query(query_params, query_struct_names))

            if response.status_code >= 200 and response.status_code < 300:
                return TrendCollection.model_validate_json(json_data=response.content)


            raise sdkgen.UnknownStatusCodeException("The server returned an unknown status code")
        except RequestException as e:
            raise sdkgen.ClientException("An unknown error occurred: " + str(e))


