from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,utile,module,oauth2

router = APIRouter(# just to route form another file
    tags=(['Authentication']) # for documention
)

@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)):
   user = db.query(module.Users).filter(module.Users.username == user_credentials.username).first()
   if not user:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid Credentials")
                                                # these value comes form database user.password
   if not utile.verify(user_credentials.password,user.password): 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid Credential")
        #now we have to create a token and return that token
        # if not error occure

   acces_token = oauth2.create_acces_token(data = {"user_id":user.id})
    
   

   return {"acces_toke": acces_token, "token_type":"bearer"}

    