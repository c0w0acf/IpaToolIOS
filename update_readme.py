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

readme_content = """# IpaToolIOS

A native cross-compiled port of **`ipatool`** optimized for iOS (`arm64`). This project allows you to search, manage, and download app packages directly from Apple's App Store using your own device.

---

## 🚀 Features
- **Pure iOS Execution:** Run App Store queries and binary retrieval natively on your iPhone.
- **Automated Cloud Builds:** Compiles directly via GitHub Actions using native macOS runners with CGO support.
- **Keychain Integration:** Securely saves session credentials using native iOS keychain structures.

---

## 🛠️ Building the Binary (GitHub Actions)
Since `ipatool` requires external linking (CGO) for iOS keychain support, builds are automated via GitHub Actions:
1. Go to the **Actions** tab in your GitHub repository.
2. Select the **Build ipatool for iOS** workflow and click **Run workflow**.
3. Once completed, download the `ipatool-ios` artifact zip from the workflow summary page.

---

## 📱 Running Natively on iPhone

To execute the binary directly on your iPhone (tested with **Feather** and sideloaded terminal wrappers):

1. **Transfer the Binary:** 
   Extract the `ipatool-ios` executable and drop it into your local storage using the iOS **Files** app (e.g., inside **On My iPhone > a-Shell** or your preferred terminal app's local document directory).
   
2. **Open Your Terminal App:**
   Launch your terminal wrapper (such as **`a-Shell`**, sideloaded via your paid developer certificate).

3. **Grant Permissions & Execute:**
   Run the following commands inside your terminal environment:
   ```bash
   chmod +x ipatool-ios
   ./ipatool-ios --help