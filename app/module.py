from sqlalchemy import Column,Integer,String,Boolean #import data from sqlalchemy
from sqlalchemy.sql.expression import text # for convert time into str(text)
from sqlalchemy.sql.sqltypes import TIMESTAMP # for importing time

from .database import Base # current folder file database importing base class a object


class Post(Base):#class post it define how many Column are in the table create into this class and all property like str,integer anything 
    #what they will contain or or not they.every value can be define for table mypost with the help of class post
    __tablename__= "myposts" #create a table named myposts
     # value can't be different.
    id = Column(Integer,nullable = False,primary_key = True)# just value of column id 
    title = Column(String,nullable=False)# just value of column title 
    content = Column(String, nullable = False)# just value of column content
    published = Column (Boolean, server_default ='True',nullable = False) # just value of column published
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default =text('now()'))# just value of column created_at
    #it define the time when this row of data is created 
class Users(Base):#another class to define a table
    __tablename__ = 'NewUsers' #table name

    id = Column(Integer)# just value of column id 
    username = Column(String,nullable = False,primary_key = True)# just value of column username 
    password = Column(String,nullable = False)# just value of column password
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default =text('now()'))# just value of column created_at


"""Warning"""
# if someone create a table using any class but after some time he/she want to change or create new column then they have to delete/drop the table else it's not work 
# for python file.and data will not committ as  like as you want.

