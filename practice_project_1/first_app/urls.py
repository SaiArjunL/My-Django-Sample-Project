from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
        path('users/', views.users, name = 'users'),
]
