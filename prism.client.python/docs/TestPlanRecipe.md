# TestPlanRecipe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**test_plan_id** | **int** |  | [optional] 
**test_suit_id** | **int** |  | [optional] 
**test_case_id** | **int** |  | [optional] 
**schedual** | **str** |  | [optional] 
**test_case** | [**TestCase**](TestCase.md) |  | [optional] 
**test_plan** | [**TestPlan**](TestPlan.md) |  | [optional] 
**test_suite** | [**TestSuite**](TestSuite.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_plan_recipe import TestPlanRecipe

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanRecipe from a JSON string
test_plan_recipe_instance = TestPlanRecipe.from_json(json)
# print the JSON string representation of the object
print(TestPlanRecipe.to_json())

# convert the object into a dict
test_plan_recipe_dict = test_plan_recipe_instance.to_dict()
# create an instance of TestPlanRecipe from a dict
test_plan_recipe_from_dict = TestPlanRecipe.from_dict(test_plan_recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


