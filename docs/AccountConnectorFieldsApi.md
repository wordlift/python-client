# wordlift_client.AccountConnectorFieldsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_field**](AccountConnectorFieldsApi.md#delete_field) | **DELETE** /accounts/{account_id}/oauth2/connectors/{connector_id}/fields/{field_name} | Delete account connector field
[**fields**](AccountConnectorFieldsApi.md#fields) | **GET** /accounts/{account_id}/oauth2/connectors/{connector_id}/fields | List account connector fields
[**put_field**](AccountConnectorFieldsApi.md#put_field) | **PUT** /accounts/{account_id}/oauth2/connectors/{connector_id}/fields/{field_name} | Save account connector field


# **delete_field**
> delete_field(account_id, connector_id, field_name)

Delete account connector field

Delete a configured field for an account Data Source connector.

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
    api_instance = wordlift_client.AccountConnectorFieldsApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 
    field_name = 'field_name_example' # str | 

    try:
        # Delete account connector field
        await api_instance.delete_field(account_id, connector_id, field_name)
    except Exception as e:
        print("Exception when calling AccountConnectorFieldsApi->delete_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 
 **field_name** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fields**
> Dict[str, str] fields(account_id, connector_id)

List account connector fields

List configured fields for an account Data Source connector.

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
    api_instance = wordlift_client.AccountConnectorFieldsApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 

    try:
        # List account connector fields
        api_response = await api_instance.fields(account_id, connector_id)
        print("The response of AccountConnectorFieldsApi->fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountConnectorFieldsApi->fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 

### Return type

**Dict[str, str]**

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

# **put_field**
> put_field(account_id, connector_id, field_name, field_value_request)

Save account connector field

Create or replace a configured field for an account Data Source connector.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.field_value_request import FieldValueRequest
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
    api_instance = wordlift_client.AccountConnectorFieldsApi(api_client)
    account_id = 56 # int | 
    connector_id = 'connector_id_example' # str | 
    field_name = 'field_name_example' # str | 
    field_value_request = wordlift_client.FieldValueRequest() # FieldValueRequest | 

    try:
        # Save account connector field
        await api_instance.put_field(account_id, connector_id, field_name, field_value_request)
    except Exception as e:
        print("Exception when calling AccountConnectorFieldsApi->put_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**|  | 
 **connector_id** | **str**|  | 
 **field_name** | **str**|  | 
 **field_value_request** | [**FieldValueRequest**](FieldValueRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

