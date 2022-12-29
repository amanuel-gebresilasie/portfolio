from django.shortcuts import render,HttpResponse
from .models import Projects

def home(request):
    all_projects = Projects.objects.all()
    content = {
            "projects": all_projects
            }
    return render(request,'portfolio/index.html',content)

def a(r):
    return HttpResponse("djanflgo http response")
