# WebsiteSearch

Search Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clicks** | **int** | Number of clicks. | 
**ctr** | **float** | CTR. | 
**id** | **int** | The id: it&#39;s now a unique id, but a row index. | 
**impressions** | **int** | Number of impressions. | 
**keys** | **List[str]** | The keys for the current data, matching the provided &#x60;dimensions&#x60; in the query. | 
**position** | **float** | Position. | 
**score** | **float** | A score to spot traffic opportunities, from 0.0 to 1.0 (the higher the better). The score is based on the traffic data. | 

## Example

```python
from wordlift-client.models.website_search import WebsiteSearch

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteSearch from a JSON string
website_search_instance = WebsiteSearch.from_json(json)
# print the JSON string representation of the object
print(WebsiteSearch.to_json())

# convert the object into a dict
website_search_dict = website_search_instance.to_dict()
# create an instance of WebsiteSearch from a dict
website_search_from_dict = WebsiteSearch.from_dict(website_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


