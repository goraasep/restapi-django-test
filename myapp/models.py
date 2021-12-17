from django.db import models

# Create your models here.
class AppContent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)