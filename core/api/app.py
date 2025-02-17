from fastapi import FastAPI, Request, APIRouter, status

from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import requests, base64
import asyncio
import uvicorn
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from core.api.Gear import Gear
class JohnAPI:
    def __init__(self):
        self._router__problem = APIRouter(prefix='/Problem', tags=['Problem'])
        self._router__ticket = APIRouter(prefix='/Ticket', tags=['Ticket'])
        self._router__problem.add_api_route(path="/", endpoint=self.endpoint_problem, methods=['GET', 'POST'])
        self._router__ticket.add_api_route(path="/", endpoint=self.endpoint_ticket, methods=['GET', 'POST'])

    def get_routers(self):
        return (self._router__ticket, self._router__problem)


    async def endpoint_ticket(self, request: Request):
        rqst_data = await self.validate_request(request)
        await asyncio.to_thread(sync_blocker_in_cockpit, rqst_data, endpoint='ticket')
        return status.HTTP_200_OK
    async def endpoint_problem(self, request: Request):
        rqst_data = await self.validate_request(request)
        await asyncio.to_thread(sync_blocker_in_cockpit, rqst_data, endpoint='problem')
        return status.HTTP_200_OK

    async def validate_request(self, request: Request):
        header = request.headers
        method = request.method
        body = await request.body()

        return {'header': header,
                'method': method,
                'body': body}

def sync_blocker_in_cockpit(rqst_data, endpoint):
    _ = Gear(rqst_data["body"], endpoint)
    return None


def start_app(host, port, verbose):

    app = FastAPI()
    routes = JohnAPI()
    for router in routes.get_routers():
        app.include_router(router)
    uvicorn.run(app, host=host, port=int(port), log_level="debug" if verbose else "info")
