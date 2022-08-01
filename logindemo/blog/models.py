from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1024, null=False, blank=False)
    tags = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title
