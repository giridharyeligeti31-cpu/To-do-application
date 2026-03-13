from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
from database import SQLALCHEMY_DATABASE_URL

def test_crud():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    try:
        # Create
        print("Creating todo...")
        new_todo = models.Todo(title="Sync Test", description="Testing database sync")
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        todo_id = new_todo.id
        print(f"Created todo with ID: {todo_id}")
        
        # Read
        print("Reading todo...")
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
        print(f"Read todo: {todo.title}")
        
        # Update
        print("Updating todo...")
        todo.is_completed = True
        db.commit()
        db.refresh(todo)
        print(f"Updated status: {todo.is_completed}")
        
        # Delete
        print("Deleting todo...")
        db.delete(todo)
        db.commit()
        print("Clean up successful.")
        
    except Exception as e:
        print(f"CRUD Test FAILED: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_crud()
