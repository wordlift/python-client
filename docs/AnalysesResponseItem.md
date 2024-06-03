# AnalysesResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text matching the entity. | [optional] 
**confidence** | **float** | The confidence score this is the right entity. | [optional] 
**occurrences** | **int** | The number of occurrences. | [optional] 
**serp_position** | **int** | The position of the entity in SERP. &#x60;null&#x60; if not applicable. | [optional] 
**entity_id** | **str** | The entity id (URI). | [optional] 
**entity_label** | **str** | The entity label. | [optional] 
**entity_type** | **str** | The entity type. | [optional] 
**entity_description** | **str** | The entity description. | [optional] 

## Example

```python
from wordlift_client.models.analyses_response_item import AnalysesResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysesResponseItem from a JSON string
analyses_response_item_instance = AnalysesResponseItem.from_json(json)
# print the JSON string representation of the object
print(AnalysesResponseItem.to_json())

# convert the object into a dict
analyses_response_item_dict = analyses_response_item_instance.to_dict()
# create an instance of AnalysesResponseItem from a dict
analyses_response_item_from_dict = AnalysesResponseItem.from_dict(analyses_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


