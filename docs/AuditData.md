# AuditData

Full audit result returned by POST /api/audit (nested under `data`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The audited URL (may include trailing slash) | 
**domain** | **str** | Origin of the audited URL (scheme and host), e.g. &#39;https://www.wordlift.io&#39; | 
**timestamp** | **datetime** | ISO 8601 timestamp of when the audit was performed | 
**summary** | **str** | High-level summary of the audit findings in markdown format | 
**resources** | [**Resources**](Resources.md) |  | 
**site_files** | [**SiteFiles**](SiteFiles.md) |  | 
**seo_fundamentals** | [**SeoFundamentals**](SeoFundamentals.md) |  | 
**structured_data** | [**StructuredData**](StructuredData.md) |  | 
**content_structure** | [**ContentStructure**](ContentStructure.md) |  | 
**image_accessibility** | [**ImageAccessibility**](ImageAccessibility.md) |  | 
**automation_readiness** | [**AutomationReadiness**](AutomationReadiness.md) |  | 
**js_rendering** | [**JsRendering**](JsRendering.md) |  | 
**quick_wins** | [**QuickWinsResult**](QuickWinsResult.md) |  | 
**html_semantics** | [**HtmlSemantics**](HtmlSemantics.md) |  | 
**content_freshness** | [**ContentFreshness**](ContentFreshness.md) |  | 
**internal_linking** | [**InternalLinking**](InternalLinking.md) |  | 
**overall_score** | **int** | Overall SEO and AI-readiness score (0-100) | 
**score** | **int** | Legacy field - same as overallScore | 
**status** | **str** | Always completed: a failed audit is returned as an error response | 
**account_id** | **int** | WordLift account ID resolved from the Authorization key. | 
**account_url** | **str** | URL of the WordLift account the key belongs to | 

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


