# openapi_client.TestResultApi

All URIs are relative to *https://localhost:44303*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_result_add**](TestResultApi.md#test_result_add) | **POST** /api/v1/TestResult | 
[**test_result_add_environment**](TestResultApi.md#test_result_add_environment) | **POST** /api/v1/TestResult/AddEnvirnoment | 
[**test_result_add_metadata**](TestResultApi.md#test_result_add_metadata) | **POST** /api/v1/TestResult/AddMetadata | 
[**test_result_add_parameter**](TestResultApi.md#test_result_add_parameter) | **POST** /api/v1/TestResult/AddParameter | 
[**test_result_add_test_result**](TestResultApi.md#test_result_add_test_result) | **POST** /api/v1/TestResult/AddResult | 
[**test_result_compare_results**](TestResultApi.md#test_result_compare_results) | **GET** /api/v1/TestResult/CompareResults | 
[**test_result_compare_results_0**](TestResultApi.md#test_result_compare_results_0) | **POST** /api/v1/TestResult/CompareResults | 
[**test_result_get_environment**](TestResultApi.md#test_result_get_environment) | **GET** /api/v1/TestResult/Environment/{projectName}/{testJobName}/{buildGuid}/{dataInfo} | 
[**test_result_get_metadata**](TestResultApi.md#test_result_get_metadata) | **GET** /api/v1/TestResult/Metadata/{projectName}/{testJobName}/{buildGuid}/{dataInfo} | 
[**test_result_get_parameter**](TestResultApi.md#test_result_get_parameter) | **GET** /api/v1/TestResult/Parameter/{projectName}/{testJobName}/{buildGuid}/{dataInfo} | 
[**test_result_get_result**](TestResultApi.md#test_result_get_result) | **GET** /api/v1/TestResult/{projectName}/{testJobName}/{buildGuid}/{dataInfo} | 
[**test_result_get_results**](TestResultApi.md#test_result_get_results) | **POST** /api/v1/TestResult/GetResults | 


# **test_result_add**
> bool test_result_add(data, add_imp)

### Example


```python
import openapi_client
from openapi_client.models.func_string_task_boolean import FuncStringTaskBoolean
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    data = 'data_example' # str | 
    add_imp = openapi_client.FuncStringTaskBoolean() # FuncStringTaskBoolean | 

    try:
        api_response = api_instance.test_result_add(data, add_imp)
        print("The response of TestResultApi->test_result_add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**|  | 
 **add_imp** | [**FuncStringTaskBoolean**](FuncStringTaskBoolean.md)|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_add_environment**
> bool test_result_add_environment(environment)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    environment = 'environment_example' # str | 

    try:
        api_response = api_instance.test_result_add_environment(environment)
        print("The response of TestResultApi->test_result_add_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_add_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_add_metadata**
> bool test_result_add_metadata(metadata)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    metadata = 'metadata_example' # str | 

    try:
        api_response = api_instance.test_result_add_metadata(metadata)
        print("The response of TestResultApi->test_result_add_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_add_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_add_parameter**
> bool test_result_add_parameter(parameter)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    parameter = 'parameter_example' # str | 

    try:
        api_response = api_instance.test_result_add_parameter(parameter)
        print("The response of TestResultApi->test_result_add_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_add_parameter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_add_test_result**
> bool test_result_add_test_result(result)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    result = 'result_example' # str | 

    try:
        api_response = api_instance.test_result_add_test_result(result)
        print("The response of TestResultApi->test_result_add_test_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_add_test_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_compare_results**
> str test_result_compare_results(project_name, test_job_name, data_info, current_build_guid, compare_build_guid, reference_build_guid)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    project_name = 'project_name_example' # str | 
    test_job_name = 'test_job_name_example' # str | 
    data_info = 'data_info_example' # str | 
    current_build_guid = 'current_build_guid_example' # str | 
    compare_build_guid = 'compare_build_guid_example' # str | 
    reference_build_guid = 'reference_build_guid_example' # str | 

    try:
        api_response = api_instance.test_result_compare_results(project_name, test_job_name, data_info, current_build_guid, compare_build_guid, reference_build_guid)
        print("The response of TestResultApi->test_result_compare_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_compare_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **test_job_name** | **str**|  | 
 **data_info** | **str**|  | 
 **current_build_guid** | **str**|  | 
 **compare_build_guid** | **str**|  | 
 **reference_build_guid** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_compare_results_0**
> str test_result_compare_results_0(results)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    results = 'results_example' # str | 

    try:
        api_response = api_instance.test_result_compare_results_0(results)
        print("The response of TestResultApi->test_result_compare_results_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_compare_results_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **results** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_get_environment**
> str test_result_get_environment(project_name, test_job_name, build_guid, data_info)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    project_name = 'project_name_example' # str | 
    test_job_name = 'test_job_name_example' # str | 
    build_guid = 'build_guid_example' # str | 
    data_info = 'data_info_example' # str | 

    try:
        api_response = api_instance.test_result_get_environment(project_name, test_job_name, build_guid, data_info)
        print("The response of TestResultApi->test_result_get_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_get_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **test_job_name** | **str**|  | 
 **build_guid** | **str**|  | 
 **data_info** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_get_metadata**
> str test_result_get_metadata(project_name, test_job_name, build_guid, data_info)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    project_name = 'project_name_example' # str | 
    test_job_name = 'test_job_name_example' # str | 
    build_guid = 'build_guid_example' # str | 
    data_info = 'data_info_example' # str | 

    try:
        api_response = api_instance.test_result_get_metadata(project_name, test_job_name, build_guid, data_info)
        print("The response of TestResultApi->test_result_get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_get_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **test_job_name** | **str**|  | 
 **build_guid** | **str**|  | 
 **data_info** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_get_parameter**
> str test_result_get_parameter(project_name, test_job_name, build_guid, data_info)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    project_name = 'project_name_example' # str | 
    test_job_name = 'test_job_name_example' # str | 
    build_guid = 'build_guid_example' # str | 
    data_info = 'data_info_example' # str | 

    try:
        api_response = api_instance.test_result_get_parameter(project_name, test_job_name, build_guid, data_info)
        print("The response of TestResultApi->test_result_get_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_get_parameter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **test_job_name** | **str**|  | 
 **build_guid** | **str**|  | 
 **data_info** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_get_result**
> str test_result_get_result(project_name, test_job_name, build_guid, data_info)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    project_name = 'project_name_example' # str | 
    test_job_name = 'test_job_name_example' # str | 
    build_guid = 'build_guid_example' # str | 
    data_info = 'data_info_example' # str | 

    try:
        api_response = api_instance.test_result_get_result(project_name, test_job_name, build_guid, data_info)
        print("The response of TestResultApi->test_result_get_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_get_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **test_job_name** | **str**|  | 
 **build_guid** | **str**|  | 
 **data_info** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_get_results**
> str test_result_get_results(query)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:44303
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:44303"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TestResultApi(api_client)
    query = 'query_example' # str | 

    try:
        api_response = api_instance.test_result_get_results(query)
        print("The response of TestResultApi->test_result_get_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultApi->test_result_get_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

