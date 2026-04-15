# CheckTimeseriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_name** | **str** |  | 
**items** | [**List[CheckResultItem]**](CheckResultItem.md) |  | 

## Example

```python
from wordlift_client.models.check_timeseries_response import CheckTimeseriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTimeseriesResponse from a JSON string
check_timeseries_response_instance = CheckTimeseriesResponse.from_json(json)
# print the JSON string representation of the object
print(CheckTimeseriesResponse.to_json())

# convert the object into a dict
check_timeseries_response_dict = check_timeseries_response_instance.to_dict()
# create an instance of CheckTimeseriesResponse from a dict
check_timeseries_response_from_dict = CheckTimeseriesResponse.from_dict(check_timeseries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


