from ..import module,schemas,utile
from fastapi import status,Depends,HTTPException,APIRouter 
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    tags=['users'] # router change to or access from another file
)


@router.post("/users",response_model=schemas.responseuser)#lock the response as schemas.responseuserr
def create_users(newuser:schemas.createusers,db:Session= Depends(get_db)):
    #cur.execute("""Insert into NewUsers(username,password) Values(%s,%s) Returning *""",(newuser.username,newuser.password))
   # created = cur.fetchone()
   # conn.commit()
   #hash the password  - user.pasword

    hashed_password= utile.hash(newuser.password)# change user password as hash passowrd
    newuser.password = hashed_password #again assign hash password to newuser pasword

    created = module.Users(
        **newuser.dict())# take value as schemas.createusers and put them into python dict.
    db.add(created)
    db.commit()
    db.refresh(created)# to reflect value 
    return created


@router.get('/users/{id}',response_model= schemas.responseuser)
def get_user(id:int,db:Session = Depends(get_db)):#db for connect to database..
    user = db.query(module.Users).filter(module.Users.id==id).first() #select first user module user tell that use select a user have properties of module
    

    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND)
    return user