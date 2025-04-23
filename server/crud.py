from models import Entry, Receipt, Tax, Payment
from schemas import EntryIn,PaymentIn
from sqlalchemy.orm import Session

def create_entry(db: Session, data, user_id):
    entry = Entry(**data.dict(), created_by=user_id)
    db.add(entry)
    db.commit()
    return entry

def create_receipt(db: Session, data):
    receipt = Receipt(**data.dict())
    db.add(receipt)
    db.commit()
    return receipt

def get_all_entries(db: Session):
    return db.query(Entry).all()

def get_tax(db: Session):
    return db.query(Tax).first()

# Additional CRUDs as needed

# Add/Update/Get tax information
def get_tax(db: Session):
    return db.query(Tax).first()

def update_tax(db: Session, gst_rate: float):
    tax = db.query(Tax).first()
    if tax:
        tax.gst_rate = gst_rate
    else:
        tax = Tax(gst_rate=gst_rate)
        db.add(tax)
    db.commit()
    db.refresh(tax)
    return tax

# Payment functions
def create_payment(db: Session, payment_data: PaymentIn, user_id: int):
    payment = Payment(**payment_data.dict(), created_by=user_id)
    db.add(payment)
    db.commit()
    return payment

def get_payments(db: Session, customer_name: str = None, date: str = None):
    query = db.query(Payment)
    if customer_name:
        query = query.filter(Payment.customer_name == customer_name)
    if date:
        query = query.filter(Payment.payment_date == date)
    return query.all()
