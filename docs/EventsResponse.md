# EventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Event]**](Event.md) |  | [optional] 
**var_self** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**prev** | **str** |  | [optional] 
**last** | **str** |  | [optional] 
**first** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.events_response import EventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventsResponse from a JSON string
events_response_instance = EventsResponse.from_json(json)
# print the JSON string representation of the object
print(EventsResponse.to_json())

# convert the object into a dict
events_response_dict = events_response_instance.to_dict()
# create an instance of EventsResponse from a dict
events_response_from_dict = EventsResponse.from_dict(events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


