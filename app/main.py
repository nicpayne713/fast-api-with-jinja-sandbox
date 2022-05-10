from fastapi import FastAPI, Request  # type:ignore
from fastapi.responses import HTMLResponse  # type:ignore
from fastapi.staticfiles import StaticFiles  # type:ignore
from fastapi.templating import Jinja2Templates  # type:ignore

from app.routers import unsplash

from .library import openfile

app = FastAPI()


app.include_router(unsplash.router)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openfile(page_name + ".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
