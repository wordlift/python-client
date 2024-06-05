# coding: utf-8

"""
    Middleware

    Knowledge Graph data management.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class WithLimits(BaseModel):
    """
    An array of objects.
    """ # noqa: E501
    account_limits: Optional[StrictInt] = None
    applies_to: StrictStr
    block: Optional[StrictBool] = None
    consumption: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    id: Optional[StrictInt] = None
    limits: Optional[StrictInt] = None
    reference_id: Optional[StrictInt] = None
    reference_type: Optional[StrictStr] = None
    remaining: Optional[StrictInt] = None
    resets_in_seconds: Optional[StrictInt] = None
    subscription_limits: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["account_limits", "applies_to", "block", "consumption", "id", "limits", "reference_id", "reference_type", "remaining", "resets_in_seconds", "subscription_limits"]

    @field_validator('reference_type')
    def reference_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUBSCRIPTION', 'ACCOUNT']):
            raise ValueError("must be one of enum values ('SUBSCRIPTION', 'ACCOUNT')")
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
        """Create an instance of WithLimits from a JSON string"""
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
        """Create an instance of WithLimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_limits": obj.get("account_limits"),
            "applies_to": obj.get("applies_to"),
            "block": obj.get("block"),
            "consumption": obj.get("consumption"),
            "id": obj.get("id"),
            "limits": obj.get("limits"),
            "reference_id": obj.get("reference_id"),
            "reference_type": obj.get("reference_type"),
            "remaining": obj.get("remaining"),
            "resets_in_seconds": obj.get("resets_in_seconds"),
            "subscription_limits": obj.get("subscription_limits")
        })
        return _obj


