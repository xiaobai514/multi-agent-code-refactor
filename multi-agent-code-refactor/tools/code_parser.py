import os

def scan_files(repo_path):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))
    return files


def analyze_file(file_path):
    issues = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

        if len(code) > 1000:
            issues.append("long_function")

        if "TODO" in code:
            issues.append("todo_found")

        if "==" in code and "if" not in code:
            issues.append("potential_bug")

    return issues


def analyze_repo(repo_path):
    files = scan_files(repo_path)
    all_issues = {}

    for f in files:
        issues = analyze_file(f)
        if issues:
            all_issues[f] = issues

    return {
        "total_files": len(files),
        "issue_files": len(all_issues),
        "details": all_issues
    }
