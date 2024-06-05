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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.validation_result import ValidationResult
from wordlift_client.models.word_repetition_data import WordRepetitionData
from typing import Optional, Set
from typing_extensions import Self

class Record(BaseModel):
    """
    Record
    """ # noqa: E501
    completion: Optional[StrictStr] = None
    content_generation_id: StrictInt = Field(description="The parent content generation id.")
    data: Optional[Dict[str, Any]] = Field(default=None, description="The data from knowledge graph after applying the graphql query.")
    errors: Optional[List[ValidationResult]] = Field(default=None, description="The set of errors found for record.")
    has_upvote: StrictBool = Field(description="This indicates whether the user upvoted the completion.")
    id: Optional[StrictInt] = None
    is_accepted: StrictBool = Field(description="This indicates whether the completion is accepted by the user.")
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time.")
    not_in_prompt_words: Optional[List[StrictStr]] = Field(default=None, description="Words in completion that are not in the prompt.")
    prompt: StrictStr = Field(description="The prompt.")
    repeated_words: Optional[Dict[str, WordRepetitionData]] = Field(default=None, description="Words in completion which are repeated.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the record, whether it's accepted, with errors, with warnings or valid.")
    validated_at: Optional[datetime] = Field(default=None, description="The last validation date-time.")
    warnings: Optional[List[ValidationResult]] = Field(default=None, description="The set of errors found for record.")
    __properties: ClassVar[List[str]] = ["completion", "content_generation_id", "data", "errors", "has_upvote", "id", "is_accepted", "modified_at", "not_in_prompt_words", "prompt", "repeated_words", "status", "validated_at", "warnings"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['accepted', 'warnings', 'errors', 'valid']):
            raise ValueError("must be one of enum values ('accepted', 'warnings', 'errors', 'valid')")
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
        """Create an instance of Record from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "content_generation_id",
            "data",
            "errors",
            "modified_at",
            "not_in_prompt_words",
            "repeated_words",
            "status",
            "validated_at",
            "warnings",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in repeated_words (dict)
        _field_dict = {}
        if self.repeated_words:
            for _key in self.repeated_words:
                if self.repeated_words[_key]:
                    _field_dict[_key] = self.repeated_words[_key].to_dict()
            _dict['repeated_words'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Record from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion": obj.get("completion"),
            "content_generation_id": obj.get("content_generation_id"),
            "data": obj.get("data"),
            "errors": [ValidationResult.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "has_upvote": obj.get("has_upvote"),
            "id": obj.get("id"),
            "is_accepted": obj.get("is_accepted"),
            "modified_at": obj.get("modified_at"),
            "not_in_prompt_words": obj.get("not_in_prompt_words"),
            "prompt": obj.get("prompt"),
            "repeated_words": dict(
                (_k, WordRepetitionData.from_dict(_v))
                for _k, _v in obj["repeated_words"].items()
            )
            if obj.get("repeated_words") is not None
            else None,
            "status": obj.get("status"),
            "validated_at": obj.get("validated_at"),
            "warnings": [ValidationResult.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None
        })
        return _obj


