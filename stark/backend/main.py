  
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware



app = FastAPI(
    title="Welcome to Stark CMS", openapi_url=f"/stark/openapi.json"
)

@app.get('/')
def read_root():
    return {"Hello": "World"}