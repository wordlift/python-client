# AuditData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The audited URL (may include trailing slash) | [optional] 
**domain** | **str** | The base domain of the audited URL | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp of when the audit was performed | [optional] 
**overall_score** | **int** | Overall SEO and AI-readiness score (0-100) | [optional] 
**summary** | **str** | High-level summary of the audit findings | [optional] 
**site_files** | [**SiteFiles**](SiteFiles.md) |  | [optional] 
**seo_fundamentals** | [**SeoFundamentals**](SeoFundamentals.md) |  | [optional] 
**structured_data** | [**StructuredData**](StructuredData.md) |  | [optional] 
**content_structure** | [**ContentStructure**](ContentStructure.md) |  | [optional] 
**image_accessibility** | [**ImageAccessibility**](ImageAccessibility.md) |  | [optional] 
**automation_readiness** | [**AutomationReadiness**](AutomationReadiness.md) |  | [optional] 
**js_rendering** | [**JsRendering**](JsRendering.md) |  | [optional] 
**quick_wins** | [**List[QuickWin]**](QuickWin.md) |  | [optional] 
**status** | **str** | Status of the audit process | [optional] 
**account_id** | **int** | Account ID associated with the audit | [optional] 
**account_url** | **str** | Account URL associated with the audit | [optional] 

## Example

```python
from wordlift_client.models.audit_data import AuditData

# TODO update the JSON string below
json = "{}"
# create an instance of AuditData from a JSON string
audit_data_instance = AuditData.from_json(json)
# print the JSON string representation of the object
print(AuditData.to_json())

# convert the object into a dict
audit_data_dict = audit_data_instance.to_dict()
# create an instance of AuditData from a dict
audit_data_from_dict = AuditData.from_dict(audit_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


