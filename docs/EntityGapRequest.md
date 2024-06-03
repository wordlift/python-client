# EntityGapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to analyze. | 
**query** | **str** | The search query to analyze. | 
**model** | **str** | The model | [optional] 
**number_of_entities** | **int** | Number of entities to highlight. | [optional] [default to 5]
**query_location_name** | **str** | The location name for the query, e.g. United Kingdom. | [optional] [default to 'United States']
**query_search_engine** | **str** | The search engine domain for the query, if not set will be chosen according to &#x60;query_location_name&#x60; | [optional] [default to 'google.com']

## Example

```python
from wordlift_client.models.entity_gap_request import EntityGapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EntityGapRequest from a JSON string
entity_gap_request_instance = EntityGapRequest.from_json(json)
# print the JSON string representation of the object
print(EntityGapRequest.to_json())

# convert the object into a dict
entity_gap_request_dict = entity_gap_request_instance.to_dict()
# create an instance of EntityGapRequest from a dict
entity_gap_request_from_dict = EntityGapRequest.from_dict(entity_gap_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


