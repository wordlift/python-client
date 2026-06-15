# wordlift_client.AccountOAuth2ConnectorControllerApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorization**](AccountOAuth2ConnectorControllerApi.md#authorization) | **GET** /accounts/{account_id}/oauth2/connectors/{connector_id}/authorization | 
[**create_authorization_request**](AccountOAuth2ConnectorControllerApi.md#create_authorization_request) | **POST** /accounts/{account_id}/oauth2/connectors/{connector_id}/authorization-requests | 
[**delete_authorization**](AccountOAuth2ConnectorControllerApi.md#delete_authorization) | **DELETE** /accounts/{account_id}/oauth2/connectors/{connector_id}/authorization | 


# **authorization**
> OAuth2ConnectorAuthorizationResponse authorization(account_id, connector_id)



### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_connector_authorization_response import OAuth2ConnectorAuthorizationResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountOAuth2ConnectorControllerApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 

    try:
        api_response = await api_instance.authorization(account_id, connector_id)
        print("The response of AccountOAuth2ConnectorControllerApi->authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountOAuth2ConnectorControllerApi->authorization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 

### Return type

[**OAuth2ConnectorAuthorizationResponse**](OAuth2ConnectorAuthorizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_request**
> OAuth2ConnectorAuthorizationRequestResponse create_authorization_request(account_id, connector_id, o_auth2_connector_authorization_request)



### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_connector_authorization_request import OAuth2ConnectorAuthorizationRequest
from wordlift_client.models.o_auth2_connector_authorization_request_response import OAuth2ConnectorAuthorizationRequestResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountOAuth2ConnectorControllerApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 
    o_auth2_connector_authorization_request = wordlift_client.OAuth2ConnectorAuthorizationRequest() # OAuth2ConnectorAuthorizationRequest | 

    try:
        api_response = await api_instance.create_authorization_request(account_id, connector_id, o_auth2_connector_authorization_request)
        print("The response of AccountOAuth2ConnectorControllerApi->create_authorization_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountOAuth2ConnectorControllerApi->create_authorization_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 
 **o_auth2_connector_authorization_request** | [**OAuth2ConnectorAuthorizationRequest**](OAuth2ConnectorAuthorizationRequest.md)|  | 

### Return type

[**OAuth2ConnectorAuthorizationRequestResponse**](OAuth2ConnectorAuthorizationRequestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization**
> delete_authorization(account_id, connector_id)



### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountOAuth2ConnectorControllerApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 

    try:
        await api_instance.delete_authorization(account_id, connector_id)
    except Exception as e:
        print("Exception when calling AccountOAuth2ConnectorControllerApi->delete_authorization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

