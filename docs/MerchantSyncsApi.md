# wordlift_client.MerchantSyncsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sync**](MerchantSyncsApi.md#create_sync) | **POST** /merchants/{merchantId}/syncs | Start
[**get_merchant_sync**](MerchantSyncsApi.md#get_merchant_sync) | **GET** /merchants/{merchantId}/syncs/{id} | Get by id
[**list_merchant_syncs**](MerchantSyncsApi.md#list_merchant_syncs) | **GET** /merchants/{merchantId}/syncs | List


# **create_sync**
> MerchantSync create_sync(merchant_id)

Start

### Example


```python
import wordlift_client
from wordlift_client.models.merchant_sync import MerchantSync
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
    api_instance = wordlift_client.MerchantSyncsApi(api_client)
    merchant_id = 56 # int | The Merchant's `id`

    try:
        # Start
        api_response = await api_instance.create_sync(merchant_id)
        print("The response of MerchantSyncsApi->create_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantSyncsApi->create_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The Merchant&#39;s &#x60;id&#x60; | 

### Return type

[**MerchantSync**](MerchantSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merchant_sync**
> MerchantSync get_merchant_sync(merchant_id, id)

Get by id

### Example


```python
import wordlift_client
from wordlift_client.models.merchant_sync import MerchantSync
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
    api_instance = wordlift_client.MerchantSyncsApi(api_client)
    merchant_id = 56 # int | The Merchant's `id`
    id = 56 # int | The Merchant Sync `id`.

    try:
        # Get by id
        api_response = await api_instance.get_merchant_sync(merchant_id, id)
        print("The response of MerchantSyncsApi->get_merchant_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantSyncsApi->get_merchant_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The Merchant&#39;s &#x60;id&#x60; | 
 **id** | **int**| The Merchant Sync &#x60;id&#x60;. | 

### Return type

[**MerchantSync**](MerchantSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merchant_syncs**
> PageMerchantSync list_merchant_syncs(merchant_id, cursor=cursor, limit=limit, sort=sort)

List

List the Merchants Syncs

### Example


```python
import wordlift_client
from wordlift_client.models.page_merchant_sync import PageMerchantSync
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
    api_instance = wordlift_client.MerchantSyncsApi(api_client)
    merchant_id = 56 # int | The Merchant's `id`
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)
    sort = '+id' # str | The sorting, `+id` or `-id` (optional) (default to '+id')

    try:
        # List
        api_response = await api_instance.list_merchant_syncs(merchant_id, cursor=cursor, limit=limit, sort=sort)
        print("The response of MerchantSyncsApi->list_merchant_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantSyncsApi->list_merchant_syncs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| The Merchant&#39;s &#x60;id&#x60; | 
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]
 **sort** | **str**| The sorting, &#x60;+id&#x60; or &#x60;-id&#x60; | [optional] [default to &#39;+id&#39;]

### Return type

[**PageMerchantSync**](PageMerchantSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

