# Properties1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity. | [optional] 
**same_as** | **List[str]** | A list of sameAs entity URIs. | [optional] 

## Example

```python
from Wordlift_client.models.properties1 import Properties1

# TODO update the JSON string below
json = "{}"
# create an instance of Properties1 from a JSON string
properties1_instance = Properties1.from_json(json)
# print the JSON string representation of the object
print(Properties1.to_json())

# convert the object into a dict
properties1_dict = properties1_instance.to_dict()
# create an instance of Properties1 from a dict
properties1_from_dict = Properties1.from_dict(properties1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


