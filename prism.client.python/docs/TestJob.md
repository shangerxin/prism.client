# TestJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**credential_id** | **int** |  | [optional] 
**default_test_machine_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**test_builds** | [**List[TestBuild]**](TestBuild.md) |  | [optional] 
**test_cases** | [**List[TestCase]**](TestCase.md) |  | [optional] 
**user_credential** | [**UserCredential**](UserCredential.md) |  | [optional] 
**test_job_parameters** | [**List[TestJobParameter]**](TestJobParameter.md) |  | [optional] 
**test_job_report_templates** | [**List[TestJobReportTemplate]**](TestJobReportTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_job import TestJob

# TODO update the JSON string below
json = "{}"
# create an instance of TestJob from a JSON string
test_job_instance = TestJob.from_json(json)
# print the JSON string representation of the object
print(TestJob.to_json())

# convert the object into a dict
test_job_dict = test_job_instance.to_dict()
# create an instance of TestJob from a dict
test_job_from_dict = TestJob.from_dict(test_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


