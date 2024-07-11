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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CompletionRequest(BaseModel):
    """
    A request for a completion.
    """ # noqa: E501
    frequency_penalty: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=-2)], Annotated[int, Field(le=2, strict=True, ge=-2)]]] = None
    logit_bias: Optional[Dict[str, StrictInt]] = None
    max_tokens: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    min_words: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    model_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    presence_penalty: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=-2)], Annotated[int, Field(le=2, strict=True, ge=-2)]]] = None
    prompt: StrictStr
    stop: Optional[StrictStr] = None
    temperature: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = None
    __properties: ClassVar[List[str]] = ["frequency_penalty", "logit_bias", "max_tokens", "min_words", "model_id", "presence_penalty", "prompt", "stop", "temperature"]

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
        """Create an instance of CompletionRequest from a JSON string"""
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
        """Create an instance of CompletionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "frequency_penalty": obj.get("frequency_penalty"),
            "logit_bias": obj.get("logit_bias"),
            "max_tokens": obj.get("max_tokens"),
            "min_words": obj.get("min_words"),
            "model_id": obj.get("model_id"),
            "presence_penalty": obj.get("presence_penalty"),
            "prompt": obj.get("prompt"),
            "stop": obj.get("stop"),
            "temperature": obj.get("temperature")
        })
        return _obj


