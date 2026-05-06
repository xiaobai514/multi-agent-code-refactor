import time
import random

class GitHubClient:

    def __init__(self, repo_name):
        self.repo_name = repo_name

    def create_branch(self):
        branch = f"refactor/auto-{random.randint(1000,9999)}"
        print(f"[GitHub] Created branch: {branch}")
        return branch

    def commit_changes(self):
        print("[GitHub] Committing changes...")
        time.sleep(1)
        print("[GitHub] Commit successful")

    def create_pull_request(self, branch):
        pr_id = random.randint(10, 100)
        print(f"[GitHub] Pull Request created: #{pr_id}")
        print(f"[GitHub] Branch: {branch}")
        print(f"[GitHub] URL: https://github.com/{self.repo_name}/pull/{pr_id}")
