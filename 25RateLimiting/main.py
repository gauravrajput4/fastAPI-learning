from fastapi import FastAPI,Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# Setup limiter
limiter=Limiter(key_func=get_remote_address)

app.state.limiter = limiter

# Error handle
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc:RateLimitExceeded):
    return JSONResponse({"message": "To many Request"}, exc.status_code)

# Rate Limiter API
@app.get("/ping")
@limiter.limit("5/minute")
def pong(request: Request):
    return {"ping": "pong"}
