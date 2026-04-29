from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.core.deps import get_current_user
from app.crud.user import get_user

router = APIRouter(prefix="/users", tags=["users"])

# get my profile
@router.get("/me")
def get_my_profile(user=Depends(get_current_user)):
    return user


# get user by id
@router.get("/{user_id}")
def get_user_by_id(user_id: int, db=Depends(get_db), user=Depends(get_current_user)):

    found_user = get_user(db, user_id)

    if not found_user:
        raise HTTPException(status_code=404, detail="User not found")

    return found_user