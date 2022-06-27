from django.urls import path, include

urlpatterns = [
    path('', include('calorie_app.urls')),
]
