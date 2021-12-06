from django.urls import path
from . import views

urlpatterns=[
   path("newyear1/",views.greet,name="greet"),
]
