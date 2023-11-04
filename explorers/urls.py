from django.urls import path
from explorers import views

urlpatterns = [
    path('explorers/', views.ExplorerList.as_view()),
    path('explorers/<int:pk>/', views.ExplorerDetail.as_view()),
]