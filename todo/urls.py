from django.urls import path

from .views import *

app_name = "main_todo"

urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('<int:pk>/update', UpdateTaskView.as_view(), name="update-task"),
    path('<int:pk>/delete', DeleteTaskView.as_view(), name="delete-task")
]