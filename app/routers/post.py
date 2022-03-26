from ..import module,schemas,oauth2 #.. stand for back in folder import these file
from fastapi import status,Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
"""db:Session = Depends(get_db) === Use for connection with database..."""

router= APIRouter(
  tags=['post']
)# for access or to route this file from another file.

@router.get("/")
def root():
    return  "that's the home page of Your social media account "


@router.get("/posts",response_model=List[schemas.CreatePost]) #here schemas work as response model
def all_post(db:Session= Depends(get_db)):
    #  cur.execute("""select * from posts""") #sql command
    #  posts = cur.fetchall()
    #  return {"data":posts}

    mypost = db.query(module.Post).all()#get all post 
    return  mypost

  

@router.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.responsepost)
def add_post(post:schemas.CreatePost,db:Session= Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
   # new_post= module.Post(title =post.title,content =post.content,published = post.published)
     #  cur.execute("""INSERT INTO posts (title, content, Published)  VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
   # single_post = cur.fetchone()
    #conn.commit()
  #  return {"your post":single_post}
    print(get_current_user.username) 
    new_post = module.Post(
        **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/posts/{id}")
def get_single_post(id:int,db:Session= Depends(get_db)):
  #  cur.execute("""Select * from posts where id= %s""",(str(id),))
 #   mypost = cur.fetchone()
    mypost= db.query(module.Post).filter(module.Post.id==id).first()
    if not mypost:
       return{ "Your post": "Sorry their is not post with your id number..."} 
    else:
       return mypost


@router.put("/posts/{id}")                                                                    #use to verify that user is login or not...
def update_post(id:int,updated_post:schemas.Post,db:Session= Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):#update schemas will fix what you can update into any post
    post_query = db.query(module.Post).filter(module.Post.id==id)
    post= post_query.first()# select first matching query
    post_query.update(updated_post.dict(),synchronize_session=False) #update query
    db.commit()#commit to db
  #  cur.execute("""update posts set title= %s,content = %s, published = %s where id = %s returning *""",
   # (post.title,post.content,post.published,(str(id))))
   # cur.execute("""update posts set title = %s where id = %s returning *""",
                #(newupdate.title,(str(id))),)
   # update_post = cur.fetchone()
   # conn.commit()
    if post ==None:
             raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="post not found")
    else:
       return post_query.first()


@router.delete("/posts/{id}")                     #verify that user is login or not
def del_post(id:int,db:Session= Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
   # cur.execute("""DELETE  FROM posts WHERE id = %s RETURNING *""",(str(id),))
   ## Deleted_post =  cur.fetchone()
    #conn.commit()
    Delete_post = db.query(module.Post).filter(module.Post.id==id).first()
    db.delete(Delete_post)
    db.commit()
    if Delete_post == None:
             raise HTTPException(Status_code= status.HTTP_404_NOT_FOUND)
    else:
          return Delete_post


          # all data are in every operation same just small keyword change..