from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.CreateStudentView.as_view(), name='create'),
    path('<int:pk>/edit/', views.UpdateStudentView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteStudentView.as_view(), name='delete'),
]
