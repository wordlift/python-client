# SmartContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The account id. | 
**model_id** | **int** | The model id. | [optional] [default to 1]
**rules** | [**List[RuleRequest]**](RuleRequest.md) |  | [optional] 
**webpage_properties** | [**List[WebpageProperties]**](WebpageProperties.md) |  | [optional] 

## Example

```python
from wordlift_client.models.smart_content_request import SmartContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContentRequest from a JSON string
smart_content_request_instance = SmartContentRequest.from_json(json)
# print the JSON string representation of the object
print(SmartContentRequest.to_json())

# convert the object into a dict
smart_content_request_dict = smart_content_request_instance.to_dict()
# create an instance of SmartContentRequest from a dict
smart_content_request_from_dict = SmartContentRequest.from_dict(smart_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


