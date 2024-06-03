# Request2

The Event request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**args** | **object** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from wordlift-client.models.request2 import Request2

# TODO update the JSON string below
json = "{}"
# create an instance of Request2 from a JSON string
request2_instance = Request2.from_json(json)
# print the JSON string representation of the object
print(Request2.to_json())

# convert the object into a dict
request2_dict = request2_instance.to_dict()
# create an instance of Request2 from a dict
request2_from_dict = Request2.from_dict(request2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


