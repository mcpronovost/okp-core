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

- `username`: Unique identifier (letters, numbers, underscores, hyphens)
- `email`: User's email address
- `first_name`: User's first name
- `middle_name`: Optional middle name
- `last_name`: User's last name
- `name`: Auto-generated or custom public display name
- `abbr`: 4-character abbreviation
- `slug`: URL-friendly username
- `avatar`: Profile picture (max 200x200)
- `cover`: Cover image (max 1024x256)
- `created_at`/`updated_at`: Timestamp fields

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
    path("register/", OkpAuthRegisterView.as_view()),
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

#### OkpAuthRegisterView
- Endpoint: `POST /api/v1/auth/register/`
- Creates new user accounts
- Validates username, email, and password
- Auto-generates user fields
- Returns token and user data
- Required fields:
  - username (unique, alphanumeric + _-)
  - email (unique)
  - password (with validation)
  - password2 (confirmation)
  - terms_accepted (boolean)
- Optional fields:
  - first_name
  - last_name

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
// Register
axios.post("http://localhost:8000/api/v1/auth/register/", {
    username: "username",
    email: "user@example.com",
    password: "securepassword",
    password2: "securepassword",
    first_name: "John",
    last_name: "Doe",
    terms_accepted: true
})
```


## Admin Interface

The app provides custom admin interfaces for:
- User management with extended profile fields
- Token management with browser data display

Admin models include:
- `OkpUserAdmin`: Extended user management with custom fieldsets
- `OkpAuthTokenAdmin`: Read-only token management with browser data display

## Internationalization

The app supports multiple languages through Django's translation system:
- English (default)
- French

Translation files are located in `locale/{lang}/LC_MESSAGES/django.po`
