# ContentStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**semantic_html_score** | **int** | Score for semantic HTML usage (0-10) | [optional] 

## Example

```python
from wordlift_client.models.content_structure import ContentStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStructure from a JSON string
content_structure_instance = ContentStructure.from_json(json)
# print the JSON string representation of the object
print(ContentStructure.to_json())

# convert the object into a dict
content_structure_dict = content_structure_instance.to_dict()
# create an instance of ContentStructure from a dict
content_structure_from_dict = ContentStructure.from_dict(content_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


