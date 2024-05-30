# ContentGenerationRequest

The Content Generation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The account id bound to this content generation. | 
**deleted** | **bool** | The deleted flag. | [optional] [default to False]
**graphql_query** | **str** | The GraphQL query which will be used to import entity data from the Knowledge Graph. | 
**max_tokens** | **int** | The maximum number of tokens. | [optional] [default to 64]
**min_words** | **int** | Minimum amount of words per completion. | [optional] [default to 0]
**model_id** | **int** | The model ID. | [optional] [default to 1]
**name** | **str** | The model name. | 
**penalty** | **float** | The penalty score. | [optional] [default to 0.5]
**prompt_template** | **str** | The prompt template. | [optional] 
**stop** | **str** | The stop sequence. | [optional] [default to '###']
**temperature** | **float** | The temperature score. | [optional] [default to 0.4]
**words_to_ignore** | **List[str]** | Words to ignore when checking for words not in prompt. | [optional] 

## Example

```python
from Wordlift_client.models.content_generation_request import ContentGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationRequest from a JSON string
content_generation_request_instance = ContentGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationRequest.to_json())

# convert the object into a dict
content_generation_request_dict = content_generation_request_instance.to_dict()
# create an instance of ContentGenerationRequest from a dict
content_generation_request_from_dict = ContentGenerationRequest.from_dict(content_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


