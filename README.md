# py-connect-test
Simple Python DockerFile to test connectivity to URLs and Log Status Code

### Usage

- Provided DockerFile can be built as is and run

### Parameters

`-v` will need to be passed as the script expects to write a logfile to /log

 List of `urls` will need to be passed to Docker run/compose, the script will accept as many as required

 ##### Example:

```
 docker run -d -v /log:/log ghcr.io/tech1ndex/py-connect-test:latest "https://test.tech1ndex.ca" "https://test.tech1ndex.ca/test"
 ```