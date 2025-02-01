# OKP Authentication

A Django-based authentication system that extends Django's built-in authentication with custom functionality.

## Features

- Custom User Model with extended profile fields
- Token-based authentication using Django REST Knox
- Custom Group model with visibility control
- Multi-language support (English/French)
- Browser data tracking for authentication tokens
- Auto-generated user fields (name, abbreviation, slug)

## Models

### OkpUser
Extends Django's AbstractUser with additional fields:

- `email`: User's email address
- `middle_name`: Optional middle name
- `name`: Auto-generated or custom public display name
- `abbr`: 4-character abbreviation
- `slug`: URL-friendly username
- `avatar`: Profile picture (max 200x200)
- `cover`: Cover image (max 1024x256)
- `created_at`/`updated_at`: Timestamp fields

### OkpGroup
Custom group model replacing Django's default Group:

- `name`: Group name
- `permissions`: Group permissions
- `is_visible`: Controls group visibility
- Custom manager with `visible()` method

### OkpAuthToken
Extends Knox's AbstractAuthToken:

- Stores browser data (User Agent, Platform, Mobile status)
- Auto-expiry functionality
- Token limit per user

## API Endpoints

### Authentication Routes

```python
urlpatterns = [
    path("login/", OkpAuthLoginView.as_view()),
    path("logout/", OkpAuthLogoutView.as_view()),
    path("logoutall/", OkpAuthLogoutAllView.as_view()),
]
```

### Views

#### OkpAuthLoginView
- Endpoint: `POST /api/v1/auth/login/`
- Handles user authentication
- Returns token and user data
- Collects browser information
- Manages token limits per user

#### OkpAuthLogoutView
- Endpoint: `POST /api/v1/auth/logout/`
- Invalidates current session token

#### OkpAuthLogoutAllView
- Endpoint: `POST /api/v1/auth/logoutall/`
- Invalidates all user tokens
- Requires authentication

## Management Commands

### clean_expired_tokens
Removes expired authentication tokens from the database:

```bash
python manage.py clean_expired_tokens
```

## Configuration

### Settings

```python
AUTH_USER_MODEL = "okp_auth.OkpUser"
REST_KNOX = {
    "TOKEN_LIMIT_PER_USER": 2,
    "USER_SERIALIZER": "knox.serializers.UserSerializer",
    "AUTH_HEADER_PREFIX": "okp",
    "TOKEN_MODEL": "okp_auth.OkpAuthToken",
}
```

## Usage Example

### Frontend Authentication

```javascript
// Login
axios.post("http://localhost:8000/api/v1/auth/login/", {
    username: "username",
    password: "password"
})
// Authenticated Request
axios.get("http://localhost:8000/api/v1/.../", {
    headers: {
        "Authorization": "okp ${token}"
    }
})
// Logout
axios.post("http://localhost:8000/api/v1/auth/logout/", null, {
    headers: {
        "Authorization": "okp ${token}"
    }
})
```


## Admin Interface

The app provides custom admin interfaces for:
- User management
- Group management
- Token management

Admin models include:
- `OkpUserAdmin`: Extended user management
- `OkpGroupAdmin`: Group management with visibility control
- `OkpAuthTokenAdmin`: Read-only token management with browser data display

## Internationalization

The app supports multiple languages through Django's translation system:
- English (default)
- French

Translation files are located in `locale/{lang}/LC_MESSAGES/django.po`
