# CreateSEOScore200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyze** | **str** | Traffic light system indicating the match. M for match, T for trustworthiness, O for overall score. | [optional] 

## Example

```python
from Wordlift_client.models.create_seo_score200_response import CreateSEOScore200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSEOScore200Response from a JSON string
create_seo_score200_response_instance = CreateSEOScore200Response.from_json(json)
# print the JSON string representation of the object
print(CreateSEOScore200Response.to_json())

# convert the object into a dict
create_seo_score200_response_dict = create_seo_score200_response_instance.to_dict()
# create an instance of CreateSEOScore200Response from a dict
create_seo_score200_response_from_dict = CreateSEOScore200Response.from_dict(create_seo_score200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


