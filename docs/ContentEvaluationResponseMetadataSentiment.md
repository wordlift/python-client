# ContentEvaluationResponseMetadataSentiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polarity** | **float** |  | 
**subjectivity** | **float** |  | 

## Example

```python
from wordlift_client.models.content_evaluation_response_metadata_sentiment import ContentEvaluationResponseMetadataSentiment

# TODO update the JSON string below
json = "{}"
# create an instance of ContentEvaluationResponseMetadataSentiment from a JSON string
content_evaluation_response_metadata_sentiment_instance = ContentEvaluationResponseMetadataSentiment.from_json(json)
# print the JSON string representation of the object
print(ContentEvaluationResponseMetadataSentiment.to_json())

# convert the object into a dict
content_evaluation_response_metadata_sentiment_dict = content_evaluation_response_metadata_sentiment_instance.to_dict()
# create an instance of ContentEvaluationResponseMetadataSentiment from a dict
content_evaluation_response_metadata_sentiment_from_dict = ContentEvaluationResponseMetadataSentiment.from_dict(content_evaluation_response_metadata_sentiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


