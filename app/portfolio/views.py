from django.shortcuts import render,HttpResponse
from .models import Projects

def home(request):
    all_projects = Projects.objects.all()
    content = {
            "projects": all_projects
            }
    return render(request,'portfolio/index.html',content)


def e404(request,err):
    return render(request,"404.html")
def e500(re,er):
    return render(re,"500.html")
