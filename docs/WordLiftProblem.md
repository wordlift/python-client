# WordLiftProblem

WordLift's own RFC 7807 problem-details answer, passed through as-is when it rejects the key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.word_lift_problem import WordLiftProblem

# TODO update the JSON string below
json = "{}"
# create an instance of WordLiftProblem from a JSON string
word_lift_problem_instance = WordLiftProblem.from_json(json)
# print the JSON string representation of the object
print(WordLiftProblem.to_json())

# convert the object into a dict
word_lift_problem_dict = word_lift_problem_instance.to_dict()
# create an instance of WordLiftProblem from a dict
word_lift_problem_from_dict = WordLiftProblem.from_dict(word_lift_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


