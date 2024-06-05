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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wordlift_client.models.account_subscription import AccountSubscription
from wordlift_client.models.diagnostic_plugin import DiagnosticPlugin
from typing import Optional, Set
from typing_extensions import Self

class ActiveAccount(BaseModel):
    """
    An array of objects.
    """ # noqa: E501
    country: Optional[StrictStr] = None
    diagnostic_plugins: Optional[List[DiagnosticPlugin]] = None
    domain_uri: Optional[StrictStr] = None
    google_search_console_site_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_wordpress: Optional[StrictBool] = None
    key: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    ng_dataset_id: Optional[StrictStr] = None
    package_type: Optional[StrictStr] = None
    subscription: Optional[AccountSubscription] = None
    subscription_id: Optional[StrictInt] = None
    total_entities: Optional[StrictInt] = None
    total_entities_with_schema_url: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    user_id: Optional[StrictInt] = None
    wp_admin: Optional[StrictStr] = None
    wp_include_exclude_default: Optional[StrictStr] = None
    wp_json: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["country", "diagnostic_plugins", "domain_uri", "google_search_console_site_url", "id", "is_wordpress", "key", "language", "ng_dataset_id", "package_type", "subscription", "subscription_id", "total_entities", "total_entities_with_schema_url", "url", "user_id", "wp_admin", "wp_include_exclude_default", "wp_json"]

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
        """Create an instance of ActiveAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in diagnostic_plugins (list)
        _items = []
        if self.diagnostic_plugins:
            for _item in self.diagnostic_plugins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['diagnostic_plugins'] = _items
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActiveAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "country": obj.get("country"),
            "diagnostic_plugins": [DiagnosticPlugin.from_dict(_item) for _item in obj["diagnostic_plugins"]] if obj.get("diagnostic_plugins") is not None else None,
            "domain_uri": obj.get("domain_uri"),
            "google_search_console_site_url": obj.get("google_search_console_site_url"),
            "id": obj.get("id"),
            "is_wordpress": obj.get("is_wordpress"),
            "key": obj.get("key"),
            "language": obj.get("language"),
            "ng_dataset_id": obj.get("ng_dataset_id"),
            "package_type": obj.get("package_type"),
            "subscription": AccountSubscription.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "subscription_id": obj.get("subscription_id"),
            "total_entities": obj.get("total_entities"),
            "total_entities_with_schema_url": obj.get("total_entities_with_schema_url"),
            "url": obj.get("url"),
            "user_id": obj.get("user_id"),
            "wp_admin": obj.get("wp_admin"),
            "wp_include_exclude_default": obj.get("wp_include_exclude_default"),
            "wp_json": obj.get("wp_json")
        })
        return _obj


