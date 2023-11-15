from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.config import Settings

from app.crud import CRUD

settings = Settings()

templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
templates.env.auto_reload = True
router = APIRouter()

@router.get("/")
def index(request: Request):
    db = CRUD().with_table("artist_info")
    random_artist = db.get_random_item()
    # print(random_artist)
    return templates.TemplateResponse("main.html", {
        "request": request, 
        "page_title":"big tits", 
        "random_artist":random_artist
    })

@router.get("/about")
def index(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "page_title":"about"})

@router.get("/catalog")
def catalog(request: Request):
    """Catalog page - display information about artists in database."""

    db = CRUD().with_table("artist_details")
    artists = db.all_items()

    def get_members(artist: dict):
        """This returns active members from the artist_details table. This
        method can be used within the Jinja template."""

        if "members" not in artist:
            return [artist["name"]]
        all_members = artist["members"]
        active_members = []
        for member in all_members:
            if member["active"]:
                active_members.append(member["name"])
        return active_members # limit 14 members

    def get_website(artist: dict):
        if "urls" not in artist:
            return artist["uri"]  # send discogs uri if no url found
        return artist["urls"][0]

    return templates.TemplateResponse(
            "catalog.html",
            {
                "request": request,
                "artists": artists,
                "get_members": get_members,
                "get_website": get_website,
            }
        )