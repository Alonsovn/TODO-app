from sqlalchemy.orm import Session

from src import models


def get_user(db: Session, user_id: str):
    return db.query(models.User). \
        filter(models.User.id == user_id). \
        first()


def get_user_by_username(db: Session, username: str):
    try:
        db_user = db.query(models.User). \
            filter(models.User.username == username). \
            first()

        return db_user

    except Exception as e:
        print(f"Failed getting user by username. Error: {e}")
        
  
def create_user(db: session, user : schemas.UserCreate):
    id = uuid.uuid4()
    while get_user(db, str(id)):
        id = uuid.uuid4()
        
    db_user = models.User(str(id), username, name, email, hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def get_task_by_user_id(db: Session, id: str,  skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.user_id = id).offset(skip).limit(limit).all()


def get_task_by_id(db: Session, task_id: str):
    return db.query(models.Task). \
        filter(models.Task.id == task_id). \
        first()

def add_task(db: Session, task: schemas.TaskCreate, id : str):
    if not get_user(db, str(id)):
        return None
    
    task_id = uuid.uuid4()
    while get_task_by_id(db, str(task_id)):
        task_id = uuid.uuid4()
        
    db_task = models.Task(str(task_id), task.text, id)
    db.add(db_task)
    db.commit()
    
    db.refresh(db_task)
