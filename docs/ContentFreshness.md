# ContentFreshness

Legacy field - always returns status Unknown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Always returns Unknown as this is not currently analyzed | [optional] 
**explanation** | **str** | Explanation that this is not currently analyzed | [optional] 
**category** | **str** | Always returns \&quot;N/A\&quot; | [optional] 
**publication_date** | **str** | Always returns \&quot;N/A\&quot; | [optional] 
**last_updated_date** | **str** | Always returns \&quot;N/A\&quot; | [optional] 

## Example

```python
from wordlift_client.models.content_freshness import ContentFreshness

# TODO update the JSON string below
json = "{}"
# create an instance of ContentFreshness from a JSON string
content_freshness_instance = ContentFreshness.from_json(json)
# print the JSON string representation of the object
print(ContentFreshness.to_json())

# convert the object into a dict
content_freshness_dict = content_freshness_instance.to_dict()
# create an instance of ContentFreshness from a dict
content_freshness_from_dict = ContentFreshness.from_dict(content_freshness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


