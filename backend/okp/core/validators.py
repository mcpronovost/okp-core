from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def okp_image_size_validator(value, max_mb=2):
    """
    Validate the image size.

    Args:
        value (File): The image file to validate.
        max_mb (int): The maximum size of the image in MB.

    Raises:
        ValidationError: If the image size is greater than the maximum size.
    """
    max_size = max_mb * 1024 * 1024  # 2MB
    if value.size > max_size:
        # pylint: disable=consider-using-f-string
        raise ValidationError(
            _(
                "File size must be no more than %sMB." % max_mb
            )
        )
