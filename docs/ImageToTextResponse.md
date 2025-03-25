# ImageToTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Generated text description of the image | 

## Example

```python
from wordlift_client.models.image_to_text_response import ImageToTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageToTextResponse from a JSON string
image_to_text_response_instance = ImageToTextResponse.from_json(json)
# print the JSON string representation of the object
print(ImageToTextResponse.to_json())

# convert the object into a dict
image_to_text_response_dict = image_to_text_response_instance.to_dict()
# create an instance of ImageToTextResponse from a dict
image_to_text_response_from_dict = ImageToTextResponse.from_dict(image_to_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


