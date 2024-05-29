# CreateEmbeddingsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from Wordlift_client.models.create_embeddings_input import CreateEmbeddingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmbeddingsInput from a JSON string
create_embeddings_input_instance = CreateEmbeddingsInput.from_json(json)
# print the JSON string representation of the object
print(CreateEmbeddingsInput.to_json())

# convert the object into a dict
create_embeddings_input_dict = create_embeddings_input_instance.to_dict()
# create an instance of CreateEmbeddingsInput from a dict
create_embeddings_input_from_dict = CreateEmbeddingsInput.from_dict(create_embeddings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


