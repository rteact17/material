from pydantic import BaseModel
from typing import Optional

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    role: str

class EntryIn(BaseModel):
    vehicle_number: str
    customer_name: str
    date_time: str
    bulk: bool
    material: str
    quantity: float
    unit: str
    memo: Optional[str]

class ReceiptIn(BaseModel):
    customer_name: str
    mode: str
    amount: float
    date: str
    remark: str

class TaxIn(BaseModel):
    gst_rate: float

class TaxOut(TaxIn):
    id: int

class PaymentIn(BaseModel):
    customer_name: str
    mode: str
    amount: float
    payment_date: str
    remark: str

class PaymentOut(PaymentIn):
    id: int

class CustomerVehicleIn(BaseModel):
    customer_name: str
    vehicle_number: str