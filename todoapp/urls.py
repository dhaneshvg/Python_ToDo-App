from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('edit/<int:updateid>/', views.update, name='update')
]
