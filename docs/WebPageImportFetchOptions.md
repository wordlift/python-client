# WebPageImportFetchOptions

Fetch Options for Web Page Import

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_ads** | **bool** | Block ads to save bandwidth (premium_scraper only). | [optional] 
**country_code** | **str** | Country code for the proxy (premium_scraper only). | [optional] 
**mode** | **str** | The fetching mode: &#x60;default&#x60; (smart fallback), &#x60;proxy&#x60; or &#x60;premium_scraper&#x60;. | [optional] [default to 'default']
**premium_proxy** | **bool** | Use premium proxy (premium_scraper only). | [optional] 
**render_js** | **bool** | Render JavaScript on the target page (premium_scraper only). | [optional] 
**timeout** | **int** | Timeout in milliseconds (premium_scraper only). | [optional] 
**wait_for** | **str** | CSS selector to wait for before returning (premium_scraper only). | [optional] 

## Example

```python
from wordlift_client.models.web_page_import_fetch_options import WebPageImportFetchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportFetchOptions from a JSON string
web_page_import_fetch_options_instance = WebPageImportFetchOptions.from_json(json)
# print the JSON string representation of the object
print(WebPageImportFetchOptions.to_json())

# convert the object into a dict
web_page_import_fetch_options_dict = web_page_import_fetch_options_instance.to_dict()
# create an instance of WebPageImportFetchOptions from a dict
web_page_import_fetch_options_from_dict = WebPageImportFetchOptions.from_dict(web_page_import_fetch_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


