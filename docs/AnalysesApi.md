# wordlift_client.AnalysesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyse**](AnalysesApi.md#analyse) | **POST** /single | Analyse content
[**create**](AnalysesApi.md#create) | **POST** /analysis/analyses | Create
[**merge**](AnalysesApi.md#merge) | **POST** /merge | Analyse and Merge
[**v2_analysis**](AnalysesApi.md#v2_analysis) | **POST** /v2/analyze | Analyse Web Page


# **analyse**
> Response1 analyse(request1)

Analyse content

Analyze the content provided with the request.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.request1 import Request1
from wordlift_client.models.response1 import Response1
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.AnalysesApi(api_client)
    request1 = wordlift_client.Request1() # Request1 | 

    try:
        # Analyse content
        api_response = await api_instance.analyse(request1)
        print("The response of AnalysesApi->analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request1** | [**Request1**](Request1.md)|  | 

### Return type

[**Response1**](Response1.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> AnalysesResponse create(analyses_request)

Create

Create an analysis request

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.analyses_request import AnalysesRequest
from wordlift_client.models.analyses_response import AnalysesResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.AnalysesApi(api_client)
    analyses_request = wordlift_client.AnalysesRequest() # AnalysesRequest | 

    try:
        # Create
        api_response = await api_instance.create(analyses_request)
        print("The response of AnalysesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyses_request** | [**AnalysesRequest**](AnalysesRequest.md)|  | 

### Return type

[**AnalysesResponse**](AnalysesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x.wordlift.analysis+json;version=3

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**500** | Uh oh, something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge**
> str merge(request1)

Analyse and Merge

Analyze content and return the results merged as HTML code.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.request1 import Request1
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.AnalysesApi(api_client)
    request1 = wordlift_client.Request1() # Request1 | 

    try:
        # Analyse and Merge
        api_response = await api_instance.merge(request1)
        print("The response of AnalysesApi->merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request1** | [**Request1**](Request1.md)|  | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication Failure |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_analysis**
> Response1 v2_analysis(request1)

Analyse Web Page

Analyse the content of a webpage by using the `url` property of the request.

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.request1 import Request1
from wordlift_client.models.response1 import Response1
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
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
    api_instance = wordlift_client.AnalysesApi(api_client)
    request1 = wordlift_client.Request1() # Request1 | 

    try:
        # Analyse Web Page
        api_response = await api_instance.v2_analysis(request1)
        print("The response of AnalysesApi->v2_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->v2_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request1** | [**Request1**](Request1.md)|  | 

### Return type

[**Response1**](Response1.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

