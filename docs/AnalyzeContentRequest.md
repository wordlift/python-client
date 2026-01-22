# AnalyzeContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**num_queries** | **int** | Number of synthetic queries to generate | [optional] [default to 10]
**coverage_threshold** | **float** | The threshold for answering synthetic queries | [optional] [default to 0.65]

## Example

```python
from wordlift_client.models.analyze_content_request import AnalyzeContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeContentRequest from a JSON string
analyze_content_request_instance = AnalyzeContentRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyzeContentRequest.to_json())

# convert the object into a dict
analyze_content_request_dict = analyze_content_request_instance.to_dict()
# create an instance of AnalyzeContentRequest from a dict
analyze_content_request_from_dict = AnalyzeContentRequest.from_dict(analyze_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


