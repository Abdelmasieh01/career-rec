from django.shortcuts import render
from .models import Cretificate, Acheivement, Workshop, Visit, Medical

def index(request):
    return render(request, 'main/index.html',)

def certificate_list(request):
    certificates = Cretificate.objects.all()
    text = 'شهاداتي'
    return render(request, 'main/tables.html', {'text': text, 'items': certificates})

def acheivement_list(request):
    acheivements = Acheivement.objects.all()
    text = 'إنجازاتي'
    return render(request, 'main/tables.html', {'text': text, 'items': acheivements})

def workshop_list(request):
    workshops = Workshop.objects.all()
    text = 'ورش العمل'
    return render(request, 'main/tables.html', {'text': text, 'items': workshops})

def visit_list(request):
    visits = Visit.objects.all()
    text = 'الزيارات التبادلية'
    return render(request, 'main/tables.html', {'text': text, 'items': visits})

def medical_list(request):
    medicals = Medical.objects.all()
    text = 'الخطط العلاجية'
    return render(request, 'main/tables.html', {'text': text, 'items': medicals})


