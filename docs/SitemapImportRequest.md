# SitemapImportRequest

The Sitemap Import request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sitemap_url** | **str** | The sitemap URL | [optional] 
**urls** | **List[str]** | The URLs | [optional] 

## Example

```python
from wordlift-client.models.sitemap_import_request import SitemapImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SitemapImportRequest from a JSON string
sitemap_import_request_instance = SitemapImportRequest.from_json(json)
# print the JSON string representation of the object
print(SitemapImportRequest.to_json())

# convert the object into a dict
sitemap_import_request_dict = sitemap_import_request_instance.to_dict()
# create an instance of SitemapImportRequest from a dict
sitemap_import_request_from_dict = SitemapImportRequest.from_dict(sitemap_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


