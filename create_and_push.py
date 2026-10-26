import os
import subprocess
from pathlib import Path
import sys

# Use current working directory
project_dir = Path.cwd()
os.chdir(project_dir)

def run_cmd(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
    return result.returncode

print("==================================================")
print(" GitHub Automated Repo Creator & Pusher")
print("==================================================")

# 1. Initialize local Git if it doesn't exist
if not (project_dir / ".git").exists():
    print("[*] Initializing local Git repository...")
    run_cmd("git init")
    run_cmd("git branch -M main")

# 2. Stage all current files
run_cmd("git add .")

# 3. Check for changes to commit
status_check = subprocess.run("git diff --cached --quiet", shell=True)
if status_check.returncode != 0:
    commit_msg = input("\nEnter commit message: ").strip()
    if not commit_msg:
        commit_msg = "Initial commit"
    run_cmd(f'git commit -m "{commit_msg}"')
else:
    print("[!] No new changes to commit, proceeding to remote creation...")

# 4. Prompt for GitHub repository details
repo_name = input("\nEnter name for the new GitHub repository: ").strip()
if not repo_name:
    repo_name = project_dir.name

visibility = input("Repository visibility ([p]rivate / [pub]lic): ").strip().lower()
vis_flag = "--private" if visibility.startswith('p') and not visibility.startswith('pub') else "--public"

# 5. Create remote repo via GitHub CLI and push
print(f"\n[*] Creating GitHub repository '{repo_name}' ({vis_flag[2:]})...")
create_code = run_cmd(f"gh repo create {repo_name} {vis_flag} --source=. --remote=origin --push")

if create_code == 0:
    print(f"\n[+] Success! Repository '{repo_name}' created and pushed to GitHub.")
else:
    print("\n[-] Creation failed. Ensure you are logged into GitHub CLI via 'gh auth login'.")