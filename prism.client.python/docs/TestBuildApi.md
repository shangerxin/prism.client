# openapi_client.TestBuildApi

All URIs are relative to *https://localhost:44303*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_build_build_list**](TestBuildApi.md#test_build_build_list) | **GET** /api/v1/TestBuild/BuildList/{testJobName}/{start}/{end} | 
[**test_build_delete**](TestBuildApi.md#test_build_delete) | **DELETE** /api/v1/TestBuild/{id} | 
[**test_build_get**](TestBuildApi.md#test_build_get) | **GET** /api/v1/TestBuild | 
[**test_build_get_0**](TestBuildApi.md#test_build_get_0) | **GET** /api/v1/TestBuild/{id} | 
[**test_build_guid**](TestBuildApi.md#test_build_guid) | **GET** /api/v1/TestBuild/GUID/{id} | 
[**test_build_id**](TestBuildApi.md#test_build_id) | **GET** /api/v1/TestBuild/Id/{guid} | 
[**test_build_last**](TestBuildApi.md#test_build_last) | **GET** /api/v1/TestBuild/LastSuccess/{testJobName}/{testResultType} | 
[**test_build_last_success**](TestBuildApi.md#test_build_last_success) | **GET** /api/v1/TestBuild/LastSuccess/{testJobName} | 
[**test_build_post**](TestBuildApi.md#test_build_post) | **POST** /api/v1/TestBuild | 
[**test_build_put**](TestBuildApi.md#test_build_put) | **PUT** /api/v1/TestBuild/{id} | 


# **test_build_build_list**
> str test_build_build_list(test_job_name, start, end)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    test_job_name = 'test_job_name_example' # str | 
    start = '2013-10-20T19:20:30+01:00' # datetime | 
    end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_response = api_instance.test_build_build_list(test_job_name, start, end)
        print("The response of TestBuildApi->test_build_build_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_build_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_job_name** | **str**|  | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

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

# **test_build_delete**
> test_build_delete(id)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    id = 56 # int | 

    try:
        api_instance.test_build_delete(id)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_build_get**
> str test_build_get()

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
    api_instance = openapi_client.TestBuildApi(api_client)

    try:
        api_response = api_instance.test_build_get()
        print("The response of TestBuildApi->test_build_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **test_build_get_0**
> str test_build_get_0(id)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.test_build_get_0(id)
        print("The response of TestBuildApi->test_build_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **test_build_guid**
> str test_build_guid(id)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.test_build_guid(id)
        print("The response of TestBuildApi->test_build_guid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_guid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **test_build_id**
> str test_build_id(guid)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    guid = 'guid_example' # str | 

    try:
        api_response = api_instance.test_build_id(guid)
        print("The response of TestBuildApi->test_build_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 

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

# **test_build_last**
> str test_build_last(test_job_name, test_result_type)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    test_job_name = 'test_job_name_example' # str | 
    test_result_type = 'test_result_type_example' # str | 

    try:
        api_response = api_instance.test_build_last(test_job_name, test_result_type)
        print("The response of TestBuildApi->test_build_last:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_last: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_job_name** | **str**|  | 
 **test_result_type** | **str**|  | 

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

# **test_build_last_success**
> str test_build_last_success(test_job_name)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    test_job_name = 'test_job_name_example' # str | 

    try:
        api_response = api_instance.test_build_last_success(test_job_name)
        print("The response of TestBuildApi->test_build_last_success:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_last_success: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_job_name** | **str**|  | 

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

# **test_build_post**
> TestBuild test_build_post(value)

### Example


```python
import openapi_client
from openapi_client.models.test_build import TestBuild
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
    api_instance = openapi_client.TestBuildApi(api_client)
    value = 'value_example' # str | 

    try:
        api_response = api_instance.test_build_post(value)
        print("The response of TestBuildApi->test_build_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | 

### Return type

[**TestBuild**](TestBuild.md)

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

# **test_build_put**
> bool test_build_put(id, value)

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
    api_instance = openapi_client.TestBuildApi(api_client)
    id = 56 # int | 
    value = 'value_example' # str | 

    try:
        api_response = api_instance.test_build_put(id, value)
        print("The response of TestBuildApi->test_build_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestBuildApi->test_build_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **value** | **str**|  | 

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

