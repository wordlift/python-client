# SegmentSummaryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **str** |  | 
**monitor_count** | **int** |  | 
**expectation_count** | **int** |  | 

## Example

```python
from wordlift_client.models.segment_summary_item import SegmentSummaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentSummaryItem from a JSON string
segment_summary_item_instance = SegmentSummaryItem.from_json(json)
# print the JSON string representation of the object
print(SegmentSummaryItem.to_json())

# convert the object into a dict
segment_summary_item_dict = segment_summary_item_instance.to_dict()
# create an instance of SegmentSummaryItem from a dict
segment_summary_item_from_dict = SegmentSummaryItem.from_dict(segment_summary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


