# coding: utf-8

"""
    WordLift Fact-Checking API

    API for semi-automated fact-checking. Returns schema.org/ClaimReview markup. This markup is structured data that contains information about the fact check -- for example, what was the claim being assessed, who made the claim, what was the verdict.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.event import Event
from typing import Optional, Set
from typing_extensions import Self

class Response1(BaseModel):
    """
    Response1
    """ # noqa: E501
    items: Optional[List[Event]] = None
    var_self: Optional[StrictStr] = Field(default=None, alias="self")
    next: Optional[StrictStr] = None
    prev: Optional[StrictStr] = None
    last: Optional[StrictStr] = None
    first: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["items", "self", "next", "prev", "last", "first"]

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
        """Create an instance of Response1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Response1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [Event.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "self": obj.get("self"),
            "next": obj.get("next"),
            "prev": obj.get("prev"),
            "last": obj.get("last"),
            "first": obj.get("first")
        })
        return _obj


