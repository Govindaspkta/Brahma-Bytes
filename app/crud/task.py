from sqlalchemy.orm import Session
from app.models.task import Task

def get_tasks(db, owner_id):
    return db.query(Task).filter_by(owner_id=owner_id).all()


def get_task(db, task_id, owner_id):
    return db.query(Task).filter_by(id=task_id, owner_id=owner_id).first()

#create task
def create_task(db, task, owner_id):
    new_task = Task(**task.dict(), owner_id=owner_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

#update task
def update_task(db, task_id, task, owner_id):
    db_task = get_task(db, task_id, owner_id)
    if not db_task:
        return None

    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

#delete task
def delete_task(db, task_id, owner_id):
    db_task = get_task(db, task_id, owner_id)
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return db_task