from github import Github
import base64

def fetch_repo_contents(repo_full_name, access_token):
    """
    Fetches key code files from a private/public repo using the user's OAuth token.
    Returns a single concatenated string for the AI to analyze.
    """
    g = Github(access_token)
    try:
        repo = g.get_repo(repo_full_name)
        
        # extensions to analyze
        relevant_extensions = ('.js', '.jsx', '.ts', '.tsx', '.py', '.css', '.html')
        ignore_dirs = ('node_modules', 'dist', 'build', '.git', 'migrations', 'venv')
        
        all_code = []
        contents = repo.get_contents("")
        
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                if file_content.name not in ignore_dirs:
                    contents.extend(repo.get_contents(file_content.path))
            else:
                if file_content.name.endswith(relevant_extensions):
                    # Check size to prevent context window overflow (limit to ~50kb per file)
                    if file_content.size < 50000: 
                        try:
                            # Decode content
                            decoded = base64.b64decode(file_content.content).decode('utf-8')
                            all_code.append(f"--- FILE: {file_content.path} ---\n{decoded}\n")
                        except:
                            pass # Skip binary or unreadable files
                            
        return "\n".join(all_code)

    except Exception as e:
        print(f"GitHub Fetch Error: {e}")
        raise e
