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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.network_account_info import NetworkAccountInfo
from typing import Optional, Set
from typing_extensions import Self

class AccountInfo(BaseModel):
    """
    Account Information
    """ # noqa: E501
    account_id: StrictInt = Field(description="The Account Id", alias="accountId")
    dataset_id: Optional[StrictStr] = Field(default=None, description="The Dataset Id", alias="datasetId")
    dataset_uri: StrictStr = Field(description="The dataset URI", alias="datasetUri")
    features: Optional[Dict[str, StrictBool]] = Field(default=None, description="A list of features enabled or disabled for the account")
    google_search_console_site_url: Optional[StrictStr] = Field(default=None, description="Google Search Console Site URL", alias="googleSearchConsoleSiteUrl")
    key: Optional[StrictStr] = Field(default=None, description="The Key")
    language: Optional[StrictStr] = Field(default=None, description="The language code")
    networks: List[NetworkAccountInfo] = Field(description="A list of connected Account Information")
    ng_dataset_id: Optional[StrictStr] = Field(default=None, alias="ngDatasetId")
    subscription_id: StrictInt = Field(description="The Subscription Id", alias="subscriptionId")
    url: Optional[StrictStr] = Field(default=None, description="The website URL")
    wp_admin: Optional[StrictStr] = Field(default=None, description="If WordPress, the WP-ADMIN URL", alias="wpAdmin")
    wp_json: Optional[StrictStr] = Field(default=None, description="If WordPress, the WP-JSON end-point", alias="wpJson")
    __properties: ClassVar[List[str]] = ["accountId", "datasetId", "datasetUri", "features", "googleSearchConsoleSiteUrl", "key", "language", "networks", "ngDatasetId", "subscriptionId", "url", "wpAdmin", "wpJson"]

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
        """Create an instance of AccountInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "account_id",
            "dataset_id",
            "dataset_uri",
            "features",
            "google_search_console_site_url",
            "key",
            "language",
            "networks",
            "subscription_id",
            "url",
            "wp_admin",
            "wp_json",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in networks (list)
        _items = []
        if self.networks:
            for _item in self.networks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['networks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "datasetId": obj.get("datasetId"),
            "datasetUri": obj.get("datasetUri"),
            "features": obj.get("features"),
            "googleSearchConsoleSiteUrl": obj.get("googleSearchConsoleSiteUrl"),
            "key": obj.get("key"),
            "language": obj.get("language"),
            "networks": [NetworkAccountInfo.from_dict(_item) for _item in obj["networks"]] if obj.get("networks") is not None else None,
            "ngDatasetId": obj.get("ngDatasetId"),
            "subscriptionId": obj.get("subscriptionId"),
            "url": obj.get("url"),
            "wpAdmin": obj.get("wpAdmin"),
            "wpJson": obj.get("wpJson")
        })
        return _obj


