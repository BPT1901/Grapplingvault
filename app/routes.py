from fastapi import APIRouter, HTTPException, Request, Query, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import JournalEntry
from app.schemas import JournalEntrySchema
from app.database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, search: str = Query(None)):
    if search:
        entries = list(db.entries.find({"category": {"$regex": search, "$options": "i"}}))
    else:
        entries = list(db.entries.find().sort("date", -1).limit(2))
    for entry in entries:
        entry["_id"] = str(entry["_id"])
    return templates.TemplateResponse("index.html", {"request": request, "entries": entries})

@router.get("/entry", response_class=HTMLResponse)
async def new_entry_form(request: Request):
    return templates.TemplateResponse("entry.html", {"request": request})

@router.get("/entry/{entry_id}", response_class=HTMLResponse)
async def edit_entry_form(request: Request, entry_id: str):
    entry = db.entries.find_one({"_id": ObjectId(entry_id)})
    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry["_id"] = str(entry["_id"])
    return templates.TemplateResponse("entry.html", {"request": request, "entry": entry})

@router.post("/entries/", response_model=JournalEntrySchema)
async def create_entry(title: str = Form(...), category: str = Form(...), entry: str = Form(...)):
    entry_dict = {"title": title, "category": category, "entry": entry, "date": datetime.now()}
    result = db.entries.insert_one(entry_dict)
    entry_dict["_id"] = str(result.inserted_id)
    return entry_dict

@router.post("/entries/{entry_id}", response_model=JournalEntrySchema)
async def update_entry(entry_id: str, title: str = Form(...), category: str = Form(...), entry: str = Form(...)):
    update_data = {"title": title, "category": category, "entry": entry}
    result = db.entries.update_one({"_id": ObjectId(entry_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Entry not found")
    updated_entry = db.entries.find_one({"_id": ObjectId(entry_id)})
    updated_entry["_id"] = str(updated_entry["_id"])
    return updated_entry

@router.get("/entries/{entry_id}", response_model=JournalEntrySchema)
async def read_entry(entry_id: str):
    entry = db.entries.find_one({"_id": ObjectId(entry_id)})
    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry["_id"] = str(entry["_id"])
    return entry