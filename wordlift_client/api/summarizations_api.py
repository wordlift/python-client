# coding: utf-8

"""
    WordLift API

    WordLift API

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing import Dict, Optional, Union
from typing_extensions import Annotated

from wordlift_client.api_client import ApiClient, RequestSerialized
from wordlift_client.api_response import ApiResponse
from wordlift_client.rest import RESTResponseType


class SummarizationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def microdata_to_json_ld_using_post(
        self,
        body: Annotated[StrictStr, Field(description="body")],
        max_length: Annotated[Optional[StrictInt], Field(description="Maximum text length")] = None,
        min_length: Annotated[Optional[StrictInt], Field(description="Minimum text length")] = None,
        ratio: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Ratio")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Dict[str, str]:
        """Create


        :param body: body (required)
        :type body: str
        :param max_length: Maximum text length
        :type max_length: int
        :param min_length: Minimum text length
        :type min_length: int
        :param ratio: Ratio
        :type ratio: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._microdata_to_json_ld_using_post_serialize(
            body=body,
            max_length=max_length,
            min_length=min_length,
            ratio=ratio,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, str]",
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def microdata_to_json_ld_using_post_with_http_info(
        self,
        body: Annotated[StrictStr, Field(description="body")],
        max_length: Annotated[Optional[StrictInt], Field(description="Maximum text length")] = None,
        min_length: Annotated[Optional[StrictInt], Field(description="Minimum text length")] = None,
        ratio: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Ratio")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Dict[str, str]]:
        """Create


        :param body: body (required)
        :type body: str
        :param max_length: Maximum text length
        :type max_length: int
        :param min_length: Minimum text length
        :type min_length: int
        :param ratio: Ratio
        :type ratio: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._microdata_to_json_ld_using_post_serialize(
            body=body,
            max_length=max_length,
            min_length=min_length,
            ratio=ratio,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, str]",
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def microdata_to_json_ld_using_post_without_preload_content(
        self,
        body: Annotated[StrictStr, Field(description="body")],
        max_length: Annotated[Optional[StrictInt], Field(description="Maximum text length")] = None,
        min_length: Annotated[Optional[StrictInt], Field(description="Minimum text length")] = None,
        ratio: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Ratio")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create


        :param body: body (required)
        :type body: str
        :param max_length: Maximum text length
        :type max_length: int
        :param min_length: Minimum text length
        :type min_length: int
        :param ratio: Ratio
        :type ratio: float
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._microdata_to_json_ld_using_post_serialize(
            body=body,
            max_length=max_length,
            min_length=min_length,
            ratio=ratio,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, str]",
            '201': None,
            '401': None,
            '403': None,
            '404': None,
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _microdata_to_json_ld_using_post_serialize(
        self,
        body,
        max_length,
        min_length,
        ratio,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if max_length is not None:
            
            _query_params.append(('max_length', max_length))
            
        if min_length is not None:
            
            _query_params.append(('min_length', min_length))
            
        if ratio is not None:
            
            _query_params.append(('ratio', ratio))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/ld+json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'text/plain'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'ApiKey'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/summarize',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


