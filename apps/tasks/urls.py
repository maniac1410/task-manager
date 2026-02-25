from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='tasks'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:pk>',views.edit_task, name='edit_task'),
    path('delete-task.html/<int:pk>', views.delete_task, name='delete_task')

]
