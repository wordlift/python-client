# WebPageScrapeRequest

Web Page Scrape Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetch_options** | [**WebPageImportFetchOptions**](WebPageImportFetchOptions.md) |  | [optional] 
**url** | **str** | The Web Page url to scrape | 

## Example

```python
from wordlift_client.models.web_page_scrape_request import WebPageScrapeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageScrapeRequest from a JSON string
web_page_scrape_request_instance = WebPageScrapeRequest.from_json(json)
# print the JSON string representation of the object
print(WebPageScrapeRequest.to_json())

# convert the object into a dict
web_page_scrape_request_dict = web_page_scrape_request_instance.to_dict()
# create an instance of WebPageScrapeRequest from a dict
web_page_scrape_request_from_dict = WebPageScrapeRequest.from_dict(web_page_scrape_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


