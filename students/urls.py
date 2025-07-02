from django.urls import path
from .views import *

app_name = "students"

urlpatterns = [
    path("", login_view, name="login"),
    path("studentlist", student_list, name="student_list"),
    path("addstudent", add_student, name="add_student"),
    path("editstudent", edit_student, name="edit_student"),
    path("deletestudent/<id>", delete_student, name="delete_student"),
    path("logout", logout_view, name="logout_view"),
]
