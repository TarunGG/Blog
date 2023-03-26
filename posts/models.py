from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200,null=False)
    description = models.TextField()
    created_at = models.DateField(editable=False)
    last_updated = models.DateField()
    username = models.CharField(max_length=100,default=None) 