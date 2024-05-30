# GenerateSitemap200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sitemap** | **str** | The generated sitemap in XML format. | [optional] 

## Example

```python
from Wordlift_client.models.generate_sitemap200_response import GenerateSitemap200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSitemap200Response from a JSON string
generate_sitemap200_response_instance = GenerateSitemap200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateSitemap200Response.to_json())

# convert the object into a dict
generate_sitemap200_response_dict = generate_sitemap200_response_instance.to_dict()
# create an instance of GenerateSitemap200Response from a dict
generate_sitemap200_response_from_dict = GenerateSitemap200Response.from_dict(generate_sitemap200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


