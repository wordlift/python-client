# SeoFundamentals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for SEO fundamentals (0-20) | [optional] 
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**title** | **str** | Page title tag content | [optional] 
**description** | **str** | Meta description content | [optional] 
**h1_count** | **int** | Number of H1 headings on the page | [optional] 

## Example

```python
from wordlift_client.models.seo_fundamentals import SeoFundamentals

# TODO update the JSON string below
json = "{}"
# create an instance of SeoFundamentals from a JSON string
seo_fundamentals_instance = SeoFundamentals.from_json(json)
# print the JSON string representation of the object
print(SeoFundamentals.to_json())

# convert the object into a dict
seo_fundamentals_dict = seo_fundamentals_instance.to_dict()
# create an instance of SeoFundamentals from a dict
seo_fundamentals_from_dict = SeoFundamentals.from_dict(seo_fundamentals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


