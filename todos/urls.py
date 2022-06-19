from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name ='home'),
    path("<int:pk>",views.update,name='update'),
    path("delete/<int:pk>",views.delete_todo,name='delete'),
]