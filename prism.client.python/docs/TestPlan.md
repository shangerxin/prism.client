# TestPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**test_plan_recipes** | [**List[TestPlanRecipe]**](TestPlanRecipe.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_plan import TestPlan

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlan from a JSON string
test_plan_instance = TestPlan.from_json(json)
# print the JSON string representation of the object
print(TestPlan.to_json())

# convert the object into a dict
test_plan_dict = test_plan_instance.to_dict()
# create an instance of TestPlan from a dict
test_plan_from_dict = TestPlan.from_dict(test_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


