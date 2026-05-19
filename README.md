# py-connect-test
Simple Python container to test connectivity to URLs and log Status Code.

### Example Usage

```
python -m py_connect_test
```

#### Bypass SSL Certificate Validation

```
python -m py_connect_test -i
```

#### Docker Usage

```
docker run -d ghcr.io/tech1ndex/py-connect-test:<tag>"
```


##### Architecture: 

Current available versions are:
  - amd64
  - arm64

They are version tagged accordingly and can be pulled using `version-arch` tag format.

```
docker pull ghcr.io/tech1ndex/py-connect-test:<tag>
```