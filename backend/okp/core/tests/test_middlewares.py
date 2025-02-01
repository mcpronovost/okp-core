# pylint: disable=too-few-public-methods,redefined-outer-name
from unittest.mock import MagicMock, patch
import pytest
from django.contrib import admin
from django.test import RequestFactory

from okp.core.middlewares import OkpAdminOrderMiddleware


@pytest.fixture
def middleware():
    return OkpAdminOrderMiddleware(get_response=MagicMock())


@pytest.fixture
def request_factory():
    return RequestFactory()


def test_non_admin_path(middleware, request_factory):
    request = request_factory.get("/some-other-path/")
    middleware(request)

    # Verify get_response was called
    middleware.get_response.assert_called_once_with(request)


def test_admin_path(middleware, request_factory):
    request = request_factory.get("/admin/")

    with patch("okp.core.middlewares.resolve") as mock_resolve:
        mock_resolve.return_value.app_name = "admin"
        middleware(request)

        # Verify resolve was called with correct path
        mock_resolve.assert_called_once_with("/admin/")
        # Verify get_response was called
        middleware.get_response.assert_called_once_with(request)


def test_sort_admin_menu(middleware):
    # Mock settings with specific ordering
    middleware.app_order = {
        "auth": 1,
        "sites": 2
    }
    middleware.model_order = {
        "auth": {
            "Group": 1,
            "User": 2
        }
    }

    # Create test data with deliberately unsorted models
    original_app_list = [
        {
            "app_label": "auth",
            "models": [
                {"object_name": "User"},
                {"object_name": "Group"}
            ]
        },
        {
            "app_label": "sites",
            "models": [
                {"object_name": "Site"}
            ]
        }
    ]

    mock_request = MagicMock()

    with patch.object(
        admin.site, "get_app_list",
        return_value=original_app_list
    ):
        # pylint: disable=protected-access
        middleware._sort_admin_menu()

        # Get the sorted list
        sorted_list = admin.site.get_app_list(mock_request)

        # Verify app ordering
        assert [app["app_label"] for app in sorted_list] == ["auth", "sites"]

        # Verify model ordering within the auth app
        auth_app = next(
            app for app in sorted_list if app["app_label"] == "auth")
        assert [model["object_name"]
                for model in auth_app["models"]] == ["Group", "User"]

        # Verify sites app models remained unchanged
        sites_app = next(
            app for app in sorted_list if app["app_label"] == "sites")
        assert [model["object_name"]
                for model in sites_app["models"]] == ["Site"]


def test_exception_handling(middleware, request_factory):
    """Test that middleware handles exceptions gracefully"""
    request = request_factory.get("/admin/")

    with patch(
        "okp.core.middlewares.resolve",
        side_effect=Exception("Test error")
    ):
        # Should not raise an exception
        middleware(request)

        # Verify get_response was still called
        middleware.get_response.assert_called_once_with(request)
