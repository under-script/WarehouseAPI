from django.urls import path
from api import views

urlpatterns = [
    path('get_result/', views.snippet_list),
]