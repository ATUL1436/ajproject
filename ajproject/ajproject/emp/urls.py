from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home1/",emp_home),
    path("add_emp/",add_emp),
    path("delete_emp/<int:emp_id>",delete_emp),
    path("update_emp/<int:emp_id>",update_emp),
    path("do_update_emp/<int:emp_id>",do_update_emp),
    
]
