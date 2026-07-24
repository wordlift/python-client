# wordlift_client.QuestionAndAnswerSetsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_question_and_answer_sets**](QuestionAndAnswerSetsApi.md#create_question_and_answer_sets) | **POST** /content-optimizations/questions-and-answers-sets | Create
[**delete_question_and_answer_set**](QuestionAndAnswerSetsApi.md#delete_question_and_answer_set) | **DELETE** /content-optimizations/questions-and-answers-sets/{id} | Delete
[**get_question_and_answer_sets**](QuestionAndAnswerSetsApi.md#get_question_and_answer_sets) | **GET** /content-optimizations/questions-and-answers-sets | Get
[**update_question_and_answer_set**](QuestionAndAnswerSetsApi.md#update_question_and_answer_set) | **PUT** /content-optimizations/questions-and-answers-sets/{id} | Update


# **create_question_and_answer_sets**
> SmartContentProject create_question_and_answer_sets(smart_content_request)

Create

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.smart_content_project import SmartContentProject
from wordlift_client.models.smart_content_request import SmartContentRequest
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
    api_instance = wordlift_client.QuestionAndAnswerSetsApi(api_client)
    smart_content_request = wordlift_client.SmartContentRequest() # SmartContentRequest | 

    try:
        # Create
        api_response = await api_instance.create_question_and_answer_sets(smart_content_request)
        print("The response of QuestionAndAnswerSetsApi->create_question_and_answer_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAndAnswerSetsApi->create_question_and_answer_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_content_request** | [**SmartContentRequest**](SmartContentRequest.md)|  | 

### Return type

[**SmartContentProject**](SmartContentProject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question_and_answer_set**
> delete_question_and_answer_set(id)

Delete

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.QuestionAndAnswerSetsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete
        await api_instance.delete_question_and_answer_set(id)
    except Exception as e:
        print("Exception when calling QuestionAndAnswerSetsApi->delete_question_and_answer_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | OK |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_and_answer_sets**
> List[QuestionAndAnswerSet] get_question_and_answer_sets(iri=iri, smart_content_project_id=smart_content_project_id)

Get

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer_set import QuestionAndAnswerSet
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
    api_instance = wordlift_client.QuestionAndAnswerSetsApi(api_client)
    iri = 'iri_example' # str | The webpage IRI (optional)
    smart_content_project_id = 56 # int | The smart content id. (optional)

    try:
        # Get
        api_response = await api_instance.get_question_and_answer_sets(iri=iri, smart_content_project_id=smart_content_project_id)
        print("The response of QuestionAndAnswerSetsApi->get_question_and_answer_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAndAnswerSetsApi->get_question_and_answer_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**| The webpage IRI | [optional] 
 **smart_content_project_id** | **int**| The smart content id. | [optional] 

### Return type

[**List[QuestionAndAnswerSet]**](QuestionAndAnswerSet.md)

### Authorization

[ApiKey](../README.md#ApiKey)

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

# **update_question_and_answer_set**
> QuestionAndAnswerSet update_question_and_answer_set(id, question_and_answer_set)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer_set import QuestionAndAnswerSet
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
    api_instance = wordlift_client.QuestionAndAnswerSetsApi(api_client)
    id = 'id_example' # str | 
    question_and_answer_set = wordlift_client.QuestionAndAnswerSet() # QuestionAndAnswerSet | 

    try:
        # Update
        api_response = await api_instance.update_question_and_answer_set(id, question_and_answer_set)
        print("The response of QuestionAndAnswerSetsApi->update_question_and_answer_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionAndAnswerSetsApi->update_question_and_answer_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **question_and_answer_set** | [**QuestionAndAnswerSet**](QuestionAndAnswerSet.md)|  | 

### Return type

[**QuestionAndAnswerSet**](QuestionAndAnswerSet.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

