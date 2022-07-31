from django.urls import path

from . import views

urlpatterns = [
  path('', views.get_tasks, name='tasks'),
  path('details/<int:id>', views.task_details, name="task-details")
]
