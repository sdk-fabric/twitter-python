"""
ErrorsException automatically generated by SDKgen please do not edit this file manually
https://sdkgen.app
"""

import sdkgen
from typing import Dict
from typing import Any

from .errors import Errors

class ErrorsException(sdkgen.KnownStatusCodeException):
    payload: Errors = None

    def __init__(self, payload):
        self.payload = payload

    def get_payload(self) -> Errors:
        return self.payload
