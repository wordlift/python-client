# EmbeddingRequest

A request to generate the embeddings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model used to generate the embeddings. | [optional] [default to 'nomic-ai/nomic-embed-text-v1']
**properties** | **List[str]** | The list of properties to use to generate the embeddings. | [optional] 

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


