# coding: utf-8

"""
    Embeddings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AnchorText(BaseModel):
    """
    The Anchor Text request.
    """ # noqa: E501
    actual_prompt_template: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = Field(default=False, description="Whether to enable Anchor Text, by default false.")
    max_characters: Optional[StrictInt] = Field(default=15, description="The maximum anchor text length, by default 15 characters.")
    model: Optional[StrictStr] = Field(default='gpt-4', description="The model to use.")
    prompt_template: Optional[StrictStr] = Field(default='''As an SEO and content editor, your task is to create a concise and appropriate anchor text to enhance keyword targeting, using the
provided keyword and page title. Ensure to maintain a neutral tone and adhere to the examples below for guidance:

{%- for anchor in anchors -%}
- Title: {{ anchor.title }}
- Keyword: {{ anchor.keyword }}
- Anchor text: {{ anchor.anchor_text }}
{%- endfor -%}
''', description="The prompt template, we provide a default. Liquid template language is supported.")
    __properties: ClassVar[List[str]] = ["actual_prompt_template", "enabled", "max_characters", "model", "prompt_template"]

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
        """Create an instance of AnchorText from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "actual_prompt_template",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnchorText from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actual_prompt_template": obj.get("actual_prompt_template"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "max_characters": obj.get("max_characters") if obj.get("max_characters") is not None else 15,
            "model": obj.get("model") if obj.get("model") is not None else 'gpt-4',
            "prompt_template": obj.get("prompt_template") if obj.get("prompt_template") is not None else '''As an SEO and content editor, your task is to create a concise and appropriate anchor text to enhance keyword targeting, using the
provided keyword and page title. Ensure to maintain a neutral tone and adhere to the examples below for guidance:

{%- for anchor in anchors -%}
- Title: {{ anchor.title }}
- Keyword: {{ anchor.keyword }}
- Anchor text: {{ anchor.anchor_text }}
{%- endfor -%}
'''
        })
        return _obj


