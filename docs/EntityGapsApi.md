# wordlift_client.EntityGapsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_gap**](EntityGapsApi.md#create_entity_gap) | **POST** /entity-gaps | Create


# **create_entity_gap**
> AnalysesResponse create_entity_gap(entity_gap_request)

Create

Create an Entity Gaps analysis.

### Example


```python
import wordlift_client
from wordlift_client.models.analyses_response import AnalysesResponse
from wordlift_client.models.entity_gap_request import EntityGapRequest
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
    api_instance = wordlift_client.EntityGapsApi(api_client)
    entity_gap_request = wordlift_client.EntityGapRequest() # EntityGapRequest | 

    try:
        # Create
        api_response = await api_instance.create_entity_gap(entity_gap_request)
        print("The response of EntityGapsApi->create_entity_gap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityGapsApi->create_entity_gap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_gap_request** | [**EntityGapRequest**](EntityGapRequest.md)|  | 

### Return type

[**AnalysesResponse**](AnalysesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**500** | Uh oh, something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

