# routers/file_routes.py
from django.urls import path
from logic.handlers import file_handler  # Import your view function or class

urlpatterns = [
    path('upload/', file_handler.upload_file, name='upload_file'),  # Route for file upload
]
