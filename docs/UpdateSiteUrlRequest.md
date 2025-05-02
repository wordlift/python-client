# UpdateSiteUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_url_pointer** | **object** |  | [optional] 
**site_url** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.update_site_url_request import UpdateSiteUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSiteUrlRequest from a JSON string
update_site_url_request_instance = UpdateSiteUrlRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSiteUrlRequest.to_json())

# convert the object into a dict
update_site_url_request_dict = update_site_url_request_instance.to_dict()
# create an instance of UpdateSiteUrlRequest from a dict
update_site_url_request_from_dict = UpdateSiteUrlRequest.from_dict(update_site_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


