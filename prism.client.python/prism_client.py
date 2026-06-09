#! /usr/bin/env python
"""
usage: prism_client.py [-h] -t TEST_JOB -p PROJECT [-c CSV] [-j JSON] [-m {env,meta,param,result}] -n NAME
                       [-s START] [-e END] [-x TIMEOUT_HOURS]
                       [-b {NotExecuted,Pass,Fail,Blocked,InProgress,Hang,Paused,Aborted}]
                       [-r {NotExecuted,Pass,Fail,Blocked,InProgress,Hang,Paused,Aborted}] [-g BUILD_GUID]
                       host

Prism client for helping save benchmark results to server.

positional arguments:
  host                  The server host api url such as https://localhost:44303/api/v1

options:
  -h, --help            show this help message and exit
  -t, --test-job TEST_JOB
                        The test job name.
  -p, --project PROJECT
                        The test project name
  -c, --csv CSV         The data to saved in the server
  -j, --json JSON       The data to saved in the server
  -m, --meta-type {env,meta,param,result}
                        The data type to save into the server.
  -n, --name NAME       Output root directory or a file path
  -s, --start START     The build start time
  -e, --end END         The build end time
  -x, --timeout-hours TIMEOUT_HOURS
                        The timeout hours for the test job, default is 0 which means no timeout.
  -b, --build-result {NotExecuted,Pass,Fail,Blocked,InProgress,Hang,Paused,Aborted}
                        The build result, pass or fail.
  -r, --test-result {NotExecuted,Pass,Fail,Blocked,InProgress,Hang,Paused,Aborted}
                        The test result, pass or fail.
  -g, --build-guid BUILD_GUID
                        Build GUID for tracking the build results in the server.
"""

import sys
import doctest
import json
import uuid

from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser

import openapi_client as api
from openapi_client.rest import ApiException, RESTResponse
from openapi_client.models import Project, TestResult, TestEnvironment, TestParameter, TestMetadata
from csv_to_json import csv_to_json_obj


config = api.Configuration(verify_ssl = False)
config.host = "https://localhost:44303/api/v1"

def parse_args():
    parser = ArgumentParser(description='Prism client for helping save benchmark results to server.')
    parser.add_argument('host', type=str, help='The server host api url such as https://localhost:44303/api/v1')
    parser.add_argument('-t', '--test-job', type=str, required=True, help='The test job name.')
    parser.add_argument('-p', '--project', default='Huggingface', type=str, required=True, help='The test project name')
    parser.add_argument('-c', '--csv',type=Path, help='The data to saved in the server')
    parser.add_argument('-j', '--json', type=Path, help='The data to saved in the server')
    parser.add_argument('-m', '--meta-type', type=str, choices=['env', 'meta', 'param', 'result'], help='The data type to save into the server.')
    parser.add_argument('-n', '--name', required=True, type=str, help='The name which is used to identify the saved data')
    parser.add_argument('-s', '--start', default=datetime.now().isoformat(), type=str, help="The build start time")
    parser.add_argument('-e', '--end', default=datetime.now().isoformat(), type=str, help="The build end time")
    parser.add_argument('-x', '--timeout-hours', default=0, type=int, help="The timeout hours for the test job, default is 0 which means no timeout.")
    parser.add_argument('-b', '--build-result', default='Pass', type=str, choices=['NotExecuted', 'Pass', 'Fail', 'Blocked', 'InProgress', 'Hang', 'Paused', 'Aborted'], help="The build result, pass or fail.")
    parser.add_argument('-r', '--test-result', default='Pass', type=str, choices=['NotExecuted', 'Pass', 'Fail', 'Blocked', 'InProgress', 'Hang', 'Paused', 'Aborted'], help="The test result, pass or fail.")
    parser.add_argument('-g', '--build-guid', default=str(uuid.uuid4()), help="Build GUID for tracking the build results in the server.")

    return parser.parse_args()


def get_project(host, id):
    with api.ApiClient(config) as api_client:
        # Create an instance of the API class
        result: RESTResponse = api_client.call_api("GET", f"{host}/Project/{id}", body="", header_params= {"Content-Type": "application/json"})
        if result.status == 200:
            data = result.read().decode('utf-8').replace('\\', '')[1:-1]
            result = Project.from_json(data)
            print(result)
        else:
            print(f"Failed to get project with id {id} from server, status code: {result.status}, reason: {result.reason}")


