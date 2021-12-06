from django.urls import path
from . import views
app_name = "adds"
urlpatterns=[
   path("tasks/",views.greets,name="greet"),
   path("add1/",views.add,name="add"),
]
