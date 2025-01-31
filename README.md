# okp
Core project.

## 🌟 Features

### Apps
- `OKP Core`: Core app
- `Auth`: Authentication app
- `Blog`: Blog app
- `Courrier`: Private message app
- `Forum`: Forum app
- `API`: API app

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

## 🧪 Testing

### Pylint
- Uses of pylint to check code quality and enforce consistent style
- To execute test: `pylint --load-plugins pylint_django --django-settings-module=okp.settings backend/`

### Flake8
- Uses Flake8 for fast style checking and basic error detection
- To execute test: `flake8 backend/`