def _get_data_from_file(csv: Path, json: Path):
    if csv and json:
        raise ValueError("Only one of csv or json should be provided.")
    elif csv and csv.is_file():
        data = csv_to_json_obj(csv)
        return data
    elif json and json.is_file():
        with open(json, 'r') as f:
            data = json.load(f)
            return data
    else:
        raise ValueError("Either csv or json should be provided.")


def upload_result(host, project, test_job, name, data, build_guid, build_result, test_result, start, end, timeout_hours):
    with api.ApiClient(config) as api_client:
        # Create an instance of the API class

        body = TestResult(projectName=project, testJobName=test_job, buildGuid=build_guid, dataInfo=name, data=data, buildResult=build_result, testResult=test_result, startTime=start, endTime=end, timeoutHours=timeout_hours).to_json()
        result: RESTResponse = api_client.call_api("POST", f"{host}/TestResult/AddResult/", body=body, header_params={"Content-Type": "application/json"})

        if result.status == 200:
            print(f"Successfully uploaded data to server, response: {result.read().decode('utf-8')}")
        else:
            print(f"Failed to upload data to server, status code: {result.status}, reason: {result.reason}")


def upload_environment(host, project, test_job, name, data, build_guid):
    with api.ApiClient(config) as api_client:
        # Create an instance of the API class

        body = TestEnvironment(projectName=project, testJobName=test_job, buildGuid=build_guid, dataInfo=name, data=data).to_json()
        result: RESTResponse = api_client.call_api("POST", f"{host}/TestResult/AddEnvirnoment/", body=body, header_params={"Content-Type": "application/json"})

        if result.status == 200:
            print(f"Successfully uploaded data to server, response: {result.read().decode('utf-8')}")
        else:
            print(f"Failed to upload data to server, status code: {result.status}, reason: {result.reason}")


def upload_parameter(host, project, test_job, name, data, build_guid):
    with api.ApiClient(config) as api_client:
        # Create an instance of the API class

        body = TestParameter(projectName=project, testJobName=test_job, buildGuid=build_guid, dataInfo=name, data=data).to_json()
        result: RESTResponse = api_client.call_api("POST", f"{host}/TestResult/AddParameter/", body=body, header_params={"Content-Type": "application/json"})

        if result.status == 200:
            print(f"Successfully uploaded data to server, response: {result.read().decode('utf-8')}")
        else:
            print(f"Failed to upload data to server, status code: {result.status}, reason: {result.reason}")


def upload_metadata(host, project, test_job, name, data, build_guid):
    with api.ApiClient(config) as api_client:
        # Create an instance of the API class

        body = TestMetadata(projectName=project, testJobName=test_job, buildGuid=build_guid, dataInfo=name, data=data).to_json()
        result: RESTResponse = api_client.call_api("POST", f"{host}/TestResult/AddMetadata/", body=body, header_params={"Content-Type": "application/json"})

        if result.status == 200:
            print(f"Successfully uploaded data to server, response: {result.read().decode('utf-8')}")
        else:
            print(f"Failed to upload data to server, status code: {result.status}, reason: {result.reason}")


def main(args):
    data = _get_data_from_file(args.csv, args.json)
    if args.meta_type == 'result':
        upload_result(args.host, args.project, args.test_job, args.name, data, args.build_guid, args.build_result, args.test_result, args.start, args.end, args.timeout_hours)
    elif args.meta_type == 'env':
        upload_environment(args.host, args.project, args.test_job, args.name, data, args.build_guid)
    elif args.meta_type == 'param':
        upload_parameter(args.host, args.project, args.test_job, args.name, data, args.build_guid)
    elif args.meta_type == 'meta':
        upload_metadata(args.host, args.project, args.test_job, args.name, data, args.build_guid)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"*** Run doctest for {__file__}! ***")
        doctest.testmod(optionflags=doctest.ELLIPSIS |
                        doctest.IGNORE_EXCEPTION_DETAIL)
    else:
        main(parse_args())