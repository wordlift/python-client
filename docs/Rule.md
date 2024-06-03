# Rule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The create date-time. | [optional] [readonly] 
**description** | **str** | Description for the rule | [optional] 
**fixes** | [**List[ValidationFix]**](ValidationFix.md) | The list of fixes to apply when the rule validation fails. | [optional] 
**id** | **int** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**level** | [**LevelEnum**](LevelEnum.md) |  | 
**modified_at** | **datetime** | The last modified date-time. | [optional] [readonly] 
**name** | **str** | The rule name. | 
**project_id** | **int** |  | [optional] 
**project_type** | [**ProjectType**](ProjectType.md) |  | [optional] 
**scope** | [**Scope**](Scope.md) |  | 
**type** | **str** | The rule type, one of &#x60;field&#x60;, &#x60;word&#x60; or &#x60;code&#x60;. By default &#x60;field&#x60;. | 
**what_operand_lhs** | [**WhatOperandLhs**](WhatOperandLhs.md) |  | 
**what_operand_rhs** | **str** | The right hand side operand for what condition. | 
**what_operator** | [**WhatOperator**](WhatOperator.md) |  | 
**when_operand_lhs** | **str** | The left hand side  operand for when condition. | 
**when_operand_rhs** | **str** | The right hand side operand for when condition. | 
**when_operator** | [**WhenOperator**](WhenOperator.md) |  | 

## Example

```python
from wordlift-client.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


