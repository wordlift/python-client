# wordlift_client.OAuth2ConnectorControllerApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_error**](OAuth2ConnectorControllerApi.md#authorize_error) | **GET** /oauth2/connectors/{connectorId}/authorize/complete | 
[**connectors**](OAuth2ConnectorControllerApi.md#connectors) | **GET** /oauth2/connectors | 


# **authorize_error**
> authorize_error(connector_id, error, state, code)



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
    api_instance = wordlift_client.OAuth2ConnectorControllerApi(api_client)
    connector_id = 'connector_id_example' # str | 
    error = 'error_example' # str | 
    state = 'state_example' # str | 
    code = 'code_example' # str | 

    try:
        await api_instance.authorize_error(connector_id, error, state, code)
    except Exception as e:
        print("Exception when calling OAuth2ConnectorControllerApi->authorize_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **error** | **str**|  | 
 **state** | **str**|  | 
 **code** | **str**|  | 

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

# **connectors**
> List[OAuth2ConnectorResponse] connectors()



### Example


```python
import wordlift_client
from wordlift_client.models.o_auth2_connector_response import OAuth2ConnectorResponse
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
    api_instance = wordlift_client.OAuth2ConnectorControllerApi(api_client)

    try:
        api_response = await api_instance.connectors()
        print("The response of OAuth2ConnectorControllerApi->connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ConnectorControllerApi->connectors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OAuth2ConnectorResponse]**](OAuth2ConnectorResponse.md)

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

