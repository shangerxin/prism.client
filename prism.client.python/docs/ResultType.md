# ResultType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**test_builds** | [**List[TestBuild]**](TestBuild.md) |  | [optional] 
**test_builds1** | [**List[TestBuild]**](TestBuild.md) |  | [optional] 
**test_results** | [**List[TestResult]**](TestResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.result_type import ResultType

# TODO update the JSON string below
json = "{}"
# create an instance of ResultType from a JSON string
result_type_instance = ResultType.from_json(json)
# print the JSON string representation of the object
print(ResultType.to_json())

# convert the object into a dict
result_type_dict = result_type_instance.to_dict()
# create an instance of ResultType from a dict
result_type_from_dict = ResultType.from_dict(result_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


