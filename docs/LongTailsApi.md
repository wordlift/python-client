# wordlift_client.LongTailsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get2**](LongTailsApi.md#get2) | **GET** /longtail | Get entities
[**get3**](LongTailsApi.md#get3) | **GET** /longtail/hook | Get entities by rank (async)
[**get_v2**](LongTailsApi.md#get_v2) | **GET** /longtail/v2 | Get entities by rank


# **get2**
> LongtailResponse get2(q, ln, lc, sd, sc=sc, d=d)

Get entities

Query for long tail opportunities and receive entities.

### Example


```python
import wordlift_client
from wordlift_client.models.longtail_response import LongtailResponse
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.LongTailsApi(api_client)
    q = 'q_example' # str | The Longtail query
    ln = 'London,England,United Kingdom' # str | A location name, origin of the search
    lc = 'en' # str | Language Code
    sd = 'google.co.uk, google.com.au, google.de, etc.' # str | Search Domain
    sc = 'sc_example' # str | Analysis Scope (optional)
    d = '10' # str | The maximum number of results to analyze (optional) (default to '10')

    try:
        # Get entities
        api_response = await api_instance.get2(q, ln, lc, sd, sc=sc, d=d)
        print("The response of LongTailsApi->get2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongTailsApi->get2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The Longtail query | 
 **ln** | **str**| A location name, origin of the search | 
 **lc** | **str**| Language Code | 
 **sd** | **str**| Search Domain | 
 **sc** | **str**| Analysis Scope | [optional] 
 **d** | **str**| The maximum number of results to analyze | [optional] [default to &#39;10&#39;]

### Return type

[**LongtailResponse**](LongtailResponse.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get3**
> get3(q, ln, lc, sd, hk, sc=sc, d=d)

Get entities by rank (async)

Query for long tail opportunities and receive entities along with their position in SERP.

### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.LongTailsApi(api_client)
    q = 'q_example' # str | The Longtail query
    ln = 'London,England,United Kingdom' # str | A location name, origin of the search
    lc = 'en' # str | Language Code
    sd = 'google.co.uk, google.com.au, google.de, etc.' # str | Search Domain
    hk = 'hk_example' # str | Webhook URL
    sc = 'sc_example' # str | Analysis Scope (optional)
    d = '10' # str | The maximum number of results to analyze (optional) (default to '10')

    try:
        # Get entities by rank (async)
        await api_instance.get3(q, ln, lc, sd, hk, sc=sc, d=d)
    except Exception as e:
        print("Exception when calling LongTailsApi->get3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The Longtail query | 
 **ln** | **str**| A location name, origin of the search | 
 **lc** | **str**| Language Code | 
 **sd** | **str**| Search Domain | 
 **hk** | **str**| Webhook URL | 
 **sc** | **str**| Analysis Scope | [optional] 
 **d** | **str**| The maximum number of results to analyze | [optional] [default to &#39;10&#39;]

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
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2**
> List[RankEntities] get_v2(q, ln, lc, sd, sc=sc, d=d)

Get entities by rank

Query for long tail opportunities and receive entities along with their position in SERP.

### Example


```python
import wordlift_client
from wordlift_client.models.rank_entities import RankEntities
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.LongTailsApi(api_client)
    q = 'q_example' # str | The Longtail query
    ln = 'London,England,United Kingdom' # str | A location name, origin of the search
    lc = 'en' # str | Language Code
    sd = 'google.co.uk, google.com.au, google.de, etc.' # str | Search Domain
    sc = 'sc_example' # str | Analysis Scope (optional)
    d = '10' # str | The maximum number of results to analyze (optional) (default to '10')

    try:
        # Get entities by rank
        api_response = await api_instance.get_v2(q, ln, lc, sd, sc=sc, d=d)
        print("The response of LongTailsApi->get_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LongTailsApi->get_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| The Longtail query | 
 **ln** | **str**| A location name, origin of the search | 
 **lc** | **str**| Language Code | 
 **sd** | **str**| Search Domain | 
 **sc** | **str**| Analysis Scope | [optional] 
 **d** | **str**| The maximum number of results to analyze | [optional] [default to &#39;10&#39;]

### Return type

[**List[RankEntities]**](RankEntities.md)

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
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

