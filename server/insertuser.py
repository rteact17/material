# insert_users.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base,CustomerVehicle
import bcrypt
from database import DATABASE_URL

# Create database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the table if not already created
Base.metadata.create_all(bind=engine)

def add_vehicle(customer_name: str, vehicle_number: str):
    # Create a new user instance
    new_vehicle = CustomerVehicle(customer_name=customer_name, vehicle_number=vehicle_number)
    print(f"Adding vehicle: {customer_name}, Vehicle Number: {vehicle_number}")
    
    # Create a session
    session = SessionLocal()
    
    # Add the new vehicle to the session
    session.add(new_vehicle)
    
    # Commit the transaction
    session.commit()
    
    # Close the session
    session.close()
    print("Vehicle {customer_name} added successfully.")

add_vehicle('John Doe', 'ABC1234')
add_vehicle('Jane Smith', 'XYZ5678')

# # Function to add a user
# def add_user(username: str, role: str, password: str):
#     # Hash the password before storing it
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
#     # Create a new user instance
#     new_user = User(username=username, role=role, hashed_password=hashed_password)
#     print(f"Adding user: {username}, role: {role}, Password: {password}")
#     # Create a session
#     session = SessionLocal()
    
#     # Add the new user to the session
#     session.add(new_user)
    
    
#     # Commit the transaction
#     session.commit()
    
#     # Close the session
#     session.close()
#     print("User {username} added successfully.")

# # # Add sample users (replace with your own data)
# add_user('admin', 'admin', 'adminpassword')
# add_user('superadmin', 'superadmin', 'user1password')


# from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from models import User, Base
# from database import DATABASE_URL

# engine = create_engine(DATABASE_URL, echo=True)

# # # Create session local
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create a session
# db: Session = SessionLocal()

# # Query all users
# userss = db.query(User).all()
# print("Total users: {userss} {len(userss)}")

# # Print user details
# for user in userss:
#     print("ID: {user.id}, Username: {user.username}, role: {user.role}")

# # Close the session
# db.close()
