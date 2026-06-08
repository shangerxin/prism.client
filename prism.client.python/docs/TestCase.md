# TestCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**job_id** | **int** |  | [optional] 
**script_id** | **int** |  | [optional] 
**script** | [**Script**](Script.md) |  | [optional] 
**test_job** | [**TestJob**](TestJob.md) |  | [optional] 
**test_plan_recipes** | [**List[TestPlanRecipe]**](TestPlanRecipe.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_case import TestCase

# TODO update the JSON string below
json = "{}"
# create an instance of TestCase from a JSON string
test_case_instance = TestCase.from_json(json)
# print the JSON string representation of the object
print(TestCase.to_json())

# convert the object into a dict
test_case_dict = test_case_instance.to_dict()
# create an instance of TestCase from a dict
test_case_from_dict = TestCase.from_dict(test_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


