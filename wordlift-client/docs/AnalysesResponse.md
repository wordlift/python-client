# AnalysesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysesResponseItem]**](AnalysesResponseItem.md) |  | [optional] 

## Example

```python
from Wordlift_client.models.analyses_response import AnalysesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysesResponse from a JSON string
analyses_response_instance = AnalysesResponse.from_json(json)
# print the JSON string representation of the object
print(AnalysesResponse.to_json())

# convert the object into a dict
analyses_response_dict = analyses_response_instance.to_dict()
# create an instance of AnalysesResponse from a dict
analyses_response_from_dict = AnalysesResponse.from_dict(analyses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


