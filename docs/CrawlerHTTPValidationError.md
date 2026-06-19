# CrawlerHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[CrawlerValidationError]**](CrawlerValidationError.md) |  | [optional] 

## Example

```python
from wordlift_client.models.crawler_http_validation_error import CrawlerHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlerHTTPValidationError from a JSON string
crawler_http_validation_error_instance = CrawlerHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(CrawlerHTTPValidationError.to_json())

# convert the object into a dict
crawler_http_validation_error_dict = crawler_http_validation_error_instance.to_dict()
# create an instance of CrawlerHTTPValidationError from a dict
crawler_http_validation_error_from_dict = CrawlerHTTPValidationError.from_dict(crawler_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


