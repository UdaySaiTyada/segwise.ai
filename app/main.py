from fastapi import FastAPI, HTTPException, Query
from app import database, models, crud, utils
from app.models import GameData

app = FastAPI()

# Dependency to get database session
from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
from sqlalchemy.orm import Session
from app.database import get_db

@app.on_event("startup")
async def startup():
    database.init_db()


@app.post("/api/v1/upload/csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):

    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")

    try:
        # Read the uploaded file
        csv_content = await file.read()
        data = utils.parse_csv_content(csv_content.decode("utf-8"))
        crud.store_data(db, data)
        return {"message": "Data uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/query")
async def query_data(
    field: str = None,  # Make field optional
    value: str = None,  # Make value optional
    match_type: str = Query(default="exact", enum=["exact", "substring"]),
    db: Session = Depends(get_db),
):
    try:
        query = db.query(GameData)

        # Return all records if no field or value is provided
        if not field or not value:
            return query.all()

        # Handle query based on match type
        if match_type == "exact":
            query = query.filter(getattr(GameData, field) == value)
        elif match_type == "substring":
            query = query.filter(getattr(GameData, field).ilike(f"%{value}%"))

        result = query.all()

        if not result:
            raise HTTPException(status_code=404, detail="No matching records found.")

        return result

    except AttributeError:
        raise HTTPException(status_code=400, detail=f"Field '{field}' does not exist.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

