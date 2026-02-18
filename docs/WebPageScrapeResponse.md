# WebPageScrapeResponse

Web Page Scrape Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_page** | [**WebPage**](WebPage.md) |  | 

## Example

```python
from wordlift_client.models.web_page_scrape_response import WebPageScrapeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageScrapeResponse from a JSON string
web_page_scrape_response_instance = WebPageScrapeResponse.from_json(json)
# print the JSON string representation of the object
print(WebPageScrapeResponse.to_json())

# convert the object into a dict
web_page_scrape_response_dict = web_page_scrape_response_instance.to_dict()
# create an instance of WebPageScrapeResponse from a dict
web_page_scrape_response_from_dict = WebPageScrapeResponse.from_dict(web_page_scrape_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


