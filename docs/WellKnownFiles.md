# WellKnownFiles

MCP / WebMCP / Agent Skills discovery surfaces detected under .well-known and in the page HTML.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcp_json** | **bool** | Whether &#x60;/.well-known/mcp.json&#x60; exists (legacy MCP server manifest path) | [optional] 
**mcp_server_card** | **bool** | Whether &#x60;/.well-known/mcp/server-card.json&#x60; exists (MCP server card, SEP-1649 draft) | [optional] 
**webmcp_tools_json** | **bool** | Whether &#x60;/.well-known/webmcp/tools.json&#x60; exists (Chrome Labs WebMCP tools manifest) | [optional] 
**mcp_link_tag** | **bool** | Whether a &#x60;&lt;link rel&#x3D;\&quot;mcp\&quot;&gt;&#x60; discovery tag was detected in the page HTML | [optional] 
**mcp_endpoint** | **str** | The href value of the &#x60;&lt;link rel&#x3D;\&quot;mcp\&quot;&gt;&#x60; tag, if present; null otherwise | [optional] 
**agent_skills_index** | **bool** | Whether &#x60;/.well-known/agent-skills/index.json&#x60; exists (Agent Skills Discovery, Cloudflare RFC v0.2.0) | [optional] 
**agent_skills_count** | **int** | Number of skills listed in the Agent Skills Discovery index (0 when the index is absent or empty) | [optional] 

## Example

```python
from wordlift_client.models.well_known_files import WellKnownFiles

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownFiles from a JSON string
well_known_files_instance = WellKnownFiles.from_json(json)
# print the JSON string representation of the object
print(WellKnownFiles.to_json())

# convert the object into a dict
well_known_files_dict = well_known_files_instance.to_dict()
# create an instance of WellKnownFiles from a dict
well_known_files_from_dict = WellKnownFiles.from_dict(well_known_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


