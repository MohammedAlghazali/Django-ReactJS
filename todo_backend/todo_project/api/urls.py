from django.urls import path
from .views import TodoList, TodoDetails

urlpatterns = [
    path('todos/', TodoList.as_view()),
    path('todos/<int:id>/', TodoDetails.as_view()),
]
