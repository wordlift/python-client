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


class ProjectType(str, Enum):
    """
    The project type, if applicable.
    """

    """
    allowed enum values
    """
    SMART_CONTENT = 'SMART_CONTENT'
    CONTENT_GENERATION = 'CONTENT_GENERATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProjectType from a JSON string"""
        return cls(json.loads(json_str))


