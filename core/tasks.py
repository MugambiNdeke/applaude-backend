from celery import shared_task
from .models import TestRun
from .agent import analyze_codebase
from .github_client import fetch_repo_content
import json

@shared_task
def run_ai_analysis(test_run_id, github_token):
    test_run = TestRun.objects.get(id=test_run_id)
    test_run.status = 'RUNNING'
    test_run.progress = 10
    test_run.save()

    try:
        # 1. Fetch Code from GitHub (Helper function to be implemented in github_client.py)
        # It should return a large string of relevant code files (.tsx, .ts, .py, etc)
        code_content = fetch_repo_content(test_run.repository.full_name, github_token)
        test_run.progress = 40
        test_run.save()

        # 2. Analyze with AI
        ai_response_json = analyze_codebase(code_content)
        
        if ai_response_json:
            test_run.result_json = json.loads(ai_response_json)
            test_run.status = 'COMPLETED'
            test_run.progress = 100
        else:
            test_run.status = 'FAILED'
            
    except Exception as e:
        print(e)
        test_run.status = 'FAILED'
    
    test_run.save()
