# ContentGenerationStats

Statistics about a Content Generation Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **int** | The number of accepted records. | [optional] 
**errors** | **int** | The number of records with errors. | [optional] 
**total** | **int** | The total number of records. | [optional] 
**valid** | **int** | The number of valid records. | [optional] 
**warnings** | **int** | The number of records with warnings. | [optional] 

## Example

```python
from Wordlift_client.models.content_generation_stats import ContentGenerationStats

# TODO update the JSON string below
json = "{}"
# create an instance of ContentGenerationStats from a JSON string
content_generation_stats_instance = ContentGenerationStats.from_json(json)
# print the JSON string representation of the object
print(ContentGenerationStats.to_json())

# convert the object into a dict
content_generation_stats_dict = content_generation_stats_instance.to_dict()
# create an instance of ContentGenerationStats from a dict
content_generation_stats_from_dict = ContentGenerationStats.from_dict(content_generation_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


