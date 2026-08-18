# Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.response200_create_expectation_accounts_account_id_monitoring_expectations_post import Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost

# TODO update the JSON string below
json = "{}"
# create an instance of Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost from a JSON string
response200_create_expectation_accounts_account_id_monitoring_expectations_post_instance = Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost.from_json(json)
# print the JSON string representation of the object
print(Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost.to_json())

# convert the object into a dict
response200_create_expectation_accounts_account_id_monitoring_expectations_post_dict = response200_create_expectation_accounts_account_id_monitoring_expectations_post_instance.to_dict()
# create an instance of Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost from a dict
response200_create_expectation_accounts_account_id_monitoring_expectations_post_from_dict = Response200CreateExpectationAccountsAccountIdMonitoringExpectationsPost.from_dict(response200_create_expectation_accounts_account_id_monitoring_expectations_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


