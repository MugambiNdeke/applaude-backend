from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TestRun
from .serializers import TestRunSerializer
from .tasks import run_analysis_task

class TestRunViewSet(viewsets.ModelViewSet):
    serializer_class = TestRunSerializer
    
    def get_queryset(self):
        return TestRun.objects.filter(user=self.request.user).order_by('-created_at')

    @action(detail=False, methods=['post'])
    def start(self, request):
        repo_id = request.data.get('repository_id')
        
        # Verify Github Token exists
        if not request.user.github_access_token:
             return Response({"error": "GitHub not connected"}, status=400)

        test_run = TestRun.objects.create(
            user=request.user,
            repository_id=repo_id,
            status='PENDING'
        )
        
        # Dispatch Async Task
        run_analysis_task.delay(test_run.id, request.user.github_access_token)
        
        return Response({"id": test_run.id, "status": "PENDING"})
