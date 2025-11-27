import anthropic
import os
from django.conf import settings

client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """
You are Applaude AI, an expert QA Engineer and Senior Software Architect. 
Your job is to analyze codebases for:
1. UX & Design inconsistencies (Accessibility, Responsiveness, Standards).
2. Bugs & Logic Errors (Memory leaks, Unhandled exceptions, Security flaws).
3. Scalability & Performance (Database optimization, Code splitting, Caching).

Output your response strictly in JSON format matching this structure:
{
    "ux_issues": [{"title": "...", "description": "...", "severity": "warning|failed"}],
    "bugs": [{"title": "...", "description": "...", "severity": "warning|failed"}],
    "scalability": [{"title": "...", "description": "...", "severity": "passed|warning"}],
    "summary": "..."
}
"""

def analyze_codebase(file_contents):
    """
    file_contents: str - Concatenated string of key files from the repo.
    """
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4000,
            temperature=0,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Here is the codebase content:\n\n{file_contents}\n\nAnalyze it strictly according to the system prompt."
                        }
                    ]
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"AI Agent Error: {e}")
        return None
