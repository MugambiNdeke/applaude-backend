from celery import shared_task
from .models import TestRun
from .agent import analyze_with_claude
from .github import fetch_repo_contents # Helper you will create

@shared_task
def run_analysis_task(test_run_id, github_token):
    test_run = TestRun.objects.get(id=test_run_id)
    test_run.status = 'RUNNING'
    test_run.progress = 10
    test_run.save()

    try:
        # 1. Fetch Code
        code_str = fetch_repo_contents(test_run.repository_id, github_token)
        test_run.progress = 40
        test_run.save()

        # 2. AI Analysis
        results = analyze_with_claude(code_str)
        
        if results:
            test_run.result_json = results
            test_run.status = 'COMPLETED'
            test_run.progress = 100
        else:
            test_run.status = 'FAILED'

    except Exception as e:
        print(e)
        test_run.status = 'FAILED'
    
    test_run.save()
