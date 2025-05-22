# WebPageImportRequest

The Web Page Import request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**EmbeddingRequest**](EmbeddingRequest.md) |  | [optional] 
**id_generator** | **str** | The entity id generator, by default uses the web page path. | [optional] [default to 'default']
**output_types** | **List[str]** | The type of the generated entities, by default &#x60;http://schema.org/WebPage&#x60;. | [optional] [default to ["http://schema.org/WebPage"]]
**url** | **str** | The Web Page url to import | 

## Example

```python
from wordlift_client.models.web_page_import_request import WebPageImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportRequest from a JSON string
web_page_import_request_instance = WebPageImportRequest.from_json(json)
# print the JSON string representation of the object
print(WebPageImportRequest.to_json())

# convert the object into a dict
web_page_import_request_dict = web_page_import_request_instance.to_dict()
# create an instance of WebPageImportRequest from a dict
web_page_import_request_from_dict = WebPageImportRequest.from_dict(web_page_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


