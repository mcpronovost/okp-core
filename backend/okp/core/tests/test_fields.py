# pylint: disable=attribute-defined-outside-init,redefined-outer-name
import io
import pytest
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from okp.core.fields import OkpImageField


class ImageTestModel(models.Model):
    """Test model for OkpImageField"""
    image = OkpImageField(max_width=100, max_height=100, upload_to="test/")

    class Meta:
        app_label = "core"
        managed = False


@pytest.fixture
def create_test_image():
    def _create_test_image(width=200, height=150, mode="RGB"):
        image = Image.new(mode, (width, height), color="red")
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        return SimpleUploadedFile(
            name="test.png",
            content=buffer.read(),
            content_type="image/png"
        )
    return _create_test_image


@pytest.mark.django_db
class TestOkpImageField:
    def test_resize_and_crop(self, create_test_image):
        # Create a test instance with an ID
        instance = ImageTestModel()
        instance.id = 1

        # Attach a test image
        test_file = create_test_image(width=200, height=150)
        instance.image = test_file

        # Call pre_save directly
        field = ImageTestModel._meta.get_field("image")
        field.pre_save(instance, add=True)

        # Open the processed image and check dimensions
        processed_image = Image.open(instance.image)
        assert processed_image.size == (100, 100)
        assert processed_image.mode == "RGBA"

    def test_rgba_conversion(self, create_test_image):
        instance = ImageTestModel()
        instance.id = 1

        # Create grayscale test image
        test_file = create_test_image(width=100, height=100, mode="L")
        instance.image = test_file

        # Process the image
        field = ImageTestModel._meta.get_field("image")
        field.pre_save(instance, add=True)

        # Check if converted to RGBA
        processed_image = Image.open(instance.image)
        assert processed_image.mode == "RGBA"

    def test_filename_format(self, create_test_image):
        instance = ImageTestModel()
        instance.id = 1

        test_file = create_test_image()
        instance.image = test_file

        field = ImageTestModel._meta.get_field("image")
        field.pre_save(instance, add=True)

        # Check if filename follows the expected format
        filename = instance.image.name
        assert filename.startswith("test/")
        filename_without_path = filename.split(
            "/")[-1]  # Get just the filename part
        assert filename_without_path.startswith(f"{instance.id}-")
        assert filename_without_path.endswith(".png")
        assert len(filename_without_path.split("-")
                   [1].split(".")[0]) == 8  # UUID length

    def test_no_dimensions_specified(self):
        # Test field initialization without max dimensions
        field = OkpImageField()
        assert field.max_width is None
        assert field.max_height is None
