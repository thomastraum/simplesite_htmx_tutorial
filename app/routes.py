from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.config import Settings

settings = Settings()

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
templates.env.auto_reload = True
router = APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request, "page_title":42})

@router.get("/about")
def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "page_title":"about"})