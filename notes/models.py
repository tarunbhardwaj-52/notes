from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
