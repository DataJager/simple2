from django.urls import path

from . import views

app_name = 'listing'
urlpatterns = [
    path('<int:listing_id>/', views.detail, name='detail'),
    ]
