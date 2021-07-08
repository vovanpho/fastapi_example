# import module os cap thong tin cho hoat dong khong phu thuoc he dieu hanh
import os
# trinh dieu khien mongodb vs python khong dong bo <-> dong bo dung PyMongo import motor.motor_asyncio
# Tool SQL python va lap bieu do quan he sql
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
# Cơ sở dữ liệu cung cấp cho bạn hỗ trợ asyncio đơn giản cho nhiều loại cơ sở dữ liệu.
# from app.database import Database
# from core.config import settings
#
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/db_test")
# print(DATABASE_URL)
#
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
#
metadata = MetaData()
# moi mot session tuong ung voi mot class tuong ung
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# declarative_base return a class
Base=declarative_base()

