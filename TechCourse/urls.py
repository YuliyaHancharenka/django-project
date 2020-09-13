from django.urls import path
from TechCourse import views

app_name = "TechCourse"

urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('', views.course, name='home-page'),
    path('<int:course_id>/is_interesting/', views.is_interesting, name='is_interesting'),
]