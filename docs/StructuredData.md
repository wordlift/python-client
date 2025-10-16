# StructuredData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**has_schema** | **bool** | Whether schema.org markup is present | [optional] 
**has_json_ld** | **bool** | Whether JSON-LD structured data is present | [optional] 
**detected_schemas** | **List[str]** | List of detected schema types | [optional] 

## Example

```python
from wordlift_client.models.structured_data import StructuredData

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredData from a JSON string
structured_data_instance = StructuredData.from_json(json)
# print the JSON string representation of the object
print(StructuredData.to_json())

# convert the object into a dict
structured_data_dict = structured_data_instance.to_dict()
# create an instance of StructuredData from a dict
structured_data_from_dict = StructuredData.from_dict(structured_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


