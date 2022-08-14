from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
from database import SessionLocal
from schemas import DriverResponse, DriverFilter

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/drivers/", response_model=DriverResponse)
def get_users(
        driver: DriverFilter,
        db: Session = Depends(get_db)
):
    drivers = []
    try:
        drivers = crud.get_drivers(db, driver)
        response_dict = {"code": "0", "msg": "success", "records": drivers}
    except Exception as exc:
        response_dict = {"code": "-1", "msg": "failure", "records": drivers}
    return DriverResponse(**response_dict)
