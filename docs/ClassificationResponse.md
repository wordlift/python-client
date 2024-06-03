# ClassificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 
**scores** | **List[float]** |  | [optional] 

## Example

```python
from wordlift_client.models.classification_response import ClassificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationResponse from a JSON string
classification_response_instance = ClassificationResponse.from_json(json)
# print the JSON string representation of the object
print(ClassificationResponse.to_json())

# convert the object into a dict
classification_response_dict = classification_response_instance.to_dict()
# create an instance of ClassificationResponse from a dict
classification_response_from_dict = ClassificationResponse.from_dict(classification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


