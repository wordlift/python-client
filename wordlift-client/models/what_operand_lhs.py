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


class WhatOperandLhs(str, Enum):
    """
    The left hand side operand for what condition.
    """

    """
    allowed enum values
    """
    EVERYWHERE = 'EVERYWHERE'
    FIRST_SENTENCE = 'FIRST_SENTENCE'
    LAST_SENTENCE = 'LAST_SENTENCE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WhatOperandLhs from a JSON string"""
        return cls(json.loads(json_str))

