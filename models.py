from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Driver(Base):
    __tablename__ = "driver_driver"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    driving_score = Column(Float)
    age = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
