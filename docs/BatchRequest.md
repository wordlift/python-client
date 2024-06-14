# BatchRequest

A request part of a batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | The entity URI. | 
**model** | [**Graph**](Graph.md) |  | 
**private** | **bool** | Whether the entity should be hidden from Linked Data and GraphQL. | [optional] 

## Example

```python
from wordlift_client.models.batch_request import BatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequest from a JSON string
batch_request_instance = BatchRequest.from_json(json)
# print the JSON string representation of the object
print(BatchRequest.to_json())

# convert the object into a dict
batch_request_dict = batch_request_instance.to_dict()
# create an instance of BatchRequest from a dict
batch_request_from_dict = BatchRequest.from_dict(batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


