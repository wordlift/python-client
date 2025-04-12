# ContentEvaluationResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word_count** | **int** |  | 
**sentiment** | [**ContentEvaluationResponseMetadataSentiment**](ContentEvaluationResponseMetadataSentiment.md) |  | 
**performance** | [**ContentEvaluationResponseMetadataPerformance**](ContentEvaluationResponseMetadataPerformance.md) |  | 
**eval_id** | **str** |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_metadata import ContentEvaluationResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseMetadata from a JSON string
content_evaluation_response_metadata_instance = ContentEvaluationResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseMetadata.to_json())

# convert the object into a dict
content_evaluation_response_metadata_dict = content_evaluation_response_metadata_instance.to_dict()
# create an instance of ContentEvaluationResponseMetadata from a dict
content_evaluation_response_metadata_from_dict = ContentEvaluationResponseMetadata.from_dict(content_evaluation_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


