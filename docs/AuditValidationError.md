# AuditValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[AuditValidationErrorDetailInner]**](AuditValidationErrorDetailInner.md) |  | [optional] 

## Example

```python
from wordlift_client.models.audit_validation_error import AuditValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AuditValidationError from a JSON string
audit_validation_error_instance = AuditValidationError.from_json(json)
# print the JSON string representation of the object
print(AuditValidationError.to_json())

# convert the object into a dict
audit_validation_error_dict = audit_validation_error_instance.to_dict()
# create an instance of AuditValidationError from a dict
audit_validation_error_from_dict = AuditValidationError.from_dict(audit_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


