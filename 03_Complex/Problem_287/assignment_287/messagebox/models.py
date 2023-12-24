from django.db import models

class MessageBox(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

