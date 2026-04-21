# ContentStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Numeric score for content structure (0-15) | [optional] 
**status** | **str** |  | [optional] 
**explanation** | **str** |  | [optional] 
**has_semantic_elements** | **bool** | Whether semantic HTML elements are used | [optional] 
**has_landmarks** | **bool** | Whether ARIA landmarks are present | [optional] 
**token_count** | **int** | Deterministic token-budget estimate for the main content. Computed by running Mozilla Readability on the page, converting the extracted article to Markdown via Turndown, and dividing the character count by 4 (coarse tokens≈chars/4 heuristic).  | [optional] 
**token_budget_status** | **str** | Qualitative bucket for &#x60;tokenCount&#x60; relative to typical LLM context budgets (Good ≤ 20 000, Fair ≤ 30 000, Exceeded otherwise). The &#x60;overallScore&#x60; receives a +2 bonus when &#x60;tokenCount ≤ 30 000&#x60;.  | [optional] 

## Example

```python
from wordlift_client.models.content_structure import ContentStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStructure from a JSON string
content_structure_instance = ContentStructure.from_json(json)
# print the JSON string representation of the object
print(ContentStructure.to_json())

# convert the object into a dict
content_structure_dict = content_structure_instance.to_dict()
# create an instance of ContentStructure from a dict
content_structure_from_dict = ContentStructure.from_dict(content_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


