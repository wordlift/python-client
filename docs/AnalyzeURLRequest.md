# AnalyzeURLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to analyze | 
**num_queries** | **int** | Number of synthetic queries to generate | [optional] [default to 10]
**coverage_threshold** | **float** | The threshold for answering synthetic queries | [optional] [default to 0.65]

## Example

```python
from wordlift_client.models.analyze_url_request import AnalyzeURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeURLRequest from a JSON string
analyze_url_request_instance = AnalyzeURLRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyzeURLRequest.to_json())

# convert the object into a dict
analyze_url_request_dict = analyze_url_request_instance.to_dict()
# create an instance of AnalyzeURLRequest from a dict
analyze_url_request_from_dict = AnalyzeURLRequest.from_dict(analyze_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


