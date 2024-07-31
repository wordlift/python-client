# VectorSearchQueryResponseItemFieldsValueInner

Map of extra retrieved fields. The values of the requested fields are always returned in an array.If no value is found an empty array is returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from wordlift_client.models.vector_search_query_response_item_fields_value_inner import VectorSearchQueryResponseItemFieldsValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of VectorSearchQueryResponseItemFieldsValueInner from a JSON string
vector_search_query_response_item_fields_value_inner_instance = VectorSearchQueryResponseItemFieldsValueInner.from_json(json)
# print the JSON string representation of the object
print(VectorSearchQueryResponseItemFieldsValueInner.to_json())

# convert the object into a dict
vector_search_query_response_item_fields_value_inner_dict = vector_search_query_response_item_fields_value_inner_instance.to_dict()
# create an instance of VectorSearchQueryResponseItemFieldsValueInner from a dict
vector_search_query_response_item_fields_value_inner_from_dict = VectorSearchQueryResponseItemFieldsValueInner.from_dict(vector_search_query_response_item_fields_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


