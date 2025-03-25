# ImageToTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | URL of the image to be processed | 
**prompt_type** | **str** | Type of analysis to perform | 
**custom_prompt** | **str** | Custom instructions for text generation | [optional] 

## Example

```python
from wordlift_client.models.image_to_text_request import ImageToTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageToTextRequest from a JSON string
image_to_text_request_instance = ImageToTextRequest.from_json(json)
# print the JSON string representation of the object
print(ImageToTextRequest.to_json())

# convert the object into a dict
image_to_text_request_dict = image_to_text_request_instance.to_dict()
# create an instance of ImageToTextRequest from a dict
image_to_text_request_from_dict = ImageToTextRequest.from_dict(image_to_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


