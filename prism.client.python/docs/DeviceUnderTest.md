# DeviceUnderTest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**machine_id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**test_machine** | [**TestMachine**](TestMachine.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_under_test import DeviceUnderTest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUnderTest from a JSON string
device_under_test_instance = DeviceUnderTest.from_json(json)
# print the JSON string representation of the object
print(DeviceUnderTest.to_json())

# convert the object into a dict
device_under_test_dict = device_under_test_instance.to_dict()
# create an instance of DeviceUnderTest from a dict
device_under_test_from_dict = DeviceUnderTest.from_dict(device_under_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


