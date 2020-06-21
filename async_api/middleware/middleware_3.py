import time
from typing import Any, Awaitable, Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class Middleware3(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Any], Awaitable[Response]]):
        start_time = time.time()
        print(f"reached middleware 3: {start_time}")
        response = await call_next(request)
        end_time = time.time()
        process_time = end_time - start_time
        print(f"reached middleware 3: {process_time} = {end_time} - {start_time}")
        return response
