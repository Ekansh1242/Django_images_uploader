"""
Models for the gallery app.
"""
import os
import uuid
from django.db import models
from django.dispatch import receiver

from .validators import (
    validate_image_extension,
    validate_image_mime_type,
    validate_image_size,
)


def upload_to_gallery(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    unique_name = f'{uuid.uuid4().hex}{ext}'
    return os.path.join('gallery_images', unique_name)


class UploadedImage(models.Model):
    title = models.CharField(max_length=255, blank=True, help_text='Optional title/description for the image.')
    image = models.ImageField(
        upload_to=upload_to_gallery,
        validators=[validate_image_extension, validate_image_mime_type, validate_image_size],
        help_text='Accepted formats: JPG, JPEG, PNG, GIF. Max size: 10 MB.'
    )
    original_filename = models.CharField(max_length=255, blank=True)
    file_size = models.PositiveIntegerField(default=0, help_text='File size in bytes.')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Uploaded Image'
        verbose_name_plural = 'Uploaded Images'

    def __str__(self):
        return self.title or self.original_filename or f'Image #{self.pk}'

    def save(self, *args, **kwargs):
        if self.image and not self.original_filename:
            self.original_filename = self.image.name
        if self.image and hasattr(self.image, 'size'):
            self.file_size = self.image.size
        super().save(*args, **kwargs)

    @property
    def file_size_display(self):
        size = self.file_size
        if size < 1024 * 1024:
            return f'{size / 1024:.1f} KB'
        return f'{size / (1024 * 1024):.2f} MB'


@receiver(models.signals.post_delete, sender=UploadedImage)
def delete_image_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
