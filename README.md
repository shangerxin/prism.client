# Prism Python Client

Python helper for uploading benchmark and test artifacts to a Prism server.

This README is intentionally focused on `prism_client.py` usage and examples.

## Requirements

- Python 3.10+

## Install

From this folder:

```sh
pip install -r requirements.txt
```

Optional editable install:

```sh
pip install -e .
```

## What `prism_client.py` Uploads

The script can upload four metadata types:

- `result`: test result payload to `POST /TestResult/AddResult/`
- `env`: environment payload to `POST /TestResult/AddEnvirnoment/`
- `param`: parameter payload to `POST /TestResult/AddParameter/`
- `meta`: metadata payload to `POST /TestResult/AddMetadata/`

`host` should include the API prefix, for example `https://localhost:44303/api/v1`.

## CLI Usage

```sh
python prism_client.py host -t TEST_JOB -p PROJECT -m {env,meta,param,result} -n NAME (-j JSON | -c CSV) [options]
```

Required arguments:

- `host`: Prism server API root URL
- `-t, --test-job`: test job name
- `-p, --project`: project name
- `-m, --meta-type`: one of `env`, `meta`, `param`, `result`
- `-n, --name`: unique label (`dataInfo`) for the uploaded payload
- one of `-j, --json` or `-c, --csv`

Optional arguments:

- `-g, --build-guid`: build [GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) (auto-generated if omitted)
- `-s, --start`: start time (ISO string, defaults to current time)
- `-e, --end`: end time (ISO string, defaults to current time)
- `-x, --timeout-hours`: timeout in hours (default `0`)
- `-b, --build-result`: one of `NotExecuted|Pass|Fail|Blocked|InProgress|Hang|Paused|Aborted`
- `-r, --test-result`: one of `NotExecuted|Pass|Fail|Blocked|InProgress|Hang|Paused|Aborted`

## Example: Upload Test Result From JSON

Create `result.json`:

```json
{
    "summary": {
        "throughput": 1234,
        "latency_ms": 21.4,
        "passed": true
    },
    "details": [
        {
            "name": "case_001",
            "status": "Pass",
            "duration_ms": 120
        }
    ]
}
```

Run:

```sh
python prism_client.py https://your-prism-server/api/v1 \
    -p YourProject \
    -t YourTestJob \
    -m result \
    -n benchmark-run-20260609 \
    -j result.json \
    -b Pass \
    -r Pass
```

## Example: Upload Test Result From CSV

If you provide CSV, the script converts it to JSON before upload.

```sh
python prism_client.py https://your-prism-server/api/v1 \
    -p YourProject \
    -t YourTestJob \
    -m result \
    -n benchmark-run-csv \
    -c result.csv \
    -b Pass \
    -r Pass
```

## Example: Upload Environment / Parameter / Metadata

Environment:

```sh
python prism_client.py https://your-prism-server/api/v1 \
    -p YourProject \
    -t YourTestJob \
    -m env \
    -n hw-sw-info \
    -j environment.json
```

Parameter:

```sh
python prism_client.py https://your-prism-server/api/v1 \
    -p YourProject \
    -t YourTestJob \
    -m param \
    -n runtime-args \
    -j parameters.json
```

Metadata:

```sh
python prism_client.py https://your-prism-server/api/v1 \
    -p YourProject \
    -t YourTestJob \
    -m meta \
    -n build-info \
    -j metadata.json
```

## Python API Example (Using `prism_client.py` Functions)

```python
import json
import uuid
from datetime import datetime, timezone

from prism_client import upload_result

host = "https://your-prism-server/api/v1"
project = "YourProject"
test_job = "YourTestJob"
name = "benchmark-run-20260609"

with open("result.json", "r", encoding="utf-8") as f:
        payload = json.load(f)

upload_result(
        host=host,
        project=project,
        test_job=test_job,
        name=name,
        data=payload,
        build_guid=str(uuid.uuid4()),
        build_result="Pass",
        test_result="Pass",
        start=datetime.now(timezone.utc).isoformat(),
        end=datetime.now(timezone.utc).isoformat(),
        timeout_hours=0,
)
```

## Run Tests

```sh
pytest
```




