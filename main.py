from fastapi import FastAPI, UploadFile, Response
from markitdown import MarkItDown
import tempfile
import os

app = FastAPI()

@app.post("/v1/markitdown")
def process(file: UploadFile):
  with tempfile.NamedTemporaryFile() as tmp:
    try:
      tmp.write(file.file.read())
      result = MarkItDown().convert(tmp.name)
      return Response(result.text_content, media_type="text/markdown", status_code=200)
    except Exception as error:
      return Response(str(error), media_type="text/plain", status_code=400)
    finally:
      os.unlink(tmp.name)
