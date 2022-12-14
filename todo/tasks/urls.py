from django.urls import path

from . import views

urlpatterns = [
  path('', views.get_tasks, name='tasks'),
  path('details/<int:id>', views.task_details, name="task-details"),
  path('edit/<int:id>', views.edit_task, name="edit-task"),
  path('create', views.create_task, name="create-task"),
  path('delete/<int:id>', views.delete_task, name="delete-task"),
  path('status/<int:id>', views.change_status, name="change-status")
]
