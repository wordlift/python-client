# SubmitFactCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.submit_fact_check_request import SubmitFactCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFactCheckRequest from a JSON string
submit_fact_check_request_instance = SubmitFactCheckRequest.from_json(json)
# print the JSON string representation of the object
print(SubmitFactCheckRequest.to_json())

# convert the object into a dict
submit_fact_check_request_dict = submit_fact_check_request_instance.to_dict()
# create an instance of SubmitFactCheckRequest from a dict
submit_fact_check_request_from_dict = SubmitFactCheckRequest.from_dict(submit_fact_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


