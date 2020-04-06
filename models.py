from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Service(Base):
    __tablename__ = 'topology'
    serviceId = Column(String, primary_key=True)
    userId = Column(String)
    status = Column(String)
    port = Column(String)
    ip = Column(String)
    containerId = Column(String)
    redeployRequest = Column(String)

    def __repr__(self):
        return f"<Service(userid='{self.userId}', serviceid='{self.serviceId}')>"
