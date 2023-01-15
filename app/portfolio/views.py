from django.shortcuts import render,HttpResponse
from .models import Projects

def home(request):
    all_projects = Projects.objects.all()
    content = {
            "projects": all_projects
            }
    return render(request,'portfolio/index.html',content)


def error_404_view(request,err):
    return HttpResponse("PAGE NOT FOUND !")
