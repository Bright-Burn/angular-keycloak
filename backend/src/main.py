from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(debug=False)


@app.get('/')
async def index() -> str:
    return "Hello World"


@app.get('/super/uber/files')
async def test(request: Request, auth_code: str = Query(...)):
    return {'url': str(request.url), 'code': auth_code}


@app.exception_handler(StarletteHTTPException)
async def handle(request: Request, exp):
    return JSONResponse(f"{request.url}")