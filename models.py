from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///main.db', echo=True)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    gender = Column(String)
    business_unit = Column(String)
    status = Column(String)
    joined_date = Column(Date)
    terminated_date = Column(Date)
    profile = Column(Integer)
    suspect = Column(Boolean)
    location = Column(String)

class PC_Access(Base):
    __tablename__ = 'pc_access'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    access_date_time = Column(DateTime)
    log_on_off = Column(String)
    machine_name = Column(String)
    machine_location = Column(String)
    suspect = Column(Integer)

class Building_Access(Base):
    __tablename__ = 'building_access'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    access_date_time = Column(DateTime)
    direction = Column(String)
    status = Column(String)
    office_location = Column(String)
    suspect = Column(Integer)

class Proxy_Log(Base):
    __tablename__ = 'proxy_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    access_date_time = Column(DateTime)
    machine_name = Column(String)
    url = Column(String)
    category = Column(String)
    bytes_in = Column(Integer)
    bytes_out = Column(Integer)
    suspect = Column(Integer)