# coding: utf-8

"""
    GraphQL support

    GraphQL endpoint to query Knowledge Graphs

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AutocompleteResult(BaseModel):
    """
    AutocompleteResult
    """ # noqa: E501
    id: Optional[StrictStr] = None
    labels: Optional[List[StrictStr]] = None
    descriptions: Optional[List[StrictStr]] = None
    types: Optional[List[StrictStr]] = None
    urls: Optional[List[StrictStr]] = None
    images: Optional[List[StrictStr]] = Field(default=None, description="A list of image URLs.")
    same_ass: Optional[List[StrictStr]] = Field(default=None, alias="sameAss")
    scope: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    main_type: Optional[StrictStr] = Field(default=None, description="Schema type slug", alias="mainType")
    label: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    display_types: Optional[StrictStr] = Field(default=None, alias="displayTypes")
    __properties: ClassVar[List[str]] = ["id", "labels", "descriptions", "types", "urls", "images", "sameAss", "scope", "description", "mainType", "label", "value", "displayTypes"]

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['local', 'network', 'cloud']):
            raise ValueError("must be one of enum values ('local', 'network', 'cloud')")
        return value

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
        """Create an instance of AutocompleteResult from a JSON string"""
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
        """Create an instance of AutocompleteResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "labels": obj.get("labels"),
            "descriptions": obj.get("descriptions"),
            "types": obj.get("types"),
            "urls": obj.get("urls"),
            "images": obj.get("images"),
            "sameAss": obj.get("sameAss"),
            "scope": obj.get("scope"),
            "description": obj.get("description"),
            "mainType": obj.get("mainType"),
            "label": obj.get("label"),
            "value": obj.get("value"),
            "displayTypes": obj.get("displayTypes")
        })
        return _obj


