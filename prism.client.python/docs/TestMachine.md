# TestMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**credential_id** | **int** |  | [optional] 
**device_under_tests** | [**List[DeviceUnderTest]**](DeviceUnderTest.md) |  | [optional] 
**user_credential** | [**UserCredential**](UserCredential.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_machine import TestMachine

# TODO update the JSON string below
json = "{}"
# create an instance of TestMachine from a JSON string
test_machine_instance = TestMachine.from_json(json)
# print the JSON string representation of the object
print(TestMachine.to_json())

# convert the object into a dict
test_machine_dict = test_machine_instance.to_dict()
# create an instance of TestMachine from a dict
test_machine_from_dict = TestMachine.from_dict(test_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


