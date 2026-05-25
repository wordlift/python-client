# wordlift_client.OAuth2ConnectorsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_error**](OAuth2ConnectorsApi.md#authorize_error) | **GET** /oauth2/connectors/{connectorId}/authorize/complete | Complete OAuth2 connector authorization
[**connectors**](OAuth2ConnectorsApi.md#connectors) | **GET** /oauth2/connectors | List OAuth2 connectors


# **authorize_error**
> authorize_error(connector_id, error, state, code)

Complete OAuth2 connector authorization

Complete or report the result of an OAuth2 Data Source connector authorization flow.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.OAuth2ConnectorsApi(api_client)
    connector_id = 'connector_id_example' # str | 
    error = 'error_example' # str | 
    state = 'state_example' # str | 
    code = 'code_example' # str | 

    try:
        # Complete OAuth2 connector authorization
        await api_instance.authorize_error(connector_id, error, state, code)
    except Exception as e:
        print("Exception when calling OAuth2ConnectorsApi->authorize_error: %s\n" % e)
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

[ApiKey](../README.md#ApiKey)

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

List OAuth2 connectors

List OAuth2 Data Source connectors available in the platform.

### Example

* Api Key Authentication (ApiKey):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.OAuth2ConnectorsApi(api_client)

    try:
        # List OAuth2 connectors
        api_response = await api_instance.connectors()
        print("The response of OAuth2ConnectorsApi->connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ConnectorsApi->connectors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OAuth2ConnectorResponse]**](OAuth2ConnectorResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

