from django.urls import include, path


urlpatterns = [
    path('v1/', include('apps.example_app.api.v1.urls'))
]
