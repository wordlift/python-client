# ChunksetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_properties** | **List[str]** |  | [optional] 
**chunking_strategy** | **str** |  | [optional] 
**entity_filters** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**index_properties** | **List[str]** |  | [optional] 
**previous_ids** | **List[str]** |  | [optional] 
**slug** | **str** |  | [optional] 
**vector_model** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.chunkset_response import ChunksetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChunksetResponse from a JSON string
chunkset_response_instance = ChunksetResponse.from_json(json)
# print the JSON string representation of the object
print(ChunksetResponse.to_json())

# convert the object into a dict
chunkset_response_dict = chunkset_response_instance.to_dict()
# create an instance of ChunksetResponse from a dict
chunkset_response_from_dict = ChunksetResponse.from_dict(chunkset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


