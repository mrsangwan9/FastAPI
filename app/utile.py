from passlib.context import CryptContext
#-->> pip install passlib
pwd_context = CryptContext(schemes =['bcrypt'],deprecated = 'auto')#copy paste 
#-->>hash alogrithm is bcrypt..


def hash(passwrod:str):
    return pwd_context.hash(passwrod) 
''' this function take user plain password and return hash password to calling variable
    '''


def verify(plain_password,hashed_password): 
    return pwd_context.verify(plain_password,hashed_password)
""" This function to verfiy the user password with the help of password present into the database.. 
Every password is save into the database as hash password to match user password first we have to take hash password of that user from database
then user entre plain password convert into hash password if both are same then we will allow user to login else return error.. """