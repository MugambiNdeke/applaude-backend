from django.db import models
from django.conf import settings

class Repository(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255) # e.g. "username/repo"
    private = models.BooleanField(default=False)
    github_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TestRun(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )
    
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Store the JSON result from AI
    result_json = models.JSONField(null=True, blank=True) 
    report_url = models.URLField(null=True, blank=True) # Google Doc link

    def __str__(self):
        return f"{self.repository.name} - {self.created_at}"
