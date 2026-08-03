# ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**config** | [**StructuredDataExpectationConfig**](StructuredDataExpectationConfig.md) |  | 

## Example

```python
from wordlift_client.models.response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get import ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet from a JSON string
response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get_instance = ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet.from_json(json)
# print the JSON string representation of the object
print(ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet.to_json())

# convert the object into a dict
response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get_dict = response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get_instance.to_dict()
# create an instance of ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet from a dict
response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get_from_dict = ResponseGetExpectationAccountsAccountIdMonitoringExpectationsExpectationIdGet.from_dict(response_get_expectation_accounts_account_id_monitoring_expectations_expectation_id_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


