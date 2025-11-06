# CreateUrlInspectionRequest

A URL inspection request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to analyze. | 

## Example

```python
from wordlift_client.models.create_url_inspection_request import CreateUrlInspectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUrlInspectionRequest from a JSON string
create_url_inspection_request_instance = CreateUrlInspectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUrlInspectionRequest.to_json())

# convert the object into a dict
create_url_inspection_request_dict = create_url_inspection_request_instance.to_dict()
# create an instance of CreateUrlInspectionRequest from a dict
create_url_inspection_request_from_dict = CreateUrlInspectionRequest.from_dict(create_url_inspection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


