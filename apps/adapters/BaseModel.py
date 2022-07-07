from pydantic import BaseModel as _BaseModel
from django.db import models
from typing import List


class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.from_orm(inst) for inst in instances]