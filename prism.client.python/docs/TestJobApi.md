# openapi_client.TestJobApi

All URIs are relative to *https://localhost:44303*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_job_delete**](TestJobApi.md#test_job_delete) | **DELETE** /api/v1/TestJob/{id} | 
[**test_job_get**](TestJobApi.md#test_job_get) | **GET** /api/v1/TestJob | 
[**test_job_get_0**](TestJobApi.md#test_job_get_0) | **GET** /api/v1/TestJob/{id} | 
[**test_job_id**](TestJobApi.md#test_job_id) | **GET** /api/v1/TestJob/Id/{name} | 
[**test_job_post**](TestJobApi.md#test_job_post) | **POST** /api/v1/TestJob | 
[**test_job_put**](TestJobApi.md#test_job_put) | **PUT** /api/v1/TestJob/{id} | 


# **test_job_delete**
> test_job_delete(id)

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
    api_instance = openapi_client.TestJobApi(api_client)
    id = 56 # int | 

    try:
        api_instance.test_job_delete(id)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_delete: %s\n" % e)
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

# **test_job_get**
> str test_job_get()

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
    api_instance = openapi_client.TestJobApi(api_client)

    try:
        api_response = api_instance.test_job_get()
        print("The response of TestJobApi->test_job_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_get: %s\n" % e)
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

# **test_job_get_0**
> TestJob test_job_get_0(id)

### Example


```python
import openapi_client
from openapi_client.models.test_job import TestJob
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
    api_instance = openapi_client.TestJobApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.test_job_get_0(id)
        print("The response of TestJobApi->test_job_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_get_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TestJob**](TestJob.md)

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

# **test_job_id**
> str test_job_id(name)

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
    api_instance = openapi_client.TestJobApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.test_job_id(name)
        print("The response of TestJobApi->test_job_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

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

# **test_job_post**
> TestJob test_job_post(value)

### Example


```python
import openapi_client
from openapi_client.models.test_job import TestJob
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
    api_instance = openapi_client.TestJobApi(api_client)
    value = 'value_example' # str | 

    try:
        api_response = api_instance.test_job_post(value)
        print("The response of TestJobApi->test_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | 

### Return type

[**TestJob**](TestJob.md)

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

# **test_job_put**
> bool test_job_put(id, value)

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
    api_instance = openapi_client.TestJobApi(api_client)
    id = 56 # int | 
    value = 'value_example' # str | 

    try:
        api_response = api_instance.test_job_put(id, value)
        print("The response of TestJobApi->test_job_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestJobApi->test_job_put: %s\n" % e)
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

