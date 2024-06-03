# wordlift_client.ContentGenerationWordBiasesApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_word**](ContentGenerationWordBiasesApi.md#create_word) | **POST** /content-generations/{contentGenerationId}/words | Create
[**create_words**](ContentGenerationWordBiasesApi.md#create_words) | **PUT** /content-generations/{contentGenerationId}/words | Update for prompt
[**create_words_from_csv**](ContentGenerationWordBiasesApi.md#create_words_from_csv) | **PUT** /content-generations/{contentGenerationId}/words/imports | Update from CSV
[**delete_word**](ContentGenerationWordBiasesApi.md#delete_word) | **DELETE** /content-generations/{contentGenerationId}/words/{id} | Delete
[**list_words**](ContentGenerationWordBiasesApi.md#list_words) | **GET** /content-generations/{contentGenerationId}/words | List
[**update_word**](ContentGenerationWordBiasesApi.md#update_word) | **PUT** /content-generations/{contentGenerationId}/words/{id} | Update


# **create_word**
> Word create_word(content_generation_id, word_request)

Create

### Example


```python
import wordlift_client
from wordlift_client.models.word import Word
from wordlift_client.models.word_request import WordRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    word_request = wordlift_client.WordRequest() # WordRequest | 

    try:
        # Create
        api_response = await api_instance.create_word(content_generation_id, word_request)
        print("The response of ContentGenerationWordBiasesApi->create_word:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->create_word: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **word_request** | [**WordRequest**](WordRequest.md)|  | 

### Return type

[**Word**](Word.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_words**
> List[Word] create_words(content_generation_id, word_request=word_request)

Update for prompt

Send a list of word biases for this prompt. Existing words will be deleted.

### Example


```python
import wordlift_client
from wordlift_client.models.word import Word
from wordlift_client.models.word_request import WordRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    word_request = [wordlift_client.WordRequest()] # List[WordRequest] |  (optional)

    try:
        # Update for prompt
        api_response = await api_instance.create_words(content_generation_id, word_request=word_request)
        print("The response of ContentGenerationWordBiasesApi->create_words:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->create_words: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **word_request** | [**List[WordRequest]**](WordRequest.md)|  | [optional] 

### Return type

[**List[Word]**](Word.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_words_from_csv**
> create_words_from_csv(content_generation_id, body, content_type=content_type)

Update from CSV

### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    body = 'body_example' # str | 
    content_type = 'content_type_example' # str |  (optional)

    try:
        # Update from CSV
        await api_instance.create_words_from_csv(content_generation_id, body, content_type=content_type)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->create_words_from_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **body** | **str**|  | 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_word**
> delete_word(content_generation_id, id)

Delete

### Example


```python
import wordlift_client
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    id = 56 # int | The Word to delete.

    try:
        # Delete
        await api_instance.delete_word(content_generation_id, id)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->delete_word: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **id** | **int**| The Word to delete. | 

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
**200** | Created |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_words**
> PageWord list_words(content_generation_id, the_cursor_=the_cursor_, the_maximum_number_of_results_=the_maximum_number_of_results_)

List

### Example


```python
import wordlift_client
from wordlift_client.models.page_word import PageWord
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    the_cursor_ = 'the_cursor__example' # str |  (optional)
    the_maximum_number_of_results_ = 10 # int |  (optional) (default to 10)

    try:
        # List
        api_response = await api_instance.list_words(content_generation_id, the_cursor_=the_cursor_, the_maximum_number_of_results_=the_maximum_number_of_results_)
        print("The response of ContentGenerationWordBiasesApi->list_words:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->list_words: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **the_cursor_** | **str**|  | [optional] 
 **the_maximum_number_of_results_** | **int**|  | [optional] [default to 10]

### Return type

[**PageWord**](PageWord.md)

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

# **update_word**
> Word update_word(content_generation_id, id, word_request)

Update

### Example


```python
import wordlift_client
from wordlift_client.models.word import Word
from wordlift_client.models.word_request import WordRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.ContentGenerationWordBiasesApi(api_client)
    content_generation_id = 56 # int | The Content Generation id.
    id = 56 # int | The Word bias to update.
    word_request = wordlift_client.WordRequest() # WordRequest | 

    try:
        # Update
        api_response = await api_instance.update_word(content_generation_id, id, word_request)
        print("The response of ContentGenerationWordBiasesApi->update_word:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationWordBiasesApi->update_word: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_id** | **int**| The Content Generation id. | 
 **id** | **int**| The Word bias to update. | 
 **word_request** | [**WordRequest**](WordRequest.md)|  | 

### Return type

[**Word**](Word.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

