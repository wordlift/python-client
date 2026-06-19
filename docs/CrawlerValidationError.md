# CrawlerValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[LocationInner]**](LocationInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
**input** | **object** |  | [optional] 
**ctx** | **object** |  | [optional] 

## Example

```python
from wordlift_client.models.crawler_validation_error import CrawlerValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerValidationError from a JSON string
crawler_validation_error_instance = CrawlerValidationError.from_json(json)
# print the JSON string representation of the object
print(CrawlerValidationError.to_json())

# convert the object into a dict
crawler_validation_error_dict = crawler_validation_error_instance.to_dict()
# create an instance of CrawlerValidationError from a dict
crawler_validation_error_from_dict = CrawlerValidationError.from_dict(crawler_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


