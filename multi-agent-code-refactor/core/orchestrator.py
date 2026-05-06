from agents.analyzer import analyze_code
from agents.refactor import refactor_code
from agents.tester import generate_tests
from agents.reviewer import review_code

from tools.github_integration import GitHubClient

def run_pipeline(repo_path):
    print("[System] Starting pipeline...")

    issues = analyze_code(repo_path)
    code = refactor_code(repo_path, issues)
    tests = generate_tests(code)
    result = review_code(code, tests)

    github = GitHubClient("yourname/multi-agent-code-refactor")

    branch = github.create_branch()
    github.commit_changes()
    github.create_pull_request(branch)

    print("[System] Pipeline finished")
    print(result)
