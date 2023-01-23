## DRF Request logger

[![PyPi version](https://badgen.net/pypi/v/drf-tracking-logger/)](https://pypi.org/project/drf-tracking-logger/)

A spinoff of the [drf-tracking](https://github.com/aschn/drf-tracking) to forward the logging to the standard output instead of saving it in the database

## Installation

```bash
pip install drf-tracking-logger
```

## Usage

To use a specific logger name, set an environment variable
`TRACKING LOGGER`.

The package provides a mixin `LoggingMixin` which you can include to your class based views to log the requests.

*Example*,
```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from drf_tracking_logger.mixins import LoggingMixin

class AnyRandomView(LoggingMixin, ListModelMixin, GenericAPIView):
    ...
```

## Options
- `logging_methods` : This attribute can used to strip down the request methods which needs to be logged. **It logs all the methods by default**.
- `should_log` : This method can be used to customize the logic to determine the logging.
- `handle_log` : You can override this method to change the logging behavior. It sends the log to the configured logger by default.
- `sensitive_fields` : By default, any key name which has any of `'key', 'secret', 'password', 'signature'` in its name, will get its value hidden. But you can extend this list by adding more using this attribute.

## Logging Overview
You'll get these attributes for every request/response cycle to a view that uses the mixin:

 Model field name | Description | Model field type
------------------|-------------|-----------------
`user` | User if authenticated, None if not | Foreign Key
`requested_at` | Date-time that the request was made | DateTimeField
`response_ms` | Number of milliseconds spent in view code | PositiveIntegerField
`path` | Target URI of the request, e.g., `"/api/"` | CharField
`view` | Target VIEW of the request, e.g., `"views.api.ApiView"` | CharField
`view_method` | Target METHOD of the VIEW of the request, e.g., `"get"`| CharField
`remote_addr` | IP address where the request originated (X_FORWARDED_FOR if available, REMOTE_ADDR if not), e.g., `"127.0.0.1"` | GenericIPAddressField
`host` | Originating host of the request, e.g., `"example.com"` | URLField
`method` | HTTP method, e.g., `"GET"` | CharField
`query_params` | Dictionary of request query parameters, as text | TextField
`data` | Dictionary of POST data (JSON or form), as text | TextField
`response` | JSON response data. **This will be skipped for GET requests** | TextField
`status_code` | HTTP status code, e.g., `200` or `404` | PositiveIntegerField
