from django.contrib import admin
from main.models import File


# Register your models here.


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'processed',)
    list_filter = ('uploaded_at', 'processed',)
