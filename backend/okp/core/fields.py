import io
from PIL import Image
from django.core.exceptions import ValidationError
from django.core.files import File
from django.db.models import ImageField
from django.utils.translation import gettext_lazy as _


def okpImageSizeValidator(value, max_mb=2):
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
        raise ValidationError(_("File size must be no more than %sMB." % max_mb))


class OkpImageField(ImageField):
    def __init__(self, max_width=None, max_height=None, *args, **kwargs):
        self.max_width = max_width
        self.max_height = max_height
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = getattr(model_instance, self.attname)
        if file and not file._committed:
            # Open image
            pil_image = Image.open(file)

            # Convert to RGB if necessary
            if pil_image.mode != "RGB":
                pil_image = pil_image.convert("RGB")

            # Calculate new dimensions maintaining aspect ratio
            if self.max_width or self.max_height:
                orig_width, orig_height = pil_image.size
                if self.max_width and orig_width > self.max_width:
                    width = self.max_width
                    height = int(
                        (float(orig_height) * float(width/orig_width)))
                else:
                    width = orig_width
                    height = orig_height

                if self.max_height and height > self.max_height:
                    height = self.max_height
                    width = int(
                        (float(orig_width) * float(height/orig_height)))

                if width != orig_width or height != orig_height:
                    pil_image = pil_image.resize(
                        (width, height), Image.Resampling.LANCZOS)

            # Save the image
            buffer = io.BytesIO()
            pil_image.save(buffer, format="JPEG", quality=85)
            buffer.seek(0)

            # Update the file
            new_file = File(buffer, name=file.name)
            setattr(model_instance, self.attname, new_file)

        return super().pre_save(model_instance, add)
