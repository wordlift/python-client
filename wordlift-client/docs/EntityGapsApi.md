# Wordlift_client.EntityGapsApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_gap**](EntityGapsApi.md#create_entity_gap) | **POST** /entity-gaps | Create


# **create_entity_gap**
> AnalysesResponse create_entity_gap(entity_gap_request)

Create

Create an Entity Gaps analysis.

### Example

* Api Key Authentication (ApiKey):

```python
import Wordlift_client
from Wordlift_client.models.analyses_response import AnalysesResponse
from Wordlift_client.models.entity_gap_request import EntityGapRequest
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
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
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.EntityGapsApi(api_client)
    entity_gap_request = Wordlift_client.EntityGapRequest() # EntityGapRequest | 

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

[ApiKey](../README.md#ApiKey)

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

