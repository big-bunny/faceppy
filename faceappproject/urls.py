from django.urls import path
from faceapp import views
urlpatterns = [
    path('', views.recognize_faces, name='home'),
    path('api/recognize/', views.recognize_faces, name='recognize_faces'),
]
