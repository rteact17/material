from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://touchstone_user:jjbn8046mBOfhroURnSmpcXxI0A4rcrg@dpg-cvscdluuk2gs739rvjq0-a.oregon-postgres.render.com/touchstone")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

