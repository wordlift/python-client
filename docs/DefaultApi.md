# wordlift_client.DefaultApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_account_id_web_page_import_batches_post**](DefaultApi.md#create_batch_account_id_web_page_import_batches_post) | **POST** /{account_id}/web-page-import-batches | Create a new batch of web page imports
[**get_batch_account_id_web_page_import_batches_batch_id_get**](DefaultApi.md#get_batch_account_id_web_page_import_batches_batch_id_get) | **GET** /{account_id}/web-page-import-batches/{batch_id} | Get Batch


# **create_batch_account_id_web_page_import_batches_post**
> BatchResponse create_batch_account_id_web_page_import_batches_post(account_id, web_page_imports_batch_request)

Create a new batch of web page imports

Start importing a batch of URLs asynchronously into the Knowledge Graph.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.batch_response import BatchResponse
from wordlift_client.models.web_page_imports_batch_request import WebPageImportsBatchRequest
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
    api_instance = wordlift_client.DefaultApi(api_client)
    account_id = 'account_id_example' # str | 
    web_page_imports_batch_request = wordlift_client.WebPageImportsBatchRequest() # WebPageImportsBatchRequest | 

    try:
        # Create a new batch of web page imports
        api_response = await api_instance.create_batch_account_id_web_page_import_batches_post(account_id, web_page_imports_batch_request)
        print("The response of DefaultApi->create_batch_account_id_web_page_import_batches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_batch_account_id_web_page_import_batches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **web_page_imports_batch_request** | [**WebPageImportsBatchRequest**](WebPageImportsBatchRequest.md)|  | 

### Return type

[**BatchResponse**](BatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_account_id_web_page_import_batches_batch_id_get**
> BatchResponse get_batch_account_id_web_page_import_batches_batch_id_get(batch_id, account_id)

Get Batch

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.batch_response import BatchResponse
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
    api_instance = wordlift_client.DefaultApi(api_client)
    batch_id = 'batch_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # Get Batch
        api_response = await api_instance.get_batch_account_id_web_page_import_batches_batch_id_get(batch_id, account_id)
        print("The response of DefaultApi->get_batch_account_id_web_page_import_batches_batch_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_batch_account_id_web_page_import_batches_batch_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**BatchResponse**](BatchResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

