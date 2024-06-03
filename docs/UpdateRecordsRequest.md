# UpdateRecordsRequest

A request to update the properties of multiple records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validated_at** | **datetime** | The validation time of the record. | [optional] 

## Example

```python
from wordlift_client.models.update_records_request import UpdateRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecordsRequest from a JSON string
update_records_request_instance = UpdateRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRecordsRequest.to_json())

# convert the object into a dict
update_records_request_dict = update_records_request_instance.to_dict()
# create an instance of UpdateRecordsRequest from a dict
update_records_request_from_dict = UpdateRecordsRequest.from_dict(update_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


