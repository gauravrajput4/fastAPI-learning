from http.client import HTTPException

from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base,Session

from fastapi import FastAPI,Depends,HTTPException,status

app = FastAPI()

DATABASE_URL= "sqlite:///./test.db"
engine=create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread":False
    }
)

session_local=sessionmaker(bind=engine)

Base=declarative_base()

class Todo(Base):
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed=Column(Boolean)
Base.metadata.create_all(bind=engine)

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session=Depends(get_db)):
    return {
        "message":"DB connected file"
    }
# create API
@app.post("/todos")
def create_todo(title:str, db:Session=Depends(get_db)):
    todo=Todo(title=title,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo created successfully",
        "data":todo
    }

# Read all data
@app.get("/todos")
def read_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    return {
        "Total":len(todos),
        "data":todos
    }

# Read Specific Data using id
@app.get("/todos/{id}")
def read_todo(id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id == id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    status=todo.__dict__["completed"]
    if status:
        msg="Todo is completed"
    else:
        msg="Please Complete the Task....."
    return {
        "data":todo,
        "message":msg
    }

# Update API
@app.put("/todos/{id}")
def update_todo(id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo Not found"
        )
    todo.title=title
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo updated successfully",
        "data":todo
    }

# DELETE API
@app.delete("/todos/{id}")
def delete_todo(id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    db.delete(todo)
    db.commit()
    return {
        "message":"Todo deleted successfully"
    }

