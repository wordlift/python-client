# DomainValidationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_domain** | **str** | The dataset domain, e.g. data.example.org | 
**dataset_name** | **str** | The dataset name, e.g. my-dataset-name | 

## Example

```python
from Wordlift_client.models.domain_validation_request import DomainValidationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainValidationRequest from a JSON string
domain_validation_request_instance = DomainValidationRequest.from_json(json)
# print the JSON string representation of the object
print(DomainValidationRequest.to_json())

# convert the object into a dict
domain_validation_request_dict = domain_validation_request_instance.to_dict()
# create an instance of DomainValidationRequest from a dict
domain_validation_request_from_dict = DomainValidationRequest.from_dict(domain_validation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


