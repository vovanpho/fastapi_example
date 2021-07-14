from fastapi import APIRouter, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware 
import os
from typing import List
router = APIRouter()
templates = Jinja2Templates(directory="templates")