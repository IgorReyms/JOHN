from fastapi import FastAPI, Request, APIRouter, status

from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import requests, base64
import asyncio
import uvicorn
class JohnAPI:
    def __init__(self):
        self._router__task = APIRouter(prefix='/Task', tags=['Task'])
        self._router__ticket = APIRouter(prefix='/Ticket', tags=['Ticket'])
        self._router__task.add_api_route(path="/", endpoint=self.endpoint_task, methods=['GET', 'POST'])
        self._router__ticket.add_api_route(path="/", endpoint=self.endpoint_ticket, methods=['GET', 'POST'])

    def get_routers(self):
        return (self._router__ticket, self._router__task)

    async def endpoint_root(self, request: Request):
        rqst_data = await self.validate_request(request)
        loop = asyncio.to_thread()
        loop.run_in_executor()
        return status.HTTP_200_OK
    async def endpoint_ticket(self, request: Request):
        rqst_data = await self.validate_request(request)
        return status.HTTP_200_OK
    async def endpoint_task(self, request: Request):
        rqst_data = await self.validate_request(request)
        return status.HTTP_200_OK

    async def validate_request(self, request: Request):
        header = request.headers
        method = request.method
        body = await request.body()

        return {'header': header,
                'method': method,
                'body': body}

def sync_blocker_in_cockpit(body):
    print('ok')
    a = Gear(body)
    return None


def start_app(host, port, verbose):
    app = FastAPI()
    routes = JohnAPI()
    for router in routes.get_routers():
        app.include_router(router)
    uvicorn.run(app, host=host, port=int(port), log_level="debug" if verbose else "info")
