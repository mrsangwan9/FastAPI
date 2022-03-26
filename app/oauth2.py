from jose import JWTError, jwt 
#-->> pip install python-jose[cryptography]
from datetime import datetime,timedelta
from . import schemas,module
from .database import get_db
from fastapi import Depends,HTTPException ,status
from fastapi.security import OAuth2PasswordBearer #fast api class import
from sqlalchemy.orm import Session

oauth2_scheme= OAuth2PasswordBearer(tokenUrl='login') # login token
#secret key
#algorithm
#expression time( like time to loged in. after this time user have to login again..)
SECRET_KEY = "6c57846158b64705f13498ec072ab860"
ALGORITHM = 'HS256'#hash 256 
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # expire time


def create_acces_token(data: dict):
    to_encode =  data.copy()# data copy
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # here update or manage token expire time
    to_encode.update({"exp":expire}) # update token time
    
                            #update_time key algorithm
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)# created  a token 

    return encode_jwt # return token with time_to_expire secret_key and algorithm_for_token


def verify_access_token(token:str, credentials_exception):
     try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]) #decode the token data

        id:str= payload.get("user_id") # asign id to token id
        print(id)
        if id is None: # if id value is zero rasie error
            raise credentials_exception
        token_data = schemas.TokenData(id=id) #if not none then return id value

     except JWTError:
       raise credentials_exception

     return token_data
 


def get_current_user(token:str=Depends(oauth2_scheme),db:Session = Depends(get_db)):
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="login to access",
        headers={"WWW-Authenticate":"Bearer"})

        token = verify_access_token(token,credentials_exception)

        user = db.query(module.Users).filter(module.Users.id == token.id).first()
        print(user)
        
        return user