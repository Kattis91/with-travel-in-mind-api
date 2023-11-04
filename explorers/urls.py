from django.urls import path
from explorers import views

urlpatterns = [
    path('explorers/', views.ExplorerList.as_view()),
]