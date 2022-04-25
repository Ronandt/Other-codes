import uvicorn

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates

import os
import shelve  # Persistent storage
from datetime import datetime
from uuid import uuid4  # Unique key generator

BASEDIR = os.getcwd()
DBDIR = f"{BASEDIR}/database/notes"  # Database to be stored in database folder, with name "notes"
templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

app = FastAPI()  # creates app instance


@app.get("/", response_class=HTMLResponse)
def page_home(request: Request):
    db = shelve.open(DBDIR, "c")

    notes = dict(db)  # Retrieval of all the notes

    db.close()
    return templates.TemplateResponse(
        "home.html", {"request": request, "title": "Home", "notes": notes}
    )


"""
Creation of Notes
"""

(lambda x: x*2)(3)
@app.get("/create", response_class=HTMLResponse)  # Return HTML file
def page_create_notes(request: Request):
    return templates.TemplateResponse(
        "create_notes.html", {"request": request, "title": "Create"}
    )


@app.post("/create", response_class=RedirectResponse)  # Process form data
def create_notes(subject: str = Form(...), content: str = Form(...)):
    db = shelve.open(DBDIR, "c")  # Create if dosent exist
    uuid = str(uuid4())[:8]  # First 8 characters of UUID4
    # Inserting a note into a Dictionary (Shelve)
    db[uuid] = {
        "id": uuid,
        "subject": subject,
        "content": content,
        "date_created": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "date_updated": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    db.close()  # To prevent data corruption/loss of data
    return RedirectResponse(url="/create", status_code=302)


# Deletion of Notes
@app.post("/delete", response_class=RedirectResponse)
def delete_notes(uuid: str = Form(...)):  # Key for notes deletion
    print(uuid, "is going to be deleted now!")

    db = shelve.open(DBDIR, "c")
    del db[uuid]  # Deletion of a note using its key
    db.close()

    print(uuid, "has been deleted!")
    return RedirectResponse(url="/", status_code=302)  # Redirection status code


# update Notes
# To update something in the Dict to overwrite it.

@app.get("/update/{uuid}", response_class=HTMLResponse)
def page_notes_update(request: Request, uuid):
    db = shelve.open(DBDIR, "c")
    target = db[uuid]
    db.close()
    return templates.TemplateResponse("update_notes.html", {
        "request": request, "data": target
    })


@app.post("/update", response_class=RedirectResponse)
def notes_update(
        uuid: str = Form(...), subject: str = Form(...), content: str = Form(...)
):
    db = shelve.open(DBDIR)
    data = db[uuid]

    data["subject"] = subject
    data["content"] = content
    data["date_updated"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    db[uuid] = data
    db.close()
    return RedirectResponse(url="/", status_code=302)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
#     Needed to run the site
