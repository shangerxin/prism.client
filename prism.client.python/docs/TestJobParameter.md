# TestJobParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**test_job_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**test_job** | [**TestJob**](TestJob.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_job_parameter import TestJobParameter

# TODO update the JSON string below
json = "{}"
# create an instance of TestJobParameter from a JSON string
test_job_parameter_instance = TestJobParameter.from_json(json)
# print the JSON string representation of the object
print(TestJobParameter.to_json())

# convert the object into a dict
test_job_parameter_dict = test_job_parameter_instance.to_dict()
# create an instance of TestJobParameter from a dict
test_job_parameter_from_dict = TestJobParameter.from_dict(test_job_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


