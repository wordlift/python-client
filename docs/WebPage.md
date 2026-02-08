# WebPage

Represents a web page and its extracted content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstract** | **str** | A short abstract or excerpt of the web page content. | [optional] 
**date_published** | **date** | The publication date of the web page. | [optional] 
**headline** | **str** | The headline or title of the web page. | [optional] 
**html** | **str** | The full HTML content of the web page. | [optional] 
**image** | **str** | The URL of the primary image of the web page. | [optional] 
**markdown** | **str** | The extracted content of the web page in Markdown format. | [optional] 
**status_code** | **int** | The HTTP status code returned when fetching the URL. | [optional] 
**text** | **str** | The extracted main text content of the web page. | [optional] 
**types** | **List[str]** | The RDF types for the web page entity. | [optional] [default to ["http://schema.org/WebPage"]]
**url** | **str** | The canonical URL of the web page. | [optional] 

## Example

```python
from wordlift_client.models.web_page import WebPage

# TODO update the JSON string below
json = "{}"
# create an instance of WebPage from a JSON string
web_page_instance = WebPage.from_json(json)
# print the JSON string representation of the object
print(WebPage.to_json())

# convert the object into a dict
web_page_dict = web_page_instance.to_dict()
# create an instance of WebPage from a dict
web_page_from_dict = WebPage.from_dict(web_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


