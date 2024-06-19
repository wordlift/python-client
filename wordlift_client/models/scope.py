# coding: utf-8

"""
    WordLift Fact-Checking API

    API for semi-automated fact-checking. Returns schema.org/ClaimReview markup. This markup is structured data that contains information about the fact check -- for example, what was the claim being assessed, who made the claim, what was the verdict.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Scope(str, Enum):
    """
    The rule scope.
    """

    """
    allowed enum values
    """
    USER = 'USER'
    PROJECT = 'PROJECT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Scope from a JSON string"""
        return cls(json.loads(json_str))


