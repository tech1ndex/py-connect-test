# py-connect-test

A simple Python package to test HTTP connectivity to URLs and retrieve status codes. Built with Typer CLI framework and httpx.

## Prerequisites

- Python 3.14 or higher
- Poetry (for dependency management)

## Installation

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
poetry run py-connect-test test
```

Or directly:

```bash
python -m py_connect_test.main test
```

### Options

#### Bypass SSL Certificate Validation

```bash
poetry run py-connect-test test --insecure
# or
poetry run py-connect-test test -i
```

#### Send Alerts to Webhook

```bash
poetry run py-connect-test test --alerts
# or
poetry run py-connect-test test -a
```

#### Combined Options

```bash
poetry run py-connect-test test --insecure --alerts
```

### View Help

```bash
poetry run py-connect-test test --help
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
