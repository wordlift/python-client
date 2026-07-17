# WebPageImportsBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | List of URLs to import into the KG | 

## Example

```python
from wordlift_client.models.web_page_imports_batch_request import WebPageImportsBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebPageImportsBatchRequest from a JSON string
web_page_imports_batch_request_instance = WebPageImportsBatchRequest.from_json(json)
# print the JSON string representation of the object
print(WebPageImportsBatchRequest.to_json())

# convert the object into a dict
web_page_imports_batch_request_dict = web_page_imports_batch_request_instance.to_dict()
# create an instance of WebPageImportsBatchRequest from a dict
web_page_imports_batch_request_from_dict = WebPageImportsBatchRequest.from_dict(web_page_imports_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


