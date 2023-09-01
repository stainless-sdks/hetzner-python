# Hetzner Python API Library

[![PyPI version](https://img.shields.io/pypi/v/hetzner.svg)](https://pypi.org/project/hetzner/)

The Hetzner Python library provides convenient access to the Hetzner REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://docs.hetzner.com).

## Installation

```sh
pip install hetzner
```

## Usage

```python
from hetzner import Hetzner

client = Hetzner(
    # defaults to os.environ.get("HETZNER_API_TOKEN")
    api_token="my api token",
)

server = client.servers.create(
    name="my-server",
    image="ubuntu-20.04",
    server_type="cx11",
)
print(server.server.id)
```

While you can provide a `api_token` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `HETZNER_API_TOKEN="my api token"` to your `.env` file so that your API Token is not stored in source control.

## Async Usage

Simply import `AsyncHetzner` instead of `Hetzner` and use `await` with each API call:

```python
from hetzner import AsyncHetzner

client = AsyncHetzner(
    # defaults to os.environ.get("HETZNER_API_TOKEN")
    api_token="my api token",
)


async def main():
    server = await client.servers.create(
        name="my-server",
        image="ubuntu-20.04",
        server_type="cx11",
    )
    print(server.server_id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like serializing back into json ([v1](https://docs.pydantic.dev/1.10/usage/models/), [v2](https://docs.pydantic.dev/latest/usage/serialization/)). To get a dictionary, you can call `dict(model)`.

This helps provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Hetzner API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import hetzner

client = Hetzner()

all_servers = []
# Automatically fetches more pages as needed.
for server in client.servers.list():
    # Do something with server here
    all_servers.append(server)
print(all_servers)
```

Or, asynchronously:

```python
import asyncio
import hetzner

client = AsyncHetzner()


async def main() -> None:
    all_servers = []
    # Iterate through items across all pages, issuing requests as needed.
    async for server in client.servers.list():
        all_servers.append(server)
    print(all_servers)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.servers.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.servers)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.servers.list()

print(f"page number: {first_page.page}")  # => "page number: 1"
for server in first_page.servers:
    print(server.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from hetzner import Hetzner

client = Hetzner()

client.servers.create(
    name="my-server",
    image="ubuntu-20.04",
    server_type="cx11",
    firewalls=[
        {
            "firewall": 12,
        }
    ],
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `hetzner.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `hetzner.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `hetzner.APIError`.

```python
import hetzner
from hetzner import Hetzner

client = Hetzner()

try:
    client.actions.retrieve(
        1234,
    )
except hetzner.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except hetzner.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except hetzner.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from hetzner import Hetzner

# Configure the default for all requests:
client = Hetzner(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).servers.actions.poweroff(
    2345,
)
```

### Timeouts

Requests time out after 1 minute by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from hetzner import Hetzner

# Configure the default for all requests:
client = Hetzner(
    # default is 60s
    timeout=20.0,
)

# More granular control:
client = Hetzner(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).servers.actions.poweron(
    2345,
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from hetzner import Hetzner

client = Hetzner(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Advanced: Managing HTTP resources

By default we will close the underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__) is called but you can also manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally attempts to follow [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/hetzner/hetzner-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
