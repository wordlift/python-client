# AnalysesRequest

The analysis request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text to analyse. | [optional] 
**url** | **str** | The URL to analyse. | [optional] 
**query** | **str** | The query string to analyse. | [optional] 
**html** | **str** | The html to analyse. | [optional] 
**language_code** | **str** | The language code used for content analysis, e.g. &#x60;en&#x60;. | [optional] [default to 'en']
**query_location_name** | **str** | The location name for the query, e.g. United Kingdom. | [optional] [default to 'United States']
**query_search_engine** | **str** | The search engine domain for the query, if not set will be chosen according to &#x60;query_location_name&#x60; | [optional] 
**linked_data** | **bool** | Whether to include results from Linked Data (e.g. DBpedia), by default true. | [optional] [default to True]
**local_data** | **bool** | Whether to include results from the local Knowledge Graph, by default true. | [optional] [default to True]
**network_data** | **bool** | Whether to include results from connected Knowledge Graphs, by default true. | [optional] [default to True]

## Example

```python
from Wordlift_client.models.analyses_request import AnalysesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysesRequest from a JSON string
analyses_request_instance = AnalysesRequest.from_json(json)
# print the JSON string representation of the object
print(AnalysesRequest.to_json())

# convert the object into a dict
analyses_request_dict = analyses_request_instance.to_dict()
# create an instance of AnalysesRequest from a dict
analyses_request_from_dict = AnalysesRequest.from_dict(analyses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


