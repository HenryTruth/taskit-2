from django.urls import path

from .views import TodosAPIView,TodosAPIDetailView

urlpatterns = [
    path('',TodosAPIView.as_view()),
    path('<int:id>/', TodosAPIDetailView.as_view()),
]