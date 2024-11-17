from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Ensure you have models.py where your database models are defined

# Your DATABASE_URL for MySQL on PythonAnywhere
DATABASE_URL = "mysql+pymysql://fyndproject:faizal@123@fyndproject.mysql.pythonanywhere-services.com/fyndproject$fyndtest"

# Create an engine using the DATABASE_URL
engine = create_engine(DATABASE_URL)

# Create all tables based on the models
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session instance for later use in app.py
session = Session()
