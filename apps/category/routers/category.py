from typing import List

from fastapi import APIRouter, Depends

from apps import adapters
from apps.category.models import Category
from apps.category.schema import FastCategories

router = APIRouter()

@router.get("/")
def get_categories(categories: List[Category] = Depends(adapters.retrieve_categories),) -> FastCategories:
    return FastCategories.from_qs(categories)
