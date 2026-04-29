from app.models.user import User

def get_user_by_email(db, email):
    return db.query(User).filter_by(email=email).first()


def get_user_by_username(db, username):
    return db.query(User).filter_by(username=username).first()


def get_user(db, user_id):
    return db.query(User).filter_by(id=user_id).first()


def create_user(db, user, hashed_password):
    new_user = User(**user.dict(), hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user