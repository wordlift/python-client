# SiteFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for site files (0-10). MCP / WebMCP / Agent Skills / SKILL.md signals are applied as post-hoc bonuses on &#x60;overallScore&#x60;, not on this per-criterion score. | 
**explanation** | **str** | Detailed explanation of site files evaluation | 
**robots_txt** | **str** | Deprecated: use resources.robotsTxt.status | 
**llms_txt** | **str** | Deprecated: use resources.llmsTxt.status | 
**has_llms_txt** | **bool** | Deprecated: use resources.llmsTxt. false both when llms.txt is missing and when its fetch failed | 
**bot_status** | [**List[BotStatus]**](BotStatus.md) | Empty when robots.txt could not be fetched (resources.robotsTxt.status: \&quot;unknown\&quot;) | 
**status** | **str** | Overall status of site files | 
**has_skill_md** | **bool** | Deprecated: use resources.skillMd | 
**well_known** | [**WellKnownFiles**](WellKnownFiles.md) |  | 

## Example

```python
from wordlift_client.models.site_files import SiteFiles

# TODO update the JSON string below
json = "{}"
# create an instance of SiteFiles from a JSON string
site_files_instance = SiteFiles.from_json(json)
# print the JSON string representation of the object
print(SiteFiles.to_json())

# convert the object into a dict
site_files_dict = site_files_instance.to_dict()
# create an instance of SiteFiles from a dict
site_files_from_dict = SiteFiles.from_dict(site_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


