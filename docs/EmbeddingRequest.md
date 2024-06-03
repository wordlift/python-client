# EmbeddingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graphql_query** | **str** |  | [optional] 
**properties** | **List[str]** |  | [optional] 

## Example

```python
from wordlift_client.models.embedding_request import EmbeddingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingRequest from a JSON string
embedding_request_instance = EmbeddingRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddingRequest.to_json())

# convert the object into a dict
embedding_request_dict = embedding_request_instance.to_dict()
# create an instance of EmbeddingRequest from a dict
embedding_request_from_dict = EmbeddingRequest.from_dict(embedding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


