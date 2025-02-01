# okp
Core project.

## 🌟 Features

OKP is a modular Django-based platform with the following main components:

### Apps
- 🔨 **[Core](docs/apps/core.md)**: Core functionality and shared utilities
- 🔨 **[API](docs/apps/api.md)**: RESTful API interface
- ✅ **[Authentication](docs/apps/auth.md)**: User authentication and authorization
- 📌 **[Blog](docs/apps/blog.md)**: *Optional* blogging functionality
- 📌 **[Courrier](docs/apps/courrier.md)**: *Optional* private messaging system
- 📌 **[Forum](docs/apps/forum.md)**: *Optional* discussion board


## 🛠️ Technology Stack

### Backend
- **Django** (5.1.5): Web framework for robust backend development
- **Django CORS Headers**: For handling server headers required for Cross-Origin Resource Sharing
- **Django REST Framework**: For RESTful API development
- **Django REST Knox**: For Django REST Framework multi-token authentication
- **DRF Spectacular**: For Django REST Framework sane and flexible OpenAPI 3 schema generation
- **Django Cleanup**: For automatic cleaning of old images and files on FileField, ImageField and subclasses

### Frontend
- **React** (19.0.0): For interactive UI components and dynamic features

## 🌐 Internationalization

The platform supports multiple languages:

- English (default)
- French

## 🧪 Testing

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
