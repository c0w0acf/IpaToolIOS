import os
import subprocess
from pathlib import Path

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
print(" GitHub Automated Push Script")
print("==================================================")

# 1. Show current git status
run_cmd("git status")

# 2. Stage all changes
run_cmd("git add .")

# 3. Check if there are changes to commit
status_check = subprocess.run("git diff --cached --quiet", shell=True)
if status_check.returncode != 0:
    commit_msg = input("\nEnter commit message (press Enter for default): ").strip()
    if not commit_msg:
        commit_msg = "Update project files and documentation"
    run_cmd(f'git commit -m "{commit_msg}"')
else:
    print("[!] No new changes to commit, checking remote push...")

# 4. Push updates to GitHub
print("\n[*] Pushing changes to origin main...")
push_code = run_cmd("git push origin main")

if push_code == 0:
    print("\n[+] Successfully pushed updates to GitHub!")
else:
    print("\n[-] Push failed. Verify your authentication/network.")