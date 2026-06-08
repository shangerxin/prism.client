# TestJobReportTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**test_job_id** | **int** |  | [optional] 
**email_to** | **str** |  | [optional] 
**email_cc** | **str** |  | [optional] 
**email_bcc** | **str** |  | [optional] 
**test_job** | [**TestJob**](TestJob.md) |  | [optional] 
**test_reports** | [**List[TestReport]**](TestReport.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_job_report_template import TestJobReportTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TestJobReportTemplate from a JSON string
test_job_report_template_instance = TestJobReportTemplate.from_json(json)
# print the JSON string representation of the object
print(TestJobReportTemplate.to_json())

# convert the object into a dict
test_job_report_template_dict = test_job_report_template_instance.to_dict()
# create an instance of TestJobReportTemplate from a dict
test_job_report_template_from_dict = TestJobReportTemplate.from_dict(test_job_report_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


