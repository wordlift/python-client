# wordlift_client.RulesApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_rules**](RulesApi.md#copy_rules) | **POST** /rules/copies | Copy
[**create_rule**](RulesApi.md#create_rule) | **POST** /rules | Create
[**delete_rule**](RulesApi.md#delete_rule) | **DELETE** /rules/{id} | Delete
[**list_rules**](RulesApi.md#list_rules) | **GET** /rules | List
[**update_rule**](RulesApi.md#update_rule) | **PUT** /rules/{id} | Update
[**update_rule_collection**](RulesApi.md#update_rule_collection) | **PUT** /rules-collection | Update


# **copy_rules**
> copy_rules(project_type, from_project_id, to_project_id)

Copy

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.project_type import ProjectType
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    project_type = wordlift_client.ProjectType() # ProjectType | The project type
    from_project_id = 56 # int | The source Content Generation id.
    to_project_id = 56 # int | The target Content Generation id.

    try:
        # Copy
        await api_instance.copy_rules(project_type, from_project_id, to_project_id)
    except Exception as e:
        print("Exception when calling RulesApi->copy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_type** | [**ProjectType**](.md)| The project type | 
 **from_project_id** | **int**| The source Content Generation id. | 
 **to_project_id** | **int**| The target Content Generation id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> Rule create_rule(rule_request)

Create

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.rule import Rule
from wordlift_client.models.rule_request import RuleRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    rule_request = wordlift_client.RuleRequest() # RuleRequest | 

    try:
        # Create
        api_response = await api_instance.create_rule(rule_request)
        print("The response of RulesApi->create_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->create_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_request** | [**RuleRequest**](RuleRequest.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(id)

Delete

### Example

* Api Key Authentication (ApiKeyAuth):

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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    id = 56 # int | The id

    try:
        # Delete
        await api_instance.delete_rule(id)
    except Exception as e:
        print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **list_rules**
> PageRule list_rules(cursor=cursor, limit=limit, project_id=project_id, project_type=project_type, scope=scope)

List

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.page_rule import PageRule
from wordlift_client.models.project_type import ProjectType
from wordlift_client.models.scope import Scope
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int | The maximum number of results (optional) (default to 10)
    project_id = 56 # int | The project id - if provided, must also provide the project type (optional)
    project_type = wordlift_client.ProjectType() # ProjectType | The project type - if provided, must also provide the project id (optional)
    scope = wordlift_client.Scope() # Scope | The scope (optional)

    try:
        # List
        api_response = await api_instance.list_rules(cursor=cursor, limit=limit, project_id=project_id, project_type=project_type, scope=scope)
        print("The response of RulesApi->list_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->list_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**| The maximum number of results | [optional] [default to 10]
 **project_id** | **int**| The project id - if provided, must also provide the project type | [optional] 
 **project_type** | [**ProjectType**](.md)| The project type - if provided, must also provide the project id | [optional] 
 **scope** | [**Scope**](.md)| The scope | [optional] 

### Return type

[**PageRule**](PageRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**400** | Bad request |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> Rule update_rule(id, rule_request)

Update

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.rule import Rule
from wordlift_client.models.rule_request import RuleRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    id = 56 # int | The id
    rule_request = wordlift_client.RuleRequest() # RuleRequest | 

    try:
        # Update
        api_response = await api_instance.update_rule(id, rule_request)
        print("The response of RulesApi->update_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->update_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 
 **rule_request** | [**RuleRequest**](RuleRequest.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

# **update_rule_collection**
> List[Rule] update_rule_collection(project_id, project_type, rule_request)

Update

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import wordlift_client
from wordlift_client.models.project_type import ProjectType
from wordlift_client.models.rule import Rule
from wordlift_client.models.rule_request import RuleRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.RulesApi(api_client)
    project_id = 56 # int | The project id
    project_type = wordlift_client.ProjectType() # ProjectType | The project type
    rule_request = [wordlift_client.RuleRequest()] # List[RuleRequest] | 

    try:
        # Update
        api_response = await api_instance.update_rule_collection(project_id, project_type, rule_request)
        print("The response of RulesApi->update_rule_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesApi->update_rule_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project id | 
 **project_type** | [**ProjectType**](.md)| The project type | 
 **rule_request** | [**List[RuleRequest]**](RuleRequest.md)|  | 

### Return type

[**List[Rule]**](Rule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found. |  -  |
**400** | Bad request |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

