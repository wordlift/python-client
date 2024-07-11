# coding: utf-8

"""
    Summarizer

    Generic text summarization

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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PlatformLimitRequest(BaseModel):
    """
    Platform Limit request
    """ # noqa: E501
    applies_to: StrictStr
    based_on: StrictStr
    based_on_value: StrictStr
    description: Optional[StrictStr] = None
    limits: Annotated[int, Field(strict=True, ge=1)]
    scope: StrictStr
    __properties: ClassVar[List[str]] = ["applies_to", "based_on", "based_on_value", "description", "limits", "scope"]

    @field_validator('based_on')
    def based_on_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SKU']):
            raise ValueError("must be one of enum values ('SKU')")
        return value

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACCOUNT', 'SUBSCRIPTION']):
            raise ValueError("must be one of enum values ('ACCOUNT', 'SUBSCRIPTION')")
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
        """Create an instance of PlatformLimitRequest from a JSON string"""
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
        """Create an instance of PlatformLimitRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applies_to": obj.get("applies_to"),
            "based_on": obj.get("based_on"),
            "based_on_value": obj.get("based_on_value"),
            "description": obj.get("description"),
            "limits": obj.get("limits"),
            "scope": obj.get("scope")
        })
        return _obj


