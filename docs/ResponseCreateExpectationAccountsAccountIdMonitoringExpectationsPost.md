# ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.response_create_expectation_accounts_account_id_monitoring_expectations_post import ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost from a JSON string
response_create_expectation_accounts_account_id_monitoring_expectations_post_instance = ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost.to_json())

# convert the object into a dict
response_create_expectation_accounts_account_id_monitoring_expectations_post_dict = response_create_expectation_accounts_account_id_monitoring_expectations_post_instance.to_dict()
# create an instance of ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost from a dict
response_create_expectation_accounts_account_id_monitoring_expectations_post_from_dict = ResponseCreateExpectationAccountsAccountIdMonitoringExpectationsPost.from_dict(response_create_expectation_accounts_account_id_monitoring_expectations_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


