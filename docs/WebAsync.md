# WebAsync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**completed** | **datetime** |  | [optional] 
**delivered** | **datetime** |  | [optional] 
**method** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**callback** | **str** |  | [optional] 
**remote_address** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.web_async import WebAsync

# TODO update the JSON string below
json = "{}"
# create an instance of WebAsync from a JSON string
web_async_instance = WebAsync.from_json(json)
# print the JSON string representation of the object
print(WebAsync.to_json())

# convert the object into a dict
web_async_dict = web_async_instance.to_dict()
# create an instance of WebAsync from a dict
web_async_from_dict = WebAsync.from_dict(web_async_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


