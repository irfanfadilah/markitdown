# Run

```
docker build -t markitdown:latest .
docker run -p 8000:8000 markitdown
```

# API

```
curl --request POST \
  --url http://127.0.0.1:8000/v1/markitdown \
  --header 'Content-Type: multipart/form-data' \
  --form file=path/to/your/file.docx
```
