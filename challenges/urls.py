from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('<int:month>', views.number),
    path('<str:month>', views.show_task, name = 'month-challenges'),
    
]