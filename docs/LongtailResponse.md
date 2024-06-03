# LongtailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | The page summary. | [optional] 
**entities** | [**List[Entity1]**](Entity1.md) | The list of entities matching the query. | [optional] 

## Example

```python
from wordlift-client.models.longtail_response import LongtailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LongtailResponse from a JSON string
longtail_response_instance = LongtailResponse.from_json(json)
# print the JSON string representation of the object
print(LongtailResponse.to_json())

# convert the object into a dict
longtail_response_dict = longtail_response_instance.to_dict()
# create an instance of LongtailResponse from a dict
longtail_response_from_dict = LongtailResponse.from_dict(longtail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


