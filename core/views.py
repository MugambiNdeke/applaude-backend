from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Repository, TestRun
from .serializers import RepositorySerializer, TestRunSerializer
from .tasks import run_ai_analysis

class TestRunViewSet(viewsets.ModelViewSet):
    serializer_class = TestRunSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TestRun.objects.filter(repository__user=self.request.user)

    @action(detail=False, methods=['post'])
    def start(self, request):
        repo_id = request.data.get('repository_id')
        repo = Repository.objects.get(id=repo_id, user=request.user)
        
        # Check payment status here if needed
        
        test_run = TestRun.objects.create(repository=repo)
        
        # Get user's GitHub token (stored in session or user model)
        # For MVP using a passed token or system token
        github_token = request.data.get('github_token') 
        
        run_ai_analysis.delay(test_run.id, github_token)
        
        return Response(TestRunSerializer(test_run).data, status=status.HTTP_201_CREATED)
