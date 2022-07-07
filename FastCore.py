import os

from django.core.asgi import get_asgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

application = get_asgi_application()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apps.category.routers import test_router, category_router

fastapp = FastAPI()
fastapp.include_router(test_router, tags=["test"], prefix="/test")
fastapp.include_router(category_router, tags=["category"], prefix="/category")


if settings.MOUNT_DJANGO_APP:
    fastapp.mount("/django", application)
    fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")
