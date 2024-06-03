# WithLimits

An array of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_limits** | **int** |  | [optional] 
**applies_to** | **str** |  | 
**block** | **bool** |  | [optional] 
**consumption** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**limits** | **int** |  | [optional] 
**reference_id** | **int** |  | [optional] 
**reference_type** | **str** |  | [optional] 
**remaining** | **int** |  | [optional] 
**resets_in_seconds** | **int** |  | [optional] 
**subscription_limits** | **int** |  | [optional] 

## Example

```python
from wordlift_client.models.with_limits import WithLimits

# TODO update the JSON string below
json = "{}"
# create an instance of WithLimits from a JSON string
with_limits_instance = WithLimits.from_json(json)
# print the JSON string representation of the object
print(WithLimits.to_json())

# convert the object into a dict
with_limits_dict = with_limits_instance.to_dict()
# create an instance of WithLimits from a dict
with_limits_from_dict = WithLimits.from_dict(with_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


