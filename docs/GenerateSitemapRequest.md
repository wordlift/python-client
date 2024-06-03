# GenerateSitemapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**operation_name** | **str** |  | [optional] 

## Example

```python
from wordlift_client.models.generate_sitemap_request import GenerateSitemapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSitemapRequest from a JSON string
generate_sitemap_request_instance = GenerateSitemapRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateSitemapRequest.to_json())

# convert the object into a dict
generate_sitemap_request_dict = generate_sitemap_request_instance.to_dict()
# create an instance of GenerateSitemapRequest from a dict
generate_sitemap_request_from_dict = GenerateSitemapRequest.from_dict(generate_sitemap_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


