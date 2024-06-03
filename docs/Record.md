# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion** | **str** |  | [optional] 
**content_generation_id** | **int** | The parent content generation id. | [readonly] 
**data** | **object** | The data from knowledge graph after applying the graphql query. | [optional] [readonly] 
**errors** | [**List[ValidationResult]**](ValidationResult.md) | The set of errors found for record. | [optional] [readonly] 
**has_upvote** | **bool** | This indicates whether the user upvoted the completion. | 
**id** | **int** |  | [optional] 
**is_accepted** | **bool** | This indicates whether the completion is accepted by the user. | 
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**not_in_prompt_words** | **List[str]** | Words in completion that are not in the prompt. | [optional] [readonly] 
**prompt** | **str** | The prompt. | 
**repeated_words** | [**Dict[str, WordRepetitionData]**](WordRepetitionData.md) | Words in completion which are repeated. | [optional] [readonly] 
**status** | **str** | The status of the record, whether it&#39;s accepted, with errors, with warnings or valid. | [optional] [readonly] 
**validated_at** | **datetime** | The last validation date-time. | [optional] [readonly] 
**warnings** | [**List[ValidationResult]**](ValidationResult.md) | The set of errors found for record. | [optional] [readonly] 

## Example

```python
from wordlift-client.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


