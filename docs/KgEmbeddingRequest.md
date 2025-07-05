# KgEmbeddingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**EmbeddingRequest**](EmbeddingRequest.md) |  | 
**graphql_query** | **str** | The GraphQL query used to select entities to create embedding vectors for. | 

## Example

```python
from wordlift_client.models.kg_embedding_request import KgEmbeddingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KgEmbeddingRequest from a JSON string
kg_embedding_request_instance = KgEmbeddingRequest.from_json(json)
# print the JSON string representation of the object
print(KgEmbeddingRequest.to_json())

# convert the object into a dict
kg_embedding_request_dict = kg_embedding_request_instance.to_dict()
# create an instance of KgEmbeddingRequest from a dict
kg_embedding_request_from_dict = KgEmbeddingRequest.from_dict(kg_embedding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


