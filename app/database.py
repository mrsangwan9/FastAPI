#--->> pip install sqlalchemy 
from sqlalchemy import create_engine #import create_engine a class from sqlaclchmey
#--->> sqlalchemy is an orm(you can understand like anthoer python lib) help to write command into our python file and it's convert those command into sql command 
# so we don't have to care about sql command //but still learned them they are easy..
from sqlalchemy.ext.declarative import declarative_base # to make a base class use into make module
from sqlalchemy.orm import sessionmaker # import sessionmaker to make session

SQLALCHEMY_DATABASE_ULR = 'postgresql://postgres:ilceditw@localhost/fastapi' # details of data base..
#database://<username>>:<password>@<hostname>/<database name>

engine = create_engine(SQLALCHEMY_DATABASE_ULR )#assign value into engine

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)#creae a Local session

Base = declarative_base() # make of object of declarative_base()
def get_db():# connection to database
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #db.close
""" this is most of copy paste system. you can change some data like variable name but don't because it not need to be ..
  but you must change ULR  that must be different in ur case... """