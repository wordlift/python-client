# WebPageImportRequest

The Web Page Import request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**EmbeddingRequest**](EmbeddingRequest.md) |  | [optional] 
**fetch_options** | [**WebPageImportFetchOptions**](WebPageImportFetchOptions.md) |  | [optional] 
**id** | **str** | The Web Page id (or iri) in Graph when available. | [optional] 
**id_generator** | **str** | The entity id generator, by default uses the web page path. | [optional] [default to 'default']
**output_types** | **List[str]** | The type of the generated entities, by default &#x60;http://schema.org/WebPage&#x60;. | [optional] [default to ["http://schema.org/WebPage"]]
**url** | **str** | The Web Page url to import | 
**write_strategy** | **str** | The strategy used to write to the Graph: &#x60;createOrUpdateModel&#x60; (default) will replace existing entities; &#x60;patchReplaceModel&#x60; will replace the &#x60;type&#x60;, &#x60;headline&#x60;, &#x60;abstract&#x60; and &#x60;text&#x60; properties. | [optional] [default to 'createOrUpdateModel']

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


