# BotStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bot (e.g., GPTBot, Claude-Web, Googlebot) | [optional] 
**vendor** | **str** | Vendor of the bot (e.g., OpenAI, Anthropic, Google) | [optional] 
**status** | **str** | Access status for this bot | [optional] 

## Example

```python
from wordlift_client.models.bot_status import BotStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BotStatus from a JSON string
bot_status_instance = BotStatus.from_json(json)
# print the JSON string representation of the object
print(BotStatus.to_json())

# convert the object into a dict
bot_status_dict = bot_status_instance.to_dict()
# create an instance of BotStatus from a dict
bot_status_from_dict = BotStatus.from_dict(bot_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


