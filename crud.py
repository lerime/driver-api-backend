from sqlalchemy.orm import Session

from models import Driver as DriverDB
from schemas import DriverFilter
from utils import DriverFilterQueryBuilder


def get_drivers(db: Session, filters: DriverFilter):
    q = DriverFilterQueryBuilder(**(filters.dict())).queries
    return db.query(DriverDB).filter(*q).all()
