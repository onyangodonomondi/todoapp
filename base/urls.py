from django.urls import path
from . import views
from . views import TaskList, TaskDetail , TaskCreate


urlpatterns = [
    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    
    ]