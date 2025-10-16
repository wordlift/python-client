# AuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates if the audit was successful | [optional] 
**data** | [**AuditData**](AuditData.md) |  | [optional] 

## Example

```python
from wordlift_client.models.audit_response import AuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditResponse from a JSON string
audit_response_instance = AuditResponse.from_json(json)
# print the JSON string representation of the object
print(AuditResponse.to_json())

# convert the object into a dict
audit_response_dict = audit_response_instance.to_dict()
# create an instance of AuditResponse from a dict
audit_response_from_dict = AuditResponse.from_dict(audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


