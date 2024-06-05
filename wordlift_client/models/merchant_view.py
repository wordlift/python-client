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
from typing import Optional, Set
from typing_extensions import Self

class MerchantView(BaseModel):
    """
    An array of objects.
    """ # noqa: E501
    access_token: StrictStr = Field(description="The Google merchant access token")
    account_id: Optional[StrictInt] = Field(default=None, description="The account id")
    automatic_synchronization: Optional[StrictBool] = Field(default=None, description="Whether the Merchant data will be synchronized automatically")
    created_at: Optional[datetime] = Field(default=None, description="The create date-time")
    dataset_domain: Optional[StrictStr] = Field(default=None, description="The custom domain (for example data.example.org)")
    dataset_name: Optional[StrictStr] = Field(default=None, description="The dataset path (for example /data)")
    deleted: StrictBool = Field(description="True if the merchant has been deleted")
    deleted_at: Optional[datetime] = Field(default=None, description="The delete date-time")
    google_merchant_id: StrictInt = Field(description="The Google Merchant id")
    id: Optional[StrictInt] = Field(default=None, description="The unique id")
    ignore_brand: Optional[StrictBool] = Field(default=None, description="Whether to ignore the `brand` property during validation")
    ignore_image: Optional[StrictBool] = Field(default=None, description="Whether to ignore the `image` property during validation")
    modified_at: Optional[datetime] = Field(default=None, description="The last modified date-time")
    publisher_name: StrictStr = Field(description="The publisher name (shows in schema publisher)")
    refresh_token: StrictStr = Field(description="The Google merchant refresh token")
    sid: Optional[StrictStr] = None
    sync_has_errors: Optional[StrictBool] = None
    sync_id: Optional[StrictInt] = None
    sync_products_created: Optional[StrictInt] = None
    sync_products_deleted: Optional[StrictInt] = None
    sync_products_errored: Optional[StrictInt] = None
    sync_products_skipped: Optional[StrictInt] = None
    sync_products_total: Optional[StrictInt] = None
    sync_products_updated: Optional[StrictInt] = None
    sync_started_at: Optional[datetime] = Field(default=None, description="The started date-time.")
    sync_stopped_at: Optional[datetime] = Field(default=None, description="The stopped date-time.")
    url: Optional[StrictStr] = Field(default=None, description="The website URL")
    writer_service: Optional[StrictStr] = Field(default=None, description="How to write the merchant data to the graph, if unsure, do not set anything (by default `wordpressMerchantWriter`).")
    __properties: ClassVar[List[str]] = ["access_token", "account_id", "automatic_synchronization", "created_at", "dataset_domain", "dataset_name", "deleted", "deleted_at", "google_merchant_id", "id", "ignore_brand", "ignore_image", "modified_at", "publisher_name", "refresh_token", "sid", "sync_has_errors", "sync_id", "sync_products_created", "sync_products_deleted", "sync_products_errored", "sync_products_skipped", "sync_products_total", "sync_products_updated", "sync_started_at", "sync_stopped_at", "url", "writer_service"]

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
        """Create an instance of MerchantView from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "account_id",
            "created_at",
            "deleted_at",
            "id",
            "modified_at",
            "sync_started_at",
            "sync_stopped_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantView from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
            "account_id": obj.get("account_id"),
            "automatic_synchronization": obj.get("automatic_synchronization"),
            "created_at": obj.get("created_at"),
            "dataset_domain": obj.get("dataset_domain"),
            "dataset_name": obj.get("dataset_name"),
            "deleted": obj.get("deleted") if obj.get("deleted") is not None else False,
            "deleted_at": obj.get("deleted_at"),
            "google_merchant_id": obj.get("google_merchant_id"),
            "id": obj.get("id"),
            "ignore_brand": obj.get("ignore_brand"),
            "ignore_image": obj.get("ignore_image"),
            "modified_at": obj.get("modified_at"),
            "publisher_name": obj.get("publisher_name"),
            "refresh_token": obj.get("refresh_token"),
            "sid": obj.get("sid"),
            "sync_has_errors": obj.get("sync_has_errors"),
            "sync_id": obj.get("sync_id"),
            "sync_products_created": obj.get("sync_products_created"),
            "sync_products_deleted": obj.get("sync_products_deleted"),
            "sync_products_errored": obj.get("sync_products_errored"),
            "sync_products_skipped": obj.get("sync_products_skipped"),
            "sync_products_total": obj.get("sync_products_total"),
            "sync_products_updated": obj.get("sync_products_updated"),
            "sync_started_at": obj.get("sync_started_at"),
            "sync_stopped_at": obj.get("sync_stopped_at"),
            "url": obj.get("url"),
            "writer_service": obj.get("writer_service")
        })
        return _obj


