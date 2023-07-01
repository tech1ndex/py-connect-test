# py-connect-test
Simple Python DockerFile to test connectivity to URLs and Log Status Code

### Usage

List of `--urls` will need to be passed to Docker run/compose, the script will accept as many as required.

usage: py-connect-test.py [-h] [-u [URLS ...]] [-l]

##### options:

  `-h`, `--help` - show this help message and exit

  `-u [URLS ...]`, `--urls [URLS ...]` - A list of URLs to test against

  `-l`, `--log` - Use --log if you want output logged to a file, default is stdout

  `-p LOGPATH`, `--logpath LOGPATH` - Directory path to store logfile

  `-i INTERVAL`, `--interval INTERVAL` - Interval at which to run the test in seconds, default value is 30

### Docker

- `-v` will need to be passed if you plan to log to disk
- Provided DockerFile can also be built as is and run

##### Docker Pull: 

```
docker pull ghcr.io/tech1ndex/py-connect-test:amd64
```

##### Example:

```
docker run -d -v /log:/log ghcr.io/tech1ndex/py-connect-test:latest --log --urls "https://example.com" "https://example.com/test"
```