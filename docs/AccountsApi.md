# wordlift_client.AccountsApi

All URIs are relative to *https://api.wordlift.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{id} | Get an account.
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /accounts | List
[**update_account**](AccountsApi.md#update_account) | **PUT** /accounts/{id} | Update an account.


# **get_account**
> Account get_account(id)

Get an account.

Get the account

### Example


```python
import wordlift_client
from wordlift_client.models.account import Account
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountsApi(api_client)
    id = 56 # int | 

    try:
        # Get an account.
        api_response = await api_instance.get_account(id)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> PageActiveAccount list_accounts(cursor=cursor, limit=limit, can_content_generation=can_content_generation, include_entity_count=include_entity_count, include_all_accounts=include_all_accounts, include_subscription=include_subscription, url=url, ng_dataset_id=ng_dataset_id)

List

List the accounts

### Example


```python
import wordlift_client
from wordlift_client.models.page_active_account import PageActiveAccount
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountsApi(api_client)
    cursor = 'cursor_example' # str | The cursor (optional)
    limit = 10 # int |  (optional) (default to 10)
    can_content_generation = True # bool | Filter accounts that can or cannot do Content Generation (optional)
    include_entity_count = False # bool | Add entity count data (optional) (default to False)
    include_all_accounts = False # bool | Include all the accounts the user has access to (optional) (default to False)
    include_subscription = False # bool | Include the subscription data (optional) (default to False)
    url = 'url_example' # str | The URL (optional)
    ng_dataset_id = 'ng_dataset_id_example' # str | The dataset id (optional)

    try:
        # List
        api_response = await api_instance.list_accounts(cursor=cursor, limit=limit, can_content_generation=can_content_generation, include_entity_count=include_entity_count, include_all_accounts=include_all_accounts, include_subscription=include_subscription, url=url, ng_dataset_id=ng_dataset_id)
        print("The response of AccountsApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **can_content_generation** | **bool**| Filter accounts that can or cannot do Content Generation | [optional] 
 **include_entity_count** | **bool**| Add entity count data | [optional] [default to False]
 **include_all_accounts** | **bool**| Include all the accounts the user has access to | [optional] [default to False]
 **include_subscription** | **bool**| Include the subscription data | [optional] [default to False]
 **url** | **str**| The URL | [optional] 
 **ng_dataset_id** | **str**| The dataset id | [optional] 

### Return type

[**PageActiveAccount**](PageActiveAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wordlift.accounts+json;version=1

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Account update_account(id, update_account_request)

Update an account.

Update the account

### Example


```python
import wordlift_client
from wordlift_client.models.account import Account
from wordlift_client.models.update_account_request import UpdateAccountRequest
from wordlift_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io
# See configuration.py for a list of all supported configuration parameters.
configuration = wordlift_client.Configuration(
    host = "https://api.wordlift.io"
)


# Enter a context with an instance of the API client
async with wordlift_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wordlift_client.AccountsApi(api_client)
    id = 56 # int | 
    update_account_request = wordlift_client.UpdateAccountRequest() # UpdateAccountRequest | 

    try:
        # Update an account.
        api_response = await api_instance.update_account(id, update_account_request)
        print("The response of AccountsApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_account_request** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found |  -  |
**401** | Authentication Failure |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

