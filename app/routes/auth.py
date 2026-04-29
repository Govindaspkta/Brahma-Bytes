from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from app.schemas.user import UserCreate, Token, LoginRequest
from app.crud.user import get_user_by_username, get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db=Depends(get_db)):

    # check email
    existing_email = get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # check username
    existing_username = get_user_by_username(db, user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    # create user
    hashed_password = hash_password(user.password)
    new_user = create_user(db, user, hashed_password)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.post("/login")
def login(data: LoginRequest, db=Depends(get_db)):

    user = get_user_by_username(db, data.username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }