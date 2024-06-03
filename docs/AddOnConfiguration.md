# AddOnConfiguration

An Add-On configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_do_content_expansion** | **bool** | Whether this Add-on can do content expansion | [optional] [readonly] 
**can_import_to_wordpress** | **bool** | Whether this Add-on can import to WordPress. | [optional] [readonly] 
**key** | **str** | A key | [optional] [readonly] 
**wp_admin** | **str** | The wp-admin endpoint for a website using the key. | [optional] [readonly] 
**wp_json** | **str** | The wp-json endpoint for a website using the key. | [optional] [readonly] 

## Example

```python
from wordlift-client.models.add_on_configuration import AddOnConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnConfiguration from a JSON string
add_on_configuration_instance = AddOnConfiguration.from_json(json)
# print the JSON string representation of the object
print(AddOnConfiguration.to_json())

# convert the object into a dict
add_on_configuration_dict = add_on_configuration_instance.to_dict()
# create an instance of AddOnConfiguration from a dict
add_on_configuration_from_dict = AddOnConfiguration.from_dict(add_on_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


