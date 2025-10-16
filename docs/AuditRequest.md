# AuditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The full URL of the website to audit | 

## Example

```python
from wordlift_client.models.audit_request import AuditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditRequest from a JSON string
audit_request_instance = AuditRequest.from_json(json)
# print the JSON string representation of the object
print(AuditRequest.to_json())

# convert the object into a dict
audit_request_dict = audit_request_instance.to_dict()
# create an instance of AuditRequest from a dict
audit_request_from_dict = AuditRequest.from_dict(audit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


