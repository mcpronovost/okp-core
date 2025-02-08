# okp

Core project.

## 🌟 Features

OKP is a modular Django-based platform with the following main components:

### Apps

- 🔨 **Core**: Core functionality and shared utilities
- 🔨 **API**: RESTful API interface
- ✅ **Authentication**: User authentication and authorization
- 📌 **Blog**: _Optional_ blogging functionality
- 📌 **Courrier**: _Optional_ private messaging system
- 📌 **Forum**: _Optional_ discussion board

## 🛠️ Technology Stack

### Backend

- **[Django](https://www.djangoproject.com/)** (5.1.5): Web framework for robust backend development
- **[Django CORS Headers](https://pypi.org/project/django-cors-headers/)**: For handling server headers required for Cross-Origin Resource Sharing
- **[Django REST Framework](https://pypi.org/project/djangorestframework/)**: For RESTful API development
- **[Django REST Knox](https://pypi.org/project/django-rest-knox/)**: For Django REST Framework multi-token authentication
- **[DRF Spectacular](https://pypi.org/project/drf-spectacular/)**: For Django REST Framework sane and flexible OpenAPI 3 schema generation
- **[Django Cleanup](https://pypi.org/project/django-cleanup/)**: For automatic cleaning of old images and files on FileField, ImageField and subclasses

### Frontend

- **[React](https://react.dev/blog/2024/12/05/react-19)** (19.0.0): For interactive UI components and dynamic features
- **[Axios](https://axios-http.com/docs/intro)**: For feature-rich HTTP client that supports promises and interceptors

## 🌐 Internationalization

The platform supports multiple languages:

- English (default)
- French

## 🧪 Testing

Use `python devserver.py tests` to run all tests.

### Pytest

- Uses pytest for testing and coverage
- To execute test: `pytest`

### Pylint

- Uses of pylint to check code quality and enforce consistent style
- To execute test: `pylint --load-plugins pylint_django --django-settings-module=okp.settings backend/`

### Flake8

- Uses Flake8 for fast style checking and basic error detection
- To execute test: `flake8 backend/`

## 📖 Additional Resources

- [GitHub Repository](https://github.com/mcpronovost/okp-core)
- [Issue Tracker](https://github.com/mcpronovost/okp-core/issues)
- [Changelog](CHANGELOG.md)
