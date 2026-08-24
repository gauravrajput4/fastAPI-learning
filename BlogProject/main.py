from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models,schemas
from auth import create_token,verify_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Login API
@app.post("/login")
def login():
    return {
        "access_token":create_token({"user":"admin"}),
        "token_type":"bearer"
    }

@app.get("/")
def home():
    return {"message": "Blog App started"}

# Create Blog (Protected)
@app.post("/blog",response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate,db:Session=Depends(get_db),user=Depends(verify_token)):
    new_blog=models.Blog(
        title=blog.title,
        content=blog.content,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Get All Blog
@app.get("/blogs")
def read_blogs(db:Session=Depends(get_db),page:int=1, limit:int=5,search:str=Query(default="")):
    query=db.query(models.Blog)
    if search:
        query=query.filter(models.Blog.title.ilike(f"%{search}%"))

    total =query.count()
    start = (page-1)*limit
    end = (page)*limit

    blogs=query.offset(start).limit(limit).all()

    return {
        "page":page,
        "limit":limit,
        "total":total,
        "blogs":blogs

    }

@app.get("/blog/{id}",response_model=schemas.BlogResponse)
def read_blog(id:int,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    return blog

@app.put("/blog/{id}",response_model=schemas.BlogResponse)
def update_blog(id:int,blogs:schemas.BlogCreate,db:Session=Depends(get_db),user=Depends(verify_token)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=404,detail="Blog not found")

    if blogs.title=="string"  and blogs.content=="string":
        raise HTTPException(status_code=404,detail="Please enter a valid title")

    elif blogs.title=="string" or blogs.title=="":
        blog.content=blogs.content

    elif blogs.content=="string" or blogs.content=="":
        blog.title=blogs.title
    else:
        blog.title=blogs.title
        blog.content=blogs.content

    db.commit()
    db.refresh(blog)
    return blog

@app.delete("/blog/{id}",response_model=schemas.BlogResponse)
def delete_blog(id:int,db:Session=Depends(get_db),user=Depends(verify_token)):
    blog=db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=404,detail="Blog not found")
    db.delete(blog)
    db.commit()
    return blog
