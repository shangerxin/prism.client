# TestReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**report** | **str** |  | [optional] 
**build_id** | **int** |  | [optional] 
**test_report_template_id** | **int** |  | [optional] 
**test_build** | [**TestBuild**](TestBuild.md) |  | [optional] 
**test_job_report_template** | [**TestJobReportTemplate**](TestJobReportTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_report import TestReport

# TODO update the JSON string below
json = "{}"
# create an instance of TestReport from a JSON string
test_report_instance = TestReport.from_json(json)
# print the JSON string representation of the object
print(TestReport.to_json())

# convert the object into a dict
test_report_dict = test_report_instance.to_dict()
# create an instance of TestReport from a dict
test_report_from_dict = TestReport.from_dict(test_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


