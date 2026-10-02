# ExpectationAttachment

One expectation's attachment to a segment, or directly to the monitor — segment_id is null for a direct (account-scoped) attachment, matching the same null-means-account-scoped convention MonitorStatusResponse.url uses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**severity** | [**ExpectationSeverity**](ExpectationSeverity.md) |  | 

## Example

```python
from wordlift_client.models.expectation_attachment import ExpectationAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ExpectationAttachment from a JSON string
expectation_attachment_instance = ExpectationAttachment.from_json(json)
# print the JSON string representation of the object
print(ExpectationAttachment.to_json())

# convert the object into a dict
expectation_attachment_dict = expectation_attachment_instance.to_dict()
# create an instance of ExpectationAttachment from a dict
expectation_attachment_from_dict = ExpectationAttachment.from_dict(expectation_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


