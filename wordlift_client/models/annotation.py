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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.entity_match import EntityMatch
from typing import Optional, Set
from typing_extensions import Self

class Annotation(BaseModel):
    """
    Object representing single annotation.
    """ # noqa: E501
    annotation_id: Optional[StrictStr] = Field(default=None, description="An unique id.", alias="annotationId")
    start: Optional[StrictInt] = Field(default=None, description="The starting posistion of annotation in content (zero-indexed & non negative ).")
    end: Optional[StrictInt] = Field(default=None, description="The ending posistion of annotation in content (zero-indexed & non negative ).")
    text: Optional[StrictStr] = Field(default=None, description="The annotated text.")
    entity_matches: Optional[List[EntityMatch]] = Field(default=None, description="The list of entities which the annotation matches.", alias="entityMatches")
    __properties: ClassVar[List[str]] = ["annotationId", "start", "end", "text", "entityMatches"]

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
        """Create an instance of Annotation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entity_matches (list)
        _items = []
        if self.entity_matches:
            for _item in self.entity_matches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entityMatches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Annotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annotationId": obj.get("annotationId"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "text": obj.get("text"),
            "entityMatches": [EntityMatch.from_dict(_item) for _item in obj["entityMatches"]] if obj.get("entityMatches") is not None else None
        })
        return _obj


