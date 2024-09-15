from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

# Create a Limiter instance
limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])

# Initialize FastAPI app
app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):

    return JSONResponse(
        status_code=429,
        content={"message": "Ha custom message ala pahije donhi route la"},
    )


# Example route with global rate limiting
@app.get("/example")
@limiter.limit("5/minute")  # Specific limit for this route
async def example(request: Request):
    return {"message": "This route is rate limited to 5 requests per minute."}


# Another route that uses the global limit
@app.get("/another-example")
async def another_example(request: Request):
    return {"message": "This route follows the global limit of 10 requests per minute."}


# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI server with SlowAPI rate limiting!"}


# Start the server using `uvicorn`
# Run this command in your terminal:
# uvicorn filename:app --reload
