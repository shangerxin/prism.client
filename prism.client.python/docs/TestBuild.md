# TestBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**test_job_id** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**build_result_id** | **int** |  | [optional] 
**test_result_id** | **int** |  | [optional] 
**guid** | **UUID** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**timeout_hours** | **float** |  | [optional] 
**result_type** | [**ResultType**](ResultType.md) |  | [optional] 
**result_type1** | [**ResultType**](ResultType.md) |  | [optional] 
**test_job** | [**TestJob**](TestJob.md) |  | [optional] 
**test_reports** | [**List[TestReport]**](TestReport.md) |  | [optional] 
**test_results** | [**List[TestResult]**](TestResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_build import TestBuild

# TODO update the JSON string below
json = "{}"
# create an instance of TestBuild from a JSON string
test_build_instance = TestBuild.from_json(json)
# print the JSON string representation of the object
print(TestBuild.to_json())

# convert the object into a dict
test_build_dict = test_build_instance.to_dict()
# create an instance of TestBuild from a dict
test_build_from_dict = TestBuild.from_dict(test_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


