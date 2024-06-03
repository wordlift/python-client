# ContentGeneration

A Content Generation project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The Account id bound to this Content Generation. | 
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**deleted** | **bool** | True if the project has been deleted. | [default to False]
**deleted_at** | **datetime** | The delete date-time. | [optional] [readonly] 
**graphql_query** | **str** | The GraphQL query which will be used to import entity data from the Knowledge Graph. | 
**id** | **int** | The unique id. | [optional] [readonly] 
**max_tokens** | **int** | The maximum number of tokens. | [optional] [default to 64]
**min_words** | **int** | Minimum amount of words per completion | [optional] 
**model_id** | **int** | The model ID. | [optional] [default to 1]
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**name** | **str** | The name. | 
**penalty** | **float** | The penalty score. | [optional] [default to 0.5]
**prompt_template** | **str** | The prompt template. | [optional] 
**stop** | **str** | The stop sequence. | [optional] [default to '###']
**temperature** | **float** | The temperature score. | [optional] [default to 0.4]
**words_to_ignore** | **List[str]** | Words to ignore when checking for words not in prompt. | [optional] 

## Example

```python
from wordlift-client.models.content_generation import ContentGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGeneration from a JSON string
content_generation_instance = ContentGeneration.from_json(json)
# print the JSON string representation of the object
print(ContentGeneration.to_json())

# convert the object into a dict
content_generation_dict = content_generation_instance.to_dict()
# create an instance of ContentGeneration from a dict
content_generation_from_dict = ContentGeneration.from_dict(content_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


