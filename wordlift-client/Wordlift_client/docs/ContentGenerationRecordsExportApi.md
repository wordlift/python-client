# Wordlift_client.ContentGenerationRecordsExportApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export**](ContentGenerationRecordsExportApi.md#export) | **GET** /content-generations/{contentGenerationId}/records.tsv | 


# **export**
> List[str] export(content_generation_id)



### Example


```python
import Wordlift_client
from Wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = Wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with Wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = Wordlift_client.ContentGenerationRecordsExportApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.

    try:
        api_response = await api_instance.export(content_generation_id)
        print("The response of ContentGenerationRecordsExportApi->export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationRecordsExportApi->export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/tsv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

