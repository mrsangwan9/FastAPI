''' when use into decorater it will use as response module 
                              when pass as function argument then it work as request  module
                                                        '''


from typing import Optional # for making any data optional..
from pydantic import BaseModel,EmailStr 
#--->> pip install pydantic 
#pydantic is a python lib define basemodel of request or responses and manymore
 # can be a lot of number of schemas in a single application
class Post(BaseModel):#that's the base model means user input must be like this can be more then that but must be atleast these field fill up.

                 content:str
                 title:str
                 published:bool= False
   

class Config:# for python dict
        orm_mode=True

class CreatePost(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
    content:str
    title:str
    published:bool=False
                                #get or request for just these column write on this class
    class Config:
        orm_mode=True
    
class responsepost(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
    content:str
    title:str
                        #get or request for just these column write on this class
    class Config:
        orm_mode=True#for python dict.


class createusers(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
        username:EmailStr
        password:str            #get or request for just these column write on this class


class responseuser(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
      username:str

      class Config:
        orm_mode=True

                                        #get or request for just these column write on this class


class UserLogin(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
        username:EmailStr
        password:str

                                #get or request for just these column write on this class
#class PostCreate(Post):# extends post class
    
class Token(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
        access_token :str
        token_type:str
                                #get or request for just these column write on this class

class TokenData(BaseModel):# can be use in anywhere for response as well as for reqeust from server..
        id:Optional[str] = None
                                #get or request for just these column write on this class




                                #--->>> any schemas define here can user for request and response....