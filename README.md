# Run

```
docker stop markitdown && docker rm markitdown # Stop and Remove Existing Container
docker run --name markitdown -p 8000:8000 --pull=always -d ghcr.io/irfanfadilah/markitdown
```

# API

```
curl --request POST \
  --url http://localhost:8000/v1/markitdown \
  --header 'Content-Type: multipart/form-data' \
  --form file=path/to/your/file.docx
```

# Web

```
http://localhost:8000
```
