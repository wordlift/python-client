# Resources

What the audit fetched or detected, one entry per resource. Supersedes the file facts in siteFiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**robots_txt** | [**ResourcesRobotsTxt**](ResourcesRobotsTxt.md) |  | 
**llms_txt** | [**ResourcesLlmsTxt**](ResourcesLlmsTxt.md) |  | 
**skill_md** | [**ResourcesSkillMd**](ResourcesSkillMd.md) |  | 
**mcp_json** | [**ResourcesMcpJson**](ResourcesMcpJson.md) |  | 
**mcp_server_card** | [**ResourcesMcpServerCard**](ResourcesMcpServerCard.md) |  | 
**webmcp_tools_json** | [**ResourcesWebmcpToolsJson**](ResourcesWebmcpToolsJson.md) |  | 
**agent_skills_index** | [**ResourcesAgentSkillsIndex**](ResourcesAgentSkillsIndex.md) |  | 
**mcp_link_tag** | [**ResourcesMcpLinkTag**](ResourcesMcpLinkTag.md) |  | 

## Example

```python
from wordlift_client.models.resources import Resources

# TODO update the JSON string below
json = "{}"
# create an instance of Resources from a JSON string
resources_instance = Resources.from_json(json)
# print the JSON string representation of the object
print(Resources.to_json())

# convert the object into a dict
resources_dict = resources_instance.to_dict()
# create an instance of Resources from a dict
resources_from_dict = Resources.from_dict(resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


