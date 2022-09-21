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
