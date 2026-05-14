# ChunksetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_properties** | **List[str]** |  | [optional] 
**chunking_strategy** | **str** |  | [optional] 
**entity_filters** | **str** |  | [optional] 
**index_properties** | **List[str]** |  | [optional] 
**slug** | **str** |  | [optional] 
**vector_model** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.chunkset_request import ChunksetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChunksetRequest from a JSON string
chunkset_request_instance = ChunksetRequest.from_json(json)
# print the JSON string representation of the object
print(ChunksetRequest.to_json())

# convert the object into a dict
chunkset_request_dict = chunkset_request_instance.to_dict()
# create an instance of ChunksetRequest from a dict
chunkset_request_from_dict = ChunksetRequest.from_dict(chunkset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


