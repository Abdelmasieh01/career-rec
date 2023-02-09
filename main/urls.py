from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificates/', views.certificate_list, name='certificates'),
    path('acheivements/', views.acheivement_list, name='acheivements'),
    path('workshops/', views.workshop_list, name='workshops'),
    path('visits/', views.visit_list, name='visits'),
    path('medicals/', views.medical_list, name='medicals'),
]