[![PyPI version](https://badge.fury.io/py/py-connect-test.svg)](https://pypi.org/project/py-connect-test/)
[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)

# py-connect-test

A simple Python package to test HTTP connectivity to URLs and retrieve status codes. Built with Typer CLI framework and httpx.

## Prerequisites

- Python 3.14 or higher
- Poetry (for dependency management)

## Installation

### From PyPI

```bash
pip install py-connect-test
```
...

### From Source

```bash
git clone https://github.com/tech1ndex/py-connect-test.git
cd py-connect-test
poetry install
```

## Usage

### Basic Usage

Test connectivity to the default URL (https://ifconfig.me):

```bash
py-connect-test test
```

### Options

#### Bypass SSL Certificate Validation

```bash
py-connect-test test --insecure
# or
py-connect-test test -i
```

#### Send Alerts to Webhook

```bash
py-connect-test test --alerts
# or
py-connect-test test -a
```

#### Combined Options

```bash
py-connect-test test --insecure --alerts
```

### View Help

```bash
py-connect-test test --help
```

## Docker Usage

### Build Image

```bash
docker build -t py-connect-test:latest .
```

### Run Container

```bash
docker run -d \
  -e HTTP_URL=https://example.com \
  -e WEBHOOK_URL=http://prometheus.local \
  ghcr.io/tech1ndex/py-connect-test:latest
```

### Bypass SSL Validation

```bash
docker run -d \
  -e PY_CONNECT_TEST_URL=https://example.com \
  ghcr.io/tech1ndex/py-connect-test:latest \
  py-connect-test test --insecure
```

### Multi-Architecture Support

Available architectures:
- `amd64`
- `arm64`

Pull specific architecture:

```bash
docker pull ghcr.io/tech1ndex/py-connect-test:latest-amd64
docker pull ghcr.io/tech1ndex/py-connect-test:latest-arm64
```

## Environment Variables

| Variable              | Description | Default | Required |
|-----------------------|-------------|---------|----------|
| `PY_CONNECT_TEST_URL` | URL to test connectivity to | `https://ifconfig.me` | No |
| `WEBHOOK_URL`         | Webhook URL for alerts | `http://prometheus.local` | No |
| `PAYLOAD_FILE_PATH`   | Path to JSON payload file for webhooks | `/tmp/payload.json` | No |


## Project Structure

```
py-connect-test/
├── src/py_connect_test/
│   ├── main.py                 # CLI entry point
│   ├── settings.py             # Configuration management
│   ├── setup_logger.py         # Logger setup
│   ├── py.typed                # Type hints marker
│   └── services/
│       └── http.py             # HTTP service
├── tests/
│   ├── conftest.py            # Pytest fixtures
│   └── services/
│       └── test_http_service.py # HTTP service tests
├── pyproject.toml             # Project configuration
├── Dockerfile                 # Docker configuration
└── README.md
```
