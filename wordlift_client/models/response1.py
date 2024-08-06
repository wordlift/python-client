# coding: utf-8

"""
    Manager

    Subscription management and related services.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.annotation import Annotation
from wordlift_client.models.entity import Entity
from wordlift_client.models.image import Image
from wordlift_client.models.topic import Topic
from typing import Optional, Set
from typing_extensions import Self

class Response1(BaseModel):
    """
    Response
    """ # noqa: E501
    entities: Optional[Dict[str, Entity]] = Field(default=None, description="A map of entity URI to the respective entity.")
    annotations: Optional[Dict[str, Annotation]] = Field(default=None, description="A map of annotation id to the respective annotation.")
    images: Optional[List[Image]] = Field(default=None, description="A list of images.")
    languages: Optional[List[StrictStr]] = Field(default=None, description="A list of languages.")
    topics: Optional[List[Topic]] = Field(default=None, description="A list of topics.")
    content: Optional[StrictStr] = Field(default=None, description="The text supplied for analysis.")
    __properties: ClassVar[List[str]] = ["entities", "annotations", "images", "languages", "topics", "content"]

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
        # override the default output from pydantic by calling `to_dict()` of each value in entities (dict)
        _field_dict = {}
        if self.entities:
            for _key in self.entities:
                if self.entities[_key]:
                    _field_dict[_key] = self.entities[_key].to_dict()
            _dict['entities'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in annotations (dict)
        _field_dict = {}
        if self.annotations:
            for _key in self.annotations:
                if self.annotations[_key]:
                    _field_dict[_key] = self.annotations[_key].to_dict()
            _dict['annotations'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in topics (list)
        _items = []
        if self.topics:
            for _item in self.topics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Response1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entities": dict(
                (_k, Entity.from_dict(_v))
                for _k, _v in obj["entities"].items()
            )
            if obj.get("entities") is not None
            else None,
            "annotations": dict(
                (_k, Annotation.from_dict(_v))
                for _k, _v in obj["annotations"].items()
            )
            if obj.get("annotations") is not None
            else None,
            "images": [Image.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "languages": obj.get("languages"),
            "topics": [Topic.from_dict(_item) for _item in obj["topics"]] if obj.get("topics") is not None else None,
            "content": obj.get("content")
        })
        return _obj


