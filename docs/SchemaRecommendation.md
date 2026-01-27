# SchemaRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the schema recommendation | [optional] 
**description** | **str** | Detailed description of the recommendation | [optional] 

## Example

```python
from wordlift_client.models.schema_recommendation import SchemaRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRecommendation from a JSON string
schema_recommendation_instance = SchemaRecommendation.from_json(json)
# print the JSON string representation of the object
print(SchemaRecommendation.to_json())

# convert the object into a dict
schema_recommendation_dict = schema_recommendation_instance.to_dict()
# create an instance of SchemaRecommendation from a dict
schema_recommendation_from_dict = SchemaRecommendation.from_dict(schema_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


