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
