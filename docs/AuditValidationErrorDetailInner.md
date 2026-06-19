# AuditValidationErrorDetailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | **List[str]** |  | [optional] 
**msg** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.audit_validation_error_detail_inner import AuditValidationErrorDetailInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuditValidationErrorDetailInner from a JSON string
audit_validation_error_detail_inner_instance = AuditValidationErrorDetailInner.from_json(json)
# print the JSON string representation of the object
print(AuditValidationErrorDetailInner.to_json())

# convert the object into a dict
audit_validation_error_detail_inner_dict = audit_validation_error_detail_inner_instance.to_dict()
# create an instance of AuditValidationErrorDetailInner from a dict
audit_validation_error_detail_inner_from_dict = AuditValidationErrorDetailInner.from_dict(audit_validation_error_detail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


