# FailureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**run_id** | **str** |  | 
**account_id** | **str** |  | 
**account_url** | **str** |  | 
**timestamp** | **datetime** |  | 
**url** | **str** |  | 
**handler_name** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from wordlift_client.models.failure_response import FailureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FailureResponse from a JSON string
failure_response_instance = FailureResponse.from_json(json)
# print the JSON string representation of the object
print(FailureResponse.to_json())

# convert the object into a dict
failure_response_dict = failure_response_instance.to_dict()
# create an instance of FailureResponse from a dict
failure_response_from_dict = FailureResponse.from_dict(failure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


