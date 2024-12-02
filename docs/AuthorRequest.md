# AuthorRequest

The author request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the author, e.g. &#x60;John Smith&#x60;. | 

## Example

```python
from wordlift_client.models.author_request import AuthorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorRequest from a JSON string
author_request_instance = AuthorRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorRequest.to_json())

# convert the object into a dict
author_request_dict = author_request_instance.to_dict()
# create an instance of AuthorRequest from a dict
author_request_from_dict = AuthorRequest.from_dict(author_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


