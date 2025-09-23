from django.urls import path
from . import views
urlpatterns = [
    path('feature1/', views.feature1_page, name='feature 1_page'),
]