from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import models  # Import depuis le package app
from app.database import engine, get_db  # Import depuis le package app
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "healthy"}

class TodoBase(BaseModel):
    title: str
    description: str = None

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    completed: bool
    
    class Config:
        from_attributes = True  # Remplace orm_mode = True pour Pydantic v2

class PaginatedResponse(BaseModel):
    items: List[Todo]
    total: int
    page: int
    pages: int

@app.get("/todos", response_model=PaginatedResponse)
def get_todos(
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1, le=100),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    total = db.query(models.Todo).count()
    todos = db.query(models.Todo).offset(offset).limit(limit).all()
    
    return {
        "items": todos,
        "total": total,
        "page": page,
        "pages": (total + limit - 1) // limit
    }

@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"} 