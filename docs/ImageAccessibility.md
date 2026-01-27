# ImageAccessibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for image accessibility (0-5) | [optional] 
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**total_images** | **int** | Total number of images on the page | [optional] 
**images_without_alt** | **int** | Number of images without alt text | [optional] 
**missing_alt_text_images** | **List[str]** | Sample URLs or descriptions of images missing alt text | [optional] 

## Example

```python
from wordlift_client.models.image_accessibility import ImageAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAccessibility from a JSON string
image_accessibility_instance = ImageAccessibility.from_json(json)
# print the JSON string representation of the object
print(ImageAccessibility.to_json())

# convert the object into a dict
image_accessibility_dict = image_accessibility_instance.to_dict()
# create an instance of ImageAccessibility from a dict
image_accessibility_from_dict = ImageAccessibility.from_dict(image_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


