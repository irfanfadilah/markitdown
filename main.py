from fastapi import FastAPI, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware
from markitdown import MarkItDown
import tempfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"]
)

@app.post("/v1/markitdown")
def process(file: UploadFile):
  with tempfile.NamedTemporaryFile(delete=True) as tmp:
    try:
      tmp.write(file.file.read())
      result = MarkItDown().convert(tmp.name)
      return Response(result.text_content, media_type="text/markdown", status_code=200)
    except Exception as error:
      return Response(str(error), media_type="text/plain", status_code=400)
