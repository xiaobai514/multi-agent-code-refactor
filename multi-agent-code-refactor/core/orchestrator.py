from agents.analyzer import analyze_code
from agents.refactor import refactor_code
from agents.tester import generate_tests
from agents.reviewer import review_code

def run_pipeline(repo_path):
    print("[System] Starting pipeline...")

    issues = analyze_code(repo_path)
    code = refactor_code(repo_path, issues)
    tests = generate_tests(code)
    result = review_code(code, tests)

    print("[System] Pipeline finished")
    print(result)
