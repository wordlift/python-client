# StructuredDataExpectationConfig

Config payload for an expectation triggered by ``structured_data_check``.  Each field describes a structured-data assertion specifically — the naming is intentionally not generic, since a future check (e.g. a latency assertion) will get its own config class with its own domain-specific field names rather than reusing this shape.  ``property_path`` distinguishes entity-level rules (``None``) from property-level rules (set) — there is no cross-field validator; the nullability of ``property_path`` does the work.  The domain shape is always the current version; payload-version tracking and upgrades live at the storage boundary in ``expectation_repository``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | 
**property_path** | **str** |  | [optional] 
**constraint** | [**StructuredDataConstraint**](StructuredDataConstraint.md) |  | 

## Example

```python
from wordlift_client.models.structured_data_expectation_config import StructuredDataExpectationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredDataExpectationConfig from a JSON string
structured_data_expectation_config_instance = StructuredDataExpectationConfig.from_json(json)
# print the JSON string representation of the object
print(StructuredDataExpectationConfig.to_json())

# convert the object into a dict
structured_data_expectation_config_dict = structured_data_expectation_config_instance.to_dict()
# create an instance of StructuredDataExpectationConfig from a dict
structured_data_expectation_config_from_dict = StructuredDataExpectationConfig.from_dict(structured_data_expectation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


