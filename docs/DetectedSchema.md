# DetectedSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Schema.org type (e.g., Organization, WebSite, Article) | [optional] 
**format** | **str** | Format of the structured data | [optional] 

## Example

```python
from wordlift_client.models.detected_schema import DetectedSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DetectedSchema from a JSON string
detected_schema_instance = DetectedSchema.from_json(json)
# print the JSON string representation of the object
print(DetectedSchema.to_json())

# convert the object into a dict
detected_schema_dict = detected_schema_instance.to_dict()
# create an instance of DetectedSchema from a dict
detected_schema_from_dict = DetectedSchema.from_dict(detected_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


