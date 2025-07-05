# KgEmbeddingResponse

Graph Embedding Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id/iri of the web page in the Graph. | 
**model** | **str** |  | 

## Example

```python
from wordlift_client.models.kg_embedding_response import KgEmbeddingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KgEmbeddingResponse from a JSON string
kg_embedding_response_instance = KgEmbeddingResponse.from_json(json)
# print the JSON string representation of the object
print(KgEmbeddingResponse.to_json())

# convert the object into a dict
kg_embedding_response_dict = kg_embedding_response_instance.to_dict()
# create an instance of KgEmbeddingResponse from a dict
kg_embedding_response_from_dict = KgEmbeddingResponse.from_dict(kg_embedding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


