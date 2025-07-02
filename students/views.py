from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("students:student_list")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("students:login")
    return render(request, "student/login.html")


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "student/final_studentlist.html", {"students": students})


@login_required
def add_student(request):
    if request.method == "POST":
        st_name = request.POST["studentname"].lower()
        st_subject = request.POST["subject"].lower()
        st_marks = request.POST["marks"]
        exists = Student.objects.filter(subject=st_subject, name=st_name)
        if exists.exists():
            exists.update(score=int(st_marks))
            messages.success(
                request,
                "Already student existed with subject updated the marks successfully",
            )
        else:
            Student.objects.create(
                name=st_name.lower(), subject=st_subject.lower(), score=int(st_marks)
            )
            messages.success(request, "New student added successfully")
    return redirect("students:student_list")


@login_required
def edit_student(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        name = request.POST.get("name").lower()
        subject = request.POST.get("subject").lower()
        mark = request.POST.get("mark")
        student = Student.objects.get(id=student_id)
        student.name = name
        student.subject = subject
        student.score = mark
        student.save()
        return JsonResponse(
            {"status": "success", "message": "student data updated successfully"}
        )

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, "student deleted successfully")
    return redirect("students:student_list")


@login_required
def logout_view(request):
    logout(request)
    return redirect("students:login")
