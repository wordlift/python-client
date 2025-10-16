# AutomationReadiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**issues** | **List[str]** | List of issues affecting automation readiness | [optional] 

## Example

```python
from wordlift_client.models.automation_readiness import AutomationReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationReadiness from a JSON string
automation_readiness_instance = AutomationReadiness.from_json(json)
# print the JSON string representation of the object
print(AutomationReadiness.to_json())

# convert the object into a dict
automation_readiness_dict = automation_readiness_instance.to_dict()
# create an instance of AutomationReadiness from a dict
automation_readiness_from_dict = AutomationReadiness.from_dict(automation_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


