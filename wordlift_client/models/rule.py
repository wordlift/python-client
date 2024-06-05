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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.level_enum import LevelEnum
from wordlift_client.models.project_type import ProjectType
from wordlift_client.models.scope import Scope
from wordlift_client.models.validation_fix import ValidationFix
from wordlift_client.models.what_operand_lhs import WhatOperandLhs
from wordlift_client.models.what_operator import WhatOperator
from wordlift_client.models.when_operator import WhenOperator
from typing import Optional, Set
from typing_extensions import Self

class Rule(BaseModel):
    """
    Rule
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="The create date-time.")
    description: Optional[StrictStr] = Field(default=None, description="Description for the rule")
    fixes: Optional[List[ValidationFix]] = Field(default=None, description="The list of fixes to apply when the rule validation fails.")
    id: Optional[StrictInt] = None
    is_enabled: Optional[StrictBool] = None
    level: LevelEnum
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time.")
    name: StrictStr = Field(description="The rule name.")
    project_id: Optional[StrictInt] = None
    project_type: Optional[ProjectType] = None
    scope: Scope
    type: StrictStr = Field(description="The rule type, one of `field`, `word` or `code`. By default `field`.")
    what_operand_lhs: WhatOperandLhs
    what_operand_rhs: StrictStr = Field(description="The right hand side operand for what condition.")
    what_operator: WhatOperator
    when_operand_lhs: StrictStr = Field(description="The left hand side  operand for when condition.")
    when_operand_rhs: StrictStr = Field(description="The right hand side operand for when condition.")
    when_operator: WhenOperator
    __properties: ClassVar[List[str]] = ["created_at", "description", "fixes", "id", "is_enabled", "level", "modified_at", "name", "project_id", "project_type", "scope", "type", "what_operand_lhs", "what_operand_rhs", "what_operator", "when_operand_lhs", "when_operand_rhs", "when_operator"]

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
        """Create an instance of Rule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "modified_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in fixes (list)
        _items = []
        if self.fixes:
            for _item in self.fixes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fixes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "fixes": [ValidationFix.from_dict(_item) for _item in obj["fixes"]] if obj.get("fixes") is not None else None,
            "id": obj.get("id"),
            "is_enabled": obj.get("is_enabled"),
            "level": obj.get("level"),
            "modified_at": obj.get("modified_at"),
            "name": obj.get("name"),
            "project_id": obj.get("project_id"),
            "project_type": obj.get("project_type"),
            "scope": obj.get("scope"),
            "type": obj.get("type"),
            "what_operand_lhs": obj.get("what_operand_lhs"),
            "what_operand_rhs": obj.get("what_operand_rhs"),
            "what_operator": obj.get("what_operator"),
            "when_operand_lhs": obj.get("when_operand_lhs"),
            "when_operand_rhs": obj.get("when_operand_rhs"),
            "when_operator": obj.get("when_operator")
        })
        return _obj


