import pytest
from django.db import models
from okp.core.utils import get_abbr, get_slug


class TestGetAbbr:
    """Tests for get_abbr function"""

    def test_empty_string(self):
        """Test empty string returns empty string"""
        assert get_abbr("") == ""
        assert get_abbr("   ") == "   "

    def test_single_word(self):
        """Test single word returns first letter capitalized"""
        assert get_abbr("test") == "T"
        assert get_abbr("Python") == "P"

    def test_two_words(self):
        """Test two words returns first letter of each word"""
        assert get_abbr("hello world") == "HW"
        assert get_abbr("Python Developer") == "PD"

    def test_three_words(self):
        """Test three words returns first letter of each word"""
        assert get_abbr("hello beautiful world") == "HBW"
        assert get_abbr("Python Web Developer") == "PWD"

    def test_more_than_three_words(self):
        """Test more than three words respects max_length"""
        assert get_abbr("one two three four") == "OTF"
        assert get_abbr("a b c d e f") == "ABF"

    def test_custom_max_length(self):
        """Test custom max_length parameter"""
        assert get_abbr("one two three four", max_length=2) == "OF"
        assert get_abbr("one two three four", max_length=4) == "OTTF"
        assert get_abbr("a b c d e f", max_length=5) == "ABCDF"

    def test_case_insensitive(self):
        """Test input case doesn't affect output"""
        assert get_abbr("hello WORLD") == "HW"
        assert get_abbr("PYTHON developer") == "PD"


class MockQuerySet:
    def __init__(self, existing_slugs):
        self.existing_slugs = existing_slugs
        self.excluded_id = None

    def filter(self, **kwargs):
        self.filtered_slugs = [slug for slug in self.existing_slugs if kwargs["slug"] == slug]
        return self

    def exclude(self, id=None):
        self.excluded_id = id
        return self

    def exists(self):
        return bool(self.filtered_slugs)


class MockModel:
    objects = None

    def __init__(self, existing_slugs):
        self.objects = MockQuerySet(existing_slugs)


class MockInstance:
    def __init__(self, id=1):
        self.id = id


class TestGetSlug:
    """Tests for get_slug function"""

    def test_simple_slug(self):
        """Test basic slug generation without conflicts"""
        model = MockModel([])
        instance = MockInstance()
        assert get_slug("Hello World", instance, model) == "hello-world"

    def test_slug_with_special_characters(self):
        """Test slug generation with special characters"""
        model = MockModel([])
        instance = MockInstance()
        assert get_slug("Hello & World!", instance, model) == "hello-world"

    def test_slug_with_conflicts(self):
        """Test slug generation with existing conflicts"""
        model = MockModel(["hello-world", "hello-world-1"])
        instance = MockInstance()
        assert get_slug("Hello World", instance, model) == "hello-world-2"

    def test_slug_with_multiple_conflicts(self):
        """Test slug generation with multiple existing conflicts"""
        model = MockModel(["test", "test-1", "test-2"])
        instance = MockInstance()
        assert get_slug("Test", instance, model) == "test-3"

    def test_slug_for_existing_instance(self):
        """Test slug generation for existing instance"""
        model = MockModel(["hello-world"])
        instance = MockInstance(id=1)
        assert get_slug("Hello World", instance, model) == "hello-world-1"

    def test_unicode_characters(self):
        """Test slug generation with unicode characters"""
        model = MockModel([])
        instance = MockInstance()
        assert get_slug("Héllö Wörld", instance, model) == "hello-world"