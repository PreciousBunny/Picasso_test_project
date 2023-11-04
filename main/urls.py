from django.urls import path

from main.views import FileUploadAPIView, FileListAPIView
from main.apps import MainConfig


app_name = MainConfig.name


urlpatterns = [
    path('upload', FileUploadAPIView.as_view(), name='file_upload'),
    path('files', FileListAPIView.as_view(), name='file_list'),
]
