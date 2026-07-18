"""
Custom validators for uploaded images.
"""
import os
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in settings.ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            f'Unsupported file extension "{ext}". '
            f'Allowed extensions are: {", ".join(settings.ALLOWED_IMAGE_EXTENSIONS)}.'
        )


def validate_image_mime_type(value):
    content_type = getattr(value.file, 'content_type', None)
    if content_type and content_type not in settings.ALLOWED_IMAGE_MIME_TYPES:
        raise ValidationError(
            f'Unsupported file type "{content_type}". '
            f'Only JPG, JPEG, PNG, and GIF images are allowed.'
        )


def validate_image_size(value):
    if value.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(
            f'File too large. Maximum allowed size is '
            f'{settings.MAX_UPLOAD_SIZE_MB} MB. '
            f'Your file is {value.size / (1024 * 1024):.2f} MB.'
        )
