import anthropic
from django.conf import settings
import json

def analyze_with_claude(file_data_str):
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    system_prompt = """
    You are Applaude AI, a Senior QA Engineer. Analyze the provided code for:
    1. UX/UI Issues (Accessibility, responsiveness)
    2. Bugs (Logic errors, security flaws, memory leaks)
    3. Scalability (Performance bottlenecks)
    
    Return ONLY JSON:
    {
        "ux_issues": [{"title": "...", "description": "...", "severity": "warning"}],
        "bugs": [{"title": "...", "description": "...", "severity": "failed"}],
        "scalability": [{"title": "...", "description": "...", "severity": "passed"}],
        "summary": "..."
    }
    """

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4000,
            temperature=0,
            system=system_prompt,
            messages=[
                {"role": "user", "content": f"Analyze this codebase:\n\n{file_data_str}"}
            ]
        )
        return json.loads(message.content[0].text)
    except Exception as e:
        print(f"AI Error: {e}")
        return None
