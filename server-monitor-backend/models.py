from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ip_address = Column(String)
    status = Column(String)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    severity = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, server_default=func.now())

class UsageStat(Base):
    __tablename__ = "usage_stats"
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"))
    cpu = Column(Float)
    ram = Column(Float)
    disk = Column(Float)
    network_in = Column(Float)
    created_at = Column(DateTime, server_default=func.now())