# wordlift_client.VectorSearchNodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_nodes_collection**](VectorSearchNodesApi.md#update_nodes_collection) | **PUT** /vector-search/nodes-collection | Update


# **update_nodes_collection**
> update_nodes_collection(node_request)

Update

### Example


```python
import wordlift_client
from wordlift_client.models.node_request import NodeRequest
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
    api_instance = wordlift_client.VectorSearchNodesApi(api_client)
    node_request = [wordlift_client.NodeRequest()] # List[NodeRequest] | 

    try:
        # Update
        await api_instance.update_nodes_collection(node_request)
    except Exception as e:
        print("Exception when calling VectorSearchNodesApi->update_nodes_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_request** | [**List[NodeRequest]**](NodeRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

