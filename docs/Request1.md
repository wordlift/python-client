# Request1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion** | **str** |  | [optional] 
**has_upvote** | **bool** | This indicates whether the user upvoted the completion. | 
**is_accepted** | **bool** | This indicates whether the completion is accepted by the user. | 
**validated_at** | **datetime** | Validation time of the record - null to revalidate. | [optional] 

## Example

```python
from wordlift-client.models.request1 import Request1

# TODO update the JSON string below
json = "{}"
# create an instance of Request1 from a JSON string
request1_instance = Request1.from_json(json)
# print the JSON string representation of the object
print(Request1.to_json())

# convert the object into a dict
request1_dict = request1_instance.to_dict()
# create an instance of Request1 from a dict
request1_from_dict = Request1.from_dict(request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


