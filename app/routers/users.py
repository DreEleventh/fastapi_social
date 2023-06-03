from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, utils
from ..databaseConn import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash a given password
    hash_password = utils.hash_passcode(user.password)
    user.password = hash_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id '{id}' does not exist")

    return user


@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_user_password(id: int, change_password: schemas.UserUpdate, db: Session = Depends(get_db)):

    updated_password = db.query(models.User).filter(models.User.id == id)

    update = updated_password.first()

    if not update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} does not exist.")
    else:
        hash_password = utils.hash_passcode(change_password.password)

        change_password.password = hash_password
        updated_password.password = change_password.password

        updated_password.update(change_password.dict(), synchronize_session=False)
        db.commit()

        return {"message": "Password updated successfully!"}

