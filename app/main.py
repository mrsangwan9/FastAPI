#--->> pip install fastapi[all]
from fastapi import FastAPI #we can say it's a framework on which we are going to make our app..like make a instance(object) ctrl+mouse right click to any class details in vs code
from psycopg2.extras import RealDictCursor #A cursor that uses a real dict as the base type for rows.just simple use to change data into python dict.
import time # use time.sleep(time) method
#--->> pip install psycopg2 
import psycopg2  #A Python driver for PostgreSQL need to connect python file to postgresql database 
from . import module #import module to use here . stand for curent file
from .database import engine #curent file database import engine
from  .routers import post,users,auth # import file post, users, auth from folder routers



app = FastAPI()#create an object of FASTAPI

module.Base.metadata.create_all(bind=engine)# to bind module file
#just copy and paste only just the moudel name that can be vary else cp and pt



while True:#will try untill not connect to database for any reason. but it can be not good when ur info is wrong.like password or anyother. but good at when not connect to database because of internet
    try:
        conn =  psycopg2.connect(
                                host="localhost",#our local host name it can be an ip address of our website where our website is hosting like aws.they provide hosting address
                                database="fastapi",#database name can be anything like you want
                                user="postgres",#your username is different
                                password="ilceditw",#your password must be different or can be anything
                                port=5432,#your port number where you will access your database. by default 5432 for postgressql
                                cursor_factory=RealDictCursor #just to change data into python dict
                                
                                )
        print("connected to database...")#the line will print when connected to database..
        cur = conn.cursor()#use to operation into database from python file like excute data we will use cur.excute(operation)
        break # if connected to database then it will break the loop create by {while True}
    except Exception as error: #if not connected to database will show an error
                print(error)# error printed
                time.sleep(2) # will try again after 2 second function come from import time.


#---->>>
#----->>>
app.include_router(users.router) #this line connect main file to users file present in routers folder 
app.include_router(post.router)# main to post
app.include_router(auth.router)# main to auth

#--->> this all line means just to route every or bind users,post,auth to main file every request come to main file to access
# these file it will router or turn the request to these file.
