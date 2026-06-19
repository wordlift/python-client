# LongTailProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity. | [optional] 
**same_as** | **List[str]** | A list of sameAs entity URIs. | [optional] 

## Example

```python
from wordlift_client.models.long_tail_properties import LongTailProperties

# TODO update the JSON string below
json = "{}"
# create an instance of LongTailProperties from a JSON string
long_tail_properties_instance = LongTailProperties.from_json(json)
# print the JSON string representation of the object
print(LongTailProperties.to_json())

# convert the object into a dict
long_tail_properties_dict = long_tail_properties_instance.to_dict()
# create an instance of LongTailProperties from a dict
long_tail_properties_from_dict = LongTailProperties.from_dict(long_tail_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


