# coding: utf-8

"""
    Analysis

    Analyse content using Linked Data and Knowledge Graphs.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ValidationTypeEnum(str, Enum):
    """
    ValidationTypeEnum
    """

    """
    allowed enum values
    """
    FIND_AND_REPLACE = 'FIND_AND_REPLACE'
    OPEN_AI = 'OPEN_AI'
    APPEND = 'APPEND'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ValidationTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


