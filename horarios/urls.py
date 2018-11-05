from django.urls import path
from . import views

urlpatterns = [
    #/horarios/
    path('', views.horarios, name = "horarios"),

    #/horarios/colonia *por si quiero hacer una subview para cada horario* 
    #path('colonia', views.colonia, name = "colonia"),
]
