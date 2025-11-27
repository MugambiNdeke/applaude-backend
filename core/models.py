from django.db import models
from django.conf import settings

class TestRun(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    repository_id = models.CharField(max_length=100) # GitHub Repo ID or Full Name
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    progress = models.IntegerField(default=0)
    result_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
