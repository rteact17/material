from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "userss"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)  # admin or superadmin

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Tax(Base):
    __tablename__ = "tax"
    id = Column(Integer, primary_key=True)
    gst = Column(Float)

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    vehicle_number = Column(String)
    customer_name = Column(String)
    date_time = Column(DateTime, default=datetime.utcnow)
    bulk = Column(Boolean)
    material = Column(String)
    quantity = Column(Float)
    unit = Column(String)
    memo = Column(String, nullable=True)
    rate = Column(Float, nullable=True)
    created_by = Column(Integer, ForeignKey("userss.id"))

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    mode = Column(String)
    amount = Column(Float)
    date = Column(DateTime)
    remark = Column(String)


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    mode = Column(String)  # Cash or Bank
    amount = Column(Float)
    payment_date = Column(DateTime)
    remark = Column(String)
    created_by = Column(Integer, ForeignKey("userss.id"))
    

class CustomerVehicle(Base):
    __tablename__ = "customer_vehicle"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    vehicle_number = Column(String)
