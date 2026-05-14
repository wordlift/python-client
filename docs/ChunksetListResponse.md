# ChunksetListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChunksetResponse]**](ChunksetResponse.md) |  | [optional] 

## Example

```python
from wordlift_client.models.chunkset_list_response import ChunksetListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChunksetListResponse from a JSON string
chunkset_list_response_instance = ChunksetListResponse.from_json(json)
# print the JSON string representation of the object
print(ChunksetListResponse.to_json())

# convert the object into a dict
chunkset_list_response_dict = chunkset_list_response_instance.to_dict()
# create an instance of ChunksetListResponse from a dict
chunkset_list_response_from_dict = ChunksetListResponse.from_dict(chunkset_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


