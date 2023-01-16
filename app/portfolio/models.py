from django.db import models
from django.conf import settings

class Projects(models.Model):
    img = models.ImageField(upload_to="static/portfolio/media")
    view_link = models.TextField()
    github_link = models.TextField()
