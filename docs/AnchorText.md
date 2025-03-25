# AnchorText

The Anchor Text request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_prompt_template** | **str** |  | [optional] [readonly] 
**enabled** | **bool** | Whether to enable Anchor Text, by default false. | [optional] [default to False]
**max_characters** | **int** | The maximum anchor text length, by default 15 characters. | [optional] [default to 15]
**model** | **str** | The model to use. | [optional] [default to 'gpt-4o']
**prompt_template** | **str** | The prompt template, we provide a default. Liquid template language is supported. | [optional] [default to '''As an SEO and content editor, your task is to create a concise and appropriate anchor text to enhance keyword targeting, using the
provided keyword and page title. Ensure to maintain a neutral tone and adhere to the examples below for guidance:

{%- for anchor in anchors -%}
- Title: {{ anchor.title }}
- Keyword: {{ anchor.keyword }}
- Anchor text: {{ anchor.anchor_text }}
{%- endfor -%}
''']

## Example

```python
from wordlift_client.models.anchor_text import AnchorText

# TODO update the JSON string below
json = "{}"
# create an instance of AnchorText from a JSON string
anchor_text_instance = AnchorText.from_json(json)
# print the JSON string representation of the object
print(AnchorText.to_json())

# convert the object into a dict
anchor_text_dict = anchor_text_instance.to_dict()
# create an instance of AnchorText from a dict
anchor_text_from_dict = AnchorText.from_dict(anchor_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


