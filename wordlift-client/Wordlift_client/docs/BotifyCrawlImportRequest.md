# BotifyCrawlImportRequest

The Botify Crawl Import request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** |  | [optional] 
**description** | **List[str]** |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**headline** | **str** |  | [optional] 
**request_embeddings** | **List[str]** |  | [optional] 
**text** | **List[str]** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from Wordlift_client.models.botify_crawl_import_request import BotifyCrawlImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BotifyCrawlImportRequest from a JSON string
botify_crawl_import_request_instance = BotifyCrawlImportRequest.from_json(json)
# print the JSON string representation of the object
print(BotifyCrawlImportRequest.to_json())

# convert the object into a dict
botify_crawl_import_request_dict = botify_crawl_import_request_instance.to_dict()
# create an instance of BotifyCrawlImportRequest from a dict
botify_crawl_import_request_from_dict = BotifyCrawlImportRequest.from_dict(botify_crawl_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


