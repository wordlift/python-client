# AutomationIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **str** | Priority level of the issue | [optional] 
**criterion** | **str** | WCAG or accessibility criterion reference | [optional] 
**what** | **str** | Description of the issue | [optional] 
**where** | **str** | Location of the issue on the page | [optional] 
**why** | **str** | Why this issue matters | [optional] 
**how** | **str** | How to fix the issue | [optional] 
**compliance** | **str** | Compliance impact description | [optional] 

## Example

```python
from wordlift_client.models.automation_issue import AutomationIssue

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationIssue from a JSON string
automation_issue_instance = AutomationIssue.from_json(json)
# print the JSON string representation of the object
print(AutomationIssue.to_json())

# convert the object into a dict
automation_issue_dict = automation_issue_instance.to_dict()
# create an instance of AutomationIssue from a dict
automation_issue_from_dict = AutomationIssue.from_dict(automation_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


