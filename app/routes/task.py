from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.core.deps import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate
from app.crud.task import get_tasks, get_task, create_task, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
def list_tasks(db=Depends(get_db), user=Depends(get_current_user)):
    return get_tasks(db, owner_id=user.id)


@router.post("/")
def create_new_task(task: TaskCreate, db=Depends(get_db), user=Depends(get_current_user)):
    new_task = create_task(db, task, owner_id=user.id)
    return new_task


@router.get("/{task_id}")
def get_task_by_id(task_id: int, db=Depends(get_db), user=Depends(get_current_user)):

    task = get_task(db, task_id, owner_id=user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.patch("/{task_id}")
def update_task_by_id(task_id: int, task: TaskUpdate, db=Depends(get_db), user=Depends(get_current_user)):

    updated_task = update_task(db, task_id, task, owner_id=user.id)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated_task


@router.delete("/{task_id}")
def delete_task_by_id(task_id: int, db=Depends(get_db), user=Depends(get_current_user)):

    deleted_task = delete_task(db, task_id, owner_id=user.id)

    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}