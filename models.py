from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Service(Base):
    __tablename__ = 'topology'
    serviceId = Column(String, primary_key=True)
    serviceName = Column(String)
    userId = Column(String)
    status = Column(String)
    port = Column(String)
    ip = Column(String)
    containerId = Column(String)
    redeployRequest = Column(String)

    def __repr__(self):
        return f"<Service(userid='{self.userId}', serviceid='{self.serviceId}')>"
