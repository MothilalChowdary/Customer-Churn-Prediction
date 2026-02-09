from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_view, name='input'),    
    path('output/', views.output_view, name='output') 
]
