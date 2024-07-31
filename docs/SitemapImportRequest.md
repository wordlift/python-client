# SitemapImportRequest

The Sitemap Import request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**EmbeddingRequest**](EmbeddingRequest.md) |  | [optional] 
**output_types** | **List[str]** | The type of the generated entities, by default &#x60;http://schema.org/WebPage&#x60;. | [optional] [default to ["http://schema.org/WebPage"]]
**overwrite** | **bool** | Whether to overwrite existing entities. | [optional] [default to False]
**sitemap_url** | **str** | The sitemap URL | [optional] 
**sitemap_url_regex** | **str** | A regex filter to apply to discovered URLs, it only applies to URLs in sitemaps. | [optional] 
**urls** | **List[str]** | The URLs | [optional] 

## Example

```python
from wordlift_client.models.sitemap_import_request import SitemapImportRequest

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


