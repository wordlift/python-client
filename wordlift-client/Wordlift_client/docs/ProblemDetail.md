# ProblemDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 
**status** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from Wordlift_client.models.problem_detail import ProblemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetail from a JSON string
problem_detail_instance = ProblemDetail.from_json(json)
# print the JSON string representation of the object
print(ProblemDetail.to_json())

# convert the object into a dict
problem_detail_dict = problem_detail_instance.to_dict()
# create an instance of ProblemDetail from a dict
problem_detail_from_dict = ProblemDetail.from_dict(problem_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


