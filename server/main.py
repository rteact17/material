from fastapi import FastAPI, Depends, HTTPException
from schemas import *
from auth import *
from crud import *
from sms import send_sms
from models import User, CustomerVehicle
from database import Base, engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/login")
def login(user: UserIn, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": create_access_token({"sub": user.username}), "token_type": "bearer"}

# Entries
@app.post("/entry")
def add_entry(data: EntryIn, current_user: User = Depends(verify_token), db: Session = Depends(get_db)):
    entry = create_entry(db, data, current_user.id)
    send_sms(data.customer_name, data.vehicle_number, data.material, data.quantity)
    return entry

# Payment Route
@app.post("/payment")
def add_payment(data: PaymentIn, current_user: User = Depends(verify_token), db: Session = Depends(get_db)):
    return create_payment(db, data, current_user.id)

# Get all payments for admin or superadmin
@app.get("/payments")
def list_payments(customer_name: str = None, date: str = None, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    return get_payments(db, customer_name, date)

# Tax Route (GET for superadmin or admin)
@app.get("/tax")
def get_current_tax(db: Session = Depends(get_db)):
    tax = get_tax(db)
    if not tax:
        raise HTTPException(status_code=404, detail="Tax not found")
    return tax

@app.post("/tax")
def update_tax_rate(tax: TaxIn, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    # Only superadmin can update the tax rate
    if current_user.role != "superadmin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return update_tax(db, tax.gst_rate)

# Reporting Routes
@app.get("/report")
def generate_report(db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    # Add more reporting logic here
    pass

@app.get("/vehicleCustomer")
def get_vehicle_customer(cust: str = None, veh: str = None, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    # Query using SQLAlchemy model
    vehicle_customer = db.query(CustomerVehicle).filter(CustomerVehicle.vehicle_number == veh or CustomerVehicle.customer_name == cust ).first()
    return vehicle_customer