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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class WebsiteSearch(BaseModel):
    """
    Search Data
    """ # noqa: E501
    clicks: StrictInt = Field(description="Number of clicks.")
    ctr: Union[StrictFloat, StrictInt] = Field(description="CTR.")
    id: StrictInt = Field(description="The id: it's now a unique id, but a row index.")
    impressions: StrictInt = Field(description="Number of impressions.")
    keys: List[StrictStr] = Field(description="The keys for the current data, matching the provided `dimensions` in the query.")
    position: Union[StrictFloat, StrictInt] = Field(description="Position.")
    score: Union[StrictFloat, StrictInt] = Field(description="A score to spot traffic opportunities, from 0.0 to 1.0 (the higher the better). The score is based on the traffic data.")
    __properties: ClassVar[List[str]] = ["clicks", "ctr", "id", "impressions", "keys", "position", "score"]

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
        """Create an instance of WebsiteSearch from a JSON string"""
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
        """Create an instance of WebsiteSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clicks": obj.get("clicks"),
            "ctr": obj.get("ctr"),
            "id": obj.get("id"),
            "impressions": obj.get("impressions"),
            "keys": obj.get("keys"),
            "position": obj.get("position"),
            "score": obj.get("score")
        })
        return _obj


