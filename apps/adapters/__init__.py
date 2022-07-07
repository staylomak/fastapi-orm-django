from typing import Type, TypeVar

from django.db import models
from fastapi import HTTPException, Path

from apps.category.models import Category

ModelT = TypeVar("ModelT", bound=models.Model)

"""
def retrieve_object(model_class: Type[ModelT], id: int) -> ModelT:
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance

def retrieve_question(q_id: int = Path(..., description="get question from db")) -> Question:
    return retrieve_object(Question, q_id)

def retrieve_choice(c_id: int = Path(..., description="get choice from db")):
    return retrieve_object(Choice, c_id)

def retrieve_questions():
    return Question.objects.all()

def retrieve_choices():
    return Choice.objects.all()

def retrieve_prueba(id: int = Path(..., description="get prueba from db")):
    return retrieve_object(prueba, id)

def retrieve_pruebas():
    pruebas = prueba.objects.all()
    for x in pruebas:
        print(x)
        print("_"*50)
    return pruebas
"""
def retrieve_categories():
    return Category.objects.all()
