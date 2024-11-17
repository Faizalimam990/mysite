from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine('mysql+pymysql://fyndproject:faizal123@fyndproject.mysql.pythonanywhere-services.com/fyndproject$fyndtest')
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

# 'mysql+pymysql://<USERNAME>:<PASSWORD>@<HOSTNAME>/<DATABASENAME>