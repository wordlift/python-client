# coding: utf-8

"""
    WordLift API

    WordLift API

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AnalysesRequest(BaseModel):
    """
    The analysis request.
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="The text to analyse.")
    url: Optional[StrictStr] = Field(default=None, description="The URL to analyse.")
    query: Optional[StrictStr] = Field(default=None, description="The query string to analyse.")
    html: Optional[StrictStr] = Field(default=None, description="The html to analyse.")
    language_code: Optional[StrictStr] = Field(default='en', description="The language code used for content analysis, e.g. `en`.")
    query_location_name: Optional[StrictStr] = Field(default='United States', description="The location name for the query, e.g. United Kingdom.")
    query_search_engine: Optional[StrictStr] = Field(default=None, description="The search engine domain for the query, if not set will be chosen according to `query_location_name`")
    linked_data: Optional[StrictBool] = Field(default=True, description="Whether to include results from Linked Data (e.g. DBpedia), by default true.")
    local_data: Optional[StrictBool] = Field(default=True, description="Whether to include results from the local Knowledge Graph, by default true.")
    network_data: Optional[StrictBool] = Field(default=True, description="Whether to include results from connected Knowledge Graphs, by default true.")
    __properties: ClassVar[List[str]] = ["text", "url", "query", "html", "language_code", "query_location_name", "query_search_engine", "linked_data", "local_data", "network_data"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AnalysesRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalysesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "url": obj.get("url"),
            "query": obj.get("query"),
            "html": obj.get("html"),
            "language_code": obj.get("language_code") if obj.get("language_code") is not None else 'en',
            "query_location_name": obj.get("query_location_name") if obj.get("query_location_name") is not None else 'United States',
            "query_search_engine": obj.get("query_search_engine"),
            "linked_data": obj.get("linked_data") if obj.get("linked_data") is not None else True,
            "local_data": obj.get("local_data") if obj.get("local_data") is not None else True,
            "network_data": obj.get("network_data") if obj.get("network_data") is not None else True
        })
        return _obj


