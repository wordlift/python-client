# wordlift_client.FactCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_fact_check**](FactCheckApi.md#submit_fact_check) | **POST** /fact-check/score | Submit a fact-checking request


# **submit_fact_check**
> SubmitFactCheck200Response submit_fact_check(submit_fact_check_request)

Submit a fact-checking request

### Example


```python
import wordlift_client
from wordlift_client.models.submit_fact_check200_response import SubmitFactCheck200Response
from wordlift_client.models.submit_fact_check_request import SubmitFactCheckRequest
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
    api_instance = wordlift_client.FactCheckApi(api_client)
    submit_fact_check_request = wordlift_client.SubmitFactCheckRequest() # SubmitFactCheckRequest | 

    try:
        # Submit a fact-checking request
        api_response = await api_instance.submit_fact_check(submit_fact_check_request)
        print("The response of FactCheckApi->submit_fact_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FactCheckApi->submit_fact_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_fact_check_request** | [**SubmitFactCheckRequest**](SubmitFactCheckRequest.md)|  | 

### Return type

[**SubmitFactCheck200Response**](SubmitFactCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fact-checking result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

