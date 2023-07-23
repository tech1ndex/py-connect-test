# py-connect-test
Simple Python container to test connectivity to URLs and log Status Code.

### Usage

Example with logging:

```
docker run -d -v /log:/log ghcr.io/tech1ndex/py-connect-test:<tag> -l -p /log -u "https://example.com" "https://example.com/test"
```

- `-v` will need to be passed if you plan to log to disk

List of `--urls` will need to be passed to Docker run/compose, the script will accept as many as required.


##### Parameters:

  `-h`, `--help` - show this help message and exit

  `-u [URLS ...]`, `--urls [URLS ...]` - A list of URLs to test against

  `-l`, `--log` - Use --log if you want output logged to a file, default is stdout

  `-p LOGPATH`, `--logpath LOGPATH` - Directory path to store logfile

  `-i INTERVAL`, `--interval INTERVAL` - Interval at which to run the test in seconds, default value is 30

  Note: `-l` and `-p` are dependent on each other. 

##### Architecture: 

Current available versions are:
  - amd64
  - arm64

They are version tagged accordingly and can be pulled using `version-arch` tag format.

```
docker pull ghcr.io/tech1ndex/py-connect-test:<tag>
```