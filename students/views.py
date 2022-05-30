from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse

from students.forms import StudentForm
from students.models import GENDERS, Student

# Create your views here.


class IndexView(ListView):
    model = Student
    context_object_name = "students"


class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('students:index')


class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('students:index')


class DeleteStudentView(DeleteView):
    model = Student

    def get_success_url(self):
        return reverse('students:index')
