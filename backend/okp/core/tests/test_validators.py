import pytest
from django.core.exceptions import ValidationError
from okp.core.validators import okp_image_size_validator


# pylint: disable=too-few-public-methods
class MockFile:
    def __init__(self, size):
        self.size = size


def test_okp_image_size_validator_valid_size():
    """Test that validator accepts files under the size limit"""
    # 1MB file
    mock_file = MockFile(1 * 1024 * 1024)

    # Should not raise any exception
    okp_image_size_validator(mock_file, max_mb=2)


def test_okp_image_size_validator_exact_size():
    """Test that validator accepts files exactly at the size limit"""
    # 2MB file
    mock_file = MockFile(2 * 1024 * 1024)

    # Should not raise any exception
    okp_image_size_validator(mock_file, max_mb=2)


def test_okp_image_size_validator_invalid_size():
    """Test that validator rejects files over the size limit"""
    # 3MB file
    mock_file = MockFile(3 * 1024 * 1024)

    with pytest.raises(ValidationError) as exc_info:
        okp_image_size_validator(mock_file, max_mb=2)

    assert "File size must be no more than 2MB" in str(exc_info.value)


def test_okp_image_size_validator_custom_max_size():
    """Test that validator works with custom max_mb parameter"""
    # 4MB file
    mock_file = MockFile(4 * 1024 * 1024)

    # Should not raise any exception with 5MB limit
    okp_image_size_validator(mock_file, max_mb=5)

    # Should raise exception with 3MB limit
    with pytest.raises(ValidationError) as exc_info:
        okp_image_size_validator(mock_file, max_mb=3)

    assert "File size must be no more than 3MB" in str(exc_info.value)
