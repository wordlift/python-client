# ContentGenerationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion** | **str** |  | [optional] 
**has_upvote** | **bool** | This indicates whether the user upvoted the completion. | 
**is_accepted** | **bool** | This indicates whether the completion is accepted by the user. | 
**validated_at** | **datetime** | Validation time of the record - null to revalidate. | [optional] 

## Example

```python
from wordlift_client.models.content_generation_request import ContentGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationRequest from a JSON string
content_generation_request_instance = ContentGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationRequest.to_json())

# convert the object into a dict
content_generation_request_dict = content_generation_request_instance.to_dict()
# create an instance of ContentGenerationRequest from a dict
content_generation_request_from_dict = ContentGenerationRequest.from_dict(content_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


