from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.example_app.api.v1.views import ExampleView
# from apps.example_app.api.v1.views import TranslationViewSet

# router = DefaultRouter()
# router.register(r'translations', TranslationViewSet, basename='translations')

urlpatterns = [
    # path('', include(router.urls)),  # Registers the translations API endpoints
    path('example-endpoint/', ExampleView.as_view(), name='example-endpoint'),
]
