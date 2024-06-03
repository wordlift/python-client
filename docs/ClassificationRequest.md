# ClassificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classes** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.classification_request import ClassificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationRequest from a JSON string
classification_request_instance = ClassificationRequest.from_json(json)
# print the JSON string representation of the object
print(ClassificationRequest.to_json())

# convert the object into a dict
classification_request_dict = classification_request_instance.to_dict()
# create an instance of ClassificationRequest from a dict
classification_request_from_dict = ClassificationRequest.from_dict(classification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


