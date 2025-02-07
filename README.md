# Run

```
docker build -t markitdown:latest .
docker create --name markitdown -p 8000:8000 markitdown
docker start markitdown
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
