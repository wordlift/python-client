# WebPageImportResponse

Web Page Import Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id/iri of the web page in the Graph. | 
**model** | **str** |  | 
**web_page** | [**WebPage**](WebPage.md) |  | 

## Example

```python
from wordlift_client.models.web_page_import_response import WebPageImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportResponse from a JSON string
web_page_import_response_instance = WebPageImportResponse.from_json(json)
# print the JSON string representation of the object
print(WebPageImportResponse.to_json())

# convert the object into a dict
web_page_import_response_dict = web_page_import_response_instance.to_dict()
# create an instance of WebPageImportResponse from a dict
web_page_import_response_from_dict = WebPageImportResponse.from_dict(web_page_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


