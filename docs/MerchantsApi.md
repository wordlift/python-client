# wordlift_client.MerchantsApi

All URIs are relative to *https://api.wordlift.io/quality-rating*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merchant**](MerchantsApi.md#create_merchant) | **POST** /merchants | Create
[**delete_merchant**](MerchantsApi.md#delete_merchant) | **DELETE** /merchants/{id} | Delete by id
[**get_merchant**](MerchantsApi.md#get_merchant) | **GET** /merchants/{id} | Get by id
[**list_merchants**](MerchantsApi.md#list_merchants) | **GET** /merchants | List
[**update_merchant**](MerchantsApi.md#update_merchant) | **PUT** /merchants/{id} | Update


# **create_merchant**
> Merchant create_merchant(merchant_request)

Create

Create a Merchant

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.merchant import Merchant
from wordlift_client.models.merchant_request import MerchantRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.MerchantsApi(api_client)
    merchant_request = wordlift_client.MerchantRequest() # MerchantRequest | 

    try:
        # Create
        api_response = await api_instance.create_merchant(merchant_request)
        print("The response of MerchantsApi->create_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->create_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_request** | [**MerchantRequest**](MerchantRequest.md)|  | 

### Return type

[**Merchant**](Merchant.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_merchant**
> delete_merchant(id)

Delete by id

Delete a Merchant by its `id`.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.MerchantsApi(api_client)
    id = 56 # int | The Merchant id

    try:
        # Delete by id
        await api_instance.delete_merchant(id)
    except Exception as e:
        print("Exception when calling MerchantsApi->delete_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Merchant id | 

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
**200** | Deleted |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant**
> Merchant get_merchant(id)

Get by id

Get a Merchant by its `id`.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.merchant import Merchant
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.MerchantsApi(api_client)
    id = 56 # int | The Merchant id

    try:
        # Get by id
        api_response = await api_instance.get_merchant(id)
        print("The response of MerchantsApi->get_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->get_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Merchant id | 

### Return type

[**Merchant**](Merchant.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merchants**
> PageMerchantView list_merchants(cursor=cursor, limit=limit, deleted=deleted)

List

List the Merchants, optionally filtering by the `deleted` flag

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.page_merchant_view import PageMerchantView
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.MerchantsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)
    deleted = True # bool | Filter by the `deleted` flag (optional)

    try:
        # List
        api_response = await api_instance.list_merchants(cursor=cursor, limit=limit, deleted=deleted)
        print("The response of MerchantsApi->list_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->list_merchants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]
 **deleted** | **bool**| Filter by the &#x60;deleted&#x60; flag | [optional] 

### Return type

[**PageMerchantView**](PageMerchantView.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merchant**
> Merchant update_merchant(id, merchant_request)

Update

Update a Merchant

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.merchant import Merchant
from wordlift_client.models.merchant_request import MerchantRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/quality-rating
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/quality-rating"
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
    api_instance = wordlift_client.MerchantsApi(api_client)
    id = 56 # int | The Merchant id
    merchant_request = wordlift_client.MerchantRequest() # MerchantRequest | 

    try:
        # Update
        api_response = await api_instance.update_merchant(id, merchant_request)
        print("The response of MerchantsApi->update_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantsApi->update_merchant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Merchant id | 
 **merchant_request** | [**MerchantRequest**](MerchantRequest.md)|  | 

### Return type

[**Merchant**](Merchant.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

