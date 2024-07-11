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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ContentGeneration(BaseModel):
    """
    A Content Generation project.
    """ # noqa: E501
    account_id: StrictInt = Field(description="The Account id bound to this Content Generation.")
    created_at: Optional[datetime] = Field(default=None, description="The create date-time.")
    deleted: StrictBool = Field(description="True if the project has been deleted.")
    deleted_at: Optional[datetime] = Field(default=None, description="The delete date-time.")
    graphql_query: StrictStr = Field(description="The GraphQL query which will be used to import entity data from the Knowledge Graph.")
    id: Optional[StrictInt] = Field(default=None, description="The unique id.")
    max_tokens: Optional[Annotated[int, Field(le=2000, strict=True, ge=0)]] = Field(default=64, description="The maximum number of tokens.")
    min_words: Optional[StrictInt] = Field(default=None, description="Minimum amount of words per completion")
    model_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=1, description="The model ID.")
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time.")
    name: Annotated[str, Field(min_length=0, strict=True, max_length=250)] = Field(description="The name.")
    penalty: Optional[Union[Annotated[float, Field(le=1.9, strict=True, ge=0.5)], Annotated[int, Field(le=1, strict=True, ge=1)]]] = Field(default=0.5, description="The penalty score.")
    prompt_template: Optional[StrictStr] = Field(default=None, description="The prompt template.")
    stop: Optional[StrictStr] = Field(default='###', description="The stop sequence.")
    temperature: Optional[Union[Annotated[float, Field(le=0.8, strict=True, ge=0.4)], Annotated[int, Field(le=0, strict=True, ge=1)]]] = Field(default=0.4, description="The temperature score.")
    words_to_ignore: Optional[List[StrictStr]] = Field(default=None, description="Words to ignore when checking for words not in prompt.")
    __properties: ClassVar[List[str]] = ["account_id", "created_at", "deleted", "deleted_at", "graphql_query", "id", "max_tokens", "min_words", "model_id", "modified_at", "name", "penalty", "prompt_template", "stop", "temperature", "words_to_ignore"]

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
        """Create an instance of ContentGeneration from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "deleted_at",
            "id",
            "modified_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentGeneration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_id": obj.get("account_id"),
            "created_at": obj.get("created_at"),
            "deleted": obj.get("deleted") if obj.get("deleted") is not None else False,
            "deleted_at": obj.get("deleted_at"),
            "graphql_query": obj.get("graphql_query"),
            "id": obj.get("id"),
            "max_tokens": obj.get("max_tokens") if obj.get("max_tokens") is not None else 64,
            "min_words": obj.get("min_words"),
            "model_id": obj.get("model_id") if obj.get("model_id") is not None else 1,
            "modified_at": obj.get("modified_at"),
            "name": obj.get("name"),
            "penalty": obj.get("penalty") if obj.get("penalty") is not None else 0.5,
            "prompt_template": obj.get("prompt_template"),
            "stop": obj.get("stop") if obj.get("stop") is not None else '###',
            "temperature": obj.get("temperature") if obj.get("temperature") is not None else 0.4,
            "words_to_ignore": obj.get("words_to_ignore")
        })
        return _obj


