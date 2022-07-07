from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def get_pruebas():

    return {"message": "Hello World"}
