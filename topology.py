from time import sleep

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import healthCheck
import rest_handler
from models import Service

DATABASE_URI = 'postgres+psycopg2://postgres:root@localhost:5432/ias-db'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def poll():
    s = Session()

    s.execute('SET search_path TO "ias-schema"')
    services = s.query(Service).filter_by(status='alive').filter_by(redeployRequest='false').all()

    print("services list:", services)
    for service in services:
        alive = healthCheck.check_health(service)
        if not alive:
            # TODO: call SLCM
            print("Service ", service.serviceId, "is down.")
            rest_handler.redeploy_service(service.serviceId)
            service.redeployRequest = 'true'
            s.add(service)
            s.commit()
        else:
            print("Service ", service.serviceId, "is alive.")

    s.close()


while True:
    poll()
    sleep(10)
