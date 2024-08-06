# wordlift_client.QuestionsAndAnswersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_question_and_answer**](QuestionsAndAnswersApi.md#create_question_and_answer) | **POST** /questions-and-answers | Create
[**create_questions_and_answers_collection**](QuestionsAndAnswersApi.md#create_questions_and_answers_collection) | **POST** /questions-and-answers-collection | Create
[**delete_question_and_answer**](QuestionsAndAnswersApi.md#delete_question_and_answer) | **DELETE** /questions-and-answers/{id} | Delete
[**delete_questions_and_answers_collection**](QuestionsAndAnswersApi.md#delete_questions_and_answers_collection) | **DELETE** /questions-and-answers-collection | Delete
[**get_questions_and_answers**](QuestionsAndAnswersApi.md#get_questions_and_answers) | **GET** /questions-and-answers | Get
[**update_question_and_answer**](QuestionsAndAnswersApi.md#update_question_and_answer) | **PUT** /questions-and-answers/{id} | Update
[**update_questions_and_answers_collection**](QuestionsAndAnswersApi.md#update_questions_and_answers_collection) | **PUT** /questions-and-answers-collection | Update


# **create_question_and_answer**
> QuestionAndAnswer create_question_and_answer(question_and_answer_request)

Create

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer import QuestionAndAnswer
from wordlift_client.models.question_and_answer_request import QuestionAndAnswerRequest
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    question_and_answer_request = wordlift_client.QuestionAndAnswerRequest() # QuestionAndAnswerRequest | 

    try:
        # Create
        api_response = await api_instance.create_question_and_answer(question_and_answer_request)
        print("The response of QuestionsAndAnswersApi->create_question_and_answer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->create_question_and_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_and_answer_request** | [**QuestionAndAnswerRequest**](QuestionAndAnswerRequest.md)|  | 

### Return type

[**QuestionAndAnswer**](QuestionAndAnswer.md)

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

# **create_questions_and_answers_collection**
> SmartContent create_questions_and_answers_collection(smart_content_request)

Create

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.smart_content import SmartContent
from wordlift_client.models.smart_content_request import SmartContentRequest
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    smart_content_request = wordlift_client.SmartContentRequest() # SmartContentRequest | 

    try:
        # Create
        api_response = await api_instance.create_questions_and_answers_collection(smart_content_request)
        print("The response of QuestionsAndAnswersApi->create_questions_and_answers_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->create_questions_and_answers_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_content_request** | [**SmartContentRequest**](SmartContentRequest.md)|  | 

### Return type

[**SmartContent**](SmartContent.md)

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

# **delete_question_and_answer**
> delete_question_and_answer(id)

Delete

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    id = 56 # int | 

    try:
        # Delete
        await api_instance.delete_question_and_answer(id)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->delete_question_and_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**200** | Found. |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questions_and_answers_collection**
> delete_questions_and_answers_collection(smart_content_id)

Delete

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    smart_content_id = 56 # int | 

    try:
        # Delete
        await api_instance.delete_questions_and_answers_collection(smart_content_id)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->delete_questions_and_answers_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_content_id** | **int**|  | 

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

# **get_questions_and_answers**
> List[QuestionAndAnswer] get_questions_and_answers(account_id=account_id, iri=iri, smart_content_id=smart_content_id)

Get

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer import QuestionAndAnswer
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    account_id = 56 # int | The account id. (optional)
    iri = 'iri_example' # str | The webpage IRI (optional)
    smart_content_id = 56 # int | The smart content id. (optional)

    try:
        # Get
        api_response = await api_instance.get_questions_and_answers(account_id=account_id, iri=iri, smart_content_id=smart_content_id)
        print("The response of QuestionsAndAnswersApi->get_questions_and_answers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->get_questions_and_answers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The account id. | [optional] 
 **iri** | **str**| The webpage IRI | [optional] 
 **smart_content_id** | **int**| The smart content id. | [optional] 

### Return type

[**List[QuestionAndAnswer]**](QuestionAndAnswer.md)

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

# **update_question_and_answer**
> QuestionAndAnswer update_question_and_answer(id, update_question_and_answer_request)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer import QuestionAndAnswer
from wordlift_client.models.update_question_and_answer_request import UpdateQuestionAndAnswerRequest
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    id = 56 # int | 
    update_question_and_answer_request = wordlift_client.UpdateQuestionAndAnswerRequest() # UpdateQuestionAndAnswerRequest | 

    try:
        # Update
        api_response = await api_instance.update_question_and_answer(id, update_question_and_answer_request)
        print("The response of QuestionsAndAnswersApi->update_question_and_answer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->update_question_and_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_question_and_answer_request** | [**UpdateQuestionAndAnswerRequest**](UpdateQuestionAndAnswerRequest.md)|  | 

### Return type

[**QuestionAndAnswer**](QuestionAndAnswer.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questions_and_answers_collection**
> List[QuestionAndAnswer] update_questions_and_answers_collection(question_and_answer_request)

Update

### Example

* Api Key Authentication (ApiKey):

```python
import wordlift_client
from wordlift_client.models.question_and_answer import QuestionAndAnswer
from wordlift_client.models.question_and_answer_request import QuestionAndAnswerRequest
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
    api_instance = wordlift_client.QuestionsAndAnswersApi(api_client)
    question_and_answer_request = wordlift_client.QuestionAndAnswerRequest() # QuestionAndAnswerRequest | 

    try:
        # Update
        api_response = await api_instance.update_questions_and_answers_collection(question_and_answer_request)
        print("The response of QuestionsAndAnswersApi->update_questions_and_answers_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsAndAnswersApi->update_questions_and_answers_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_and_answer_request** | [**QuestionAndAnswerRequest**](QuestionAndAnswerRequest.md)|  | 

### Return type

[**List[QuestionAndAnswer]**](QuestionAndAnswer.md)

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

