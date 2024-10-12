from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_size(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise ValidationError(
            _('Image file too large ( > 2MB )')
        )