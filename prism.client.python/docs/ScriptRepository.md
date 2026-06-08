# ScriptRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**scripts** | [**List[Script]**](Script.md) |  | [optional] 

## Example

```python
from openapi_client.models.script_repository import ScriptRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptRepository from a JSON string
script_repository_instance = ScriptRepository.from_json(json)
# print the JSON string representation of the object
print(ScriptRepository.to_json())

# convert the object into a dict
script_repository_dict = script_repository_instance.to_dict()
# create an instance of ScriptRepository from a dict
script_repository_from_dict = ScriptRepository.from_dict(script_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


