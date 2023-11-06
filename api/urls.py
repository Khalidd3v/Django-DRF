from django.urls import path
from . views  import *

urlpatterns = [
    path('home/', homepage, name="homepage"),
    path("v1/students_data/", get_students_data, name="students_data"),
    path('read/', readpage, name="read"),
    path('delete/', deletepage, name="delete"),
    path('update/', updatepage, name="update"),
    path('create/', createpage, name="create"),
]