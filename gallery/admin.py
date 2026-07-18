from django.contrib import admin
from .models import UploadedImage


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_filename', 'file_size_display', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'original_filename')
    readonly_fields = ('original_filename', 'file_size', 'uploaded_at')
