# ResourcesSkillMd

/skill.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | not_found: missing, empty, or an HTML/error page; invalid: the file exists but can&#39;t be used (JSON that doesn&#39;t parse, or an agent-skills index without a skills list; JSON resources only); unknown: the fetch failed, so whether the file exists is not known, see reason | 
**reason** | **str** | Only when status is \&quot;unknown\&quot;. blocked: the site refused the request (401/403); rate_limited: the site throttled the request (429), possibly because of the audit&#39;s own parallel requests; site_error: the site answered with another error status; unreachable: the site never answered (timeout, network or proxy failure) | [optional] 

## Example

```python
from wordlift_client.models.resources_skill_md import ResourcesSkillMd

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesSkillMd from a JSON string
resources_skill_md_instance = ResourcesSkillMd.from_json(json)
# print the JSON string representation of the object
print(ResourcesSkillMd.to_json())

# convert the object into a dict
resources_skill_md_dict = resources_skill_md_instance.to_dict()
# create an instance of ResourcesSkillMd from a dict
resources_skill_md_from_dict = ResourcesSkillMd.from_dict(resources_skill_md_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


