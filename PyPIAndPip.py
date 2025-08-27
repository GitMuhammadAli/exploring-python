"""
===========================================
 📦 PYPI & PIP QUICK REFERENCE (pypi_pip.py)
===========================================

PyPI = Python Package Index (like npm registry in JS)
pip  = Package installer for Python
"""

import subprocess
import sys

# ---------------------------
# 1. Check pip version
# ---------------------------
# Run in terminal: pip --version
print("Pip version check (terminal): pip --version")

# ---------------------------
# 2. Installing a package
# ---------------------------
# Run in terminal:
# pip install requests
print("Install package: pip install requests")

# ---------------------------
# 3. Import & use installed package
# ---------------------------
try:
    import requests
    response = requests.get("https://httpbin.org/get")
    print("Requests installed and working:", response.status_code)
except ImportError:
    print("Requests not installed. Run: pip install requests")

# ---------------------------
# 4. Uninstalling a package
# ---------------------------
# Run in terminal:
# pip uninstall requests -y
print("Uninstall package: pip uninstall requests")

# ---------------------------
# 5. List all installed packages
# ---------------------------
# Run in terminal:
# pip list
print("List installed packages: pip list")

# ---------------------------
# 6. Freeze (export) dependencies
# ---------------------------
# Run in terminal:
# pip freeze > requirements.txt
print("Save dependencies: pip freeze > requirements.txt")

# ---------------------------
# 7. Install from requirements.txt
# ---------------------------
# Run in terminal:
# pip install -r requirements.txt
print("Install from requirements: pip install -r requirements.txt")

# ---------------------------
# 8. Upgrade pip or a package
# ---------------------------
# pip install --upgrade pip
# pip install --upgrade requests
print("Upgrade pip/package: pip install --upgrade <package>")

# ---------------------------
# 9. Using pip inside Python script
# ---------------------------
def install_package(package: str):
    """Programmatically install a package with pip"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Example usage:
# install_package("numpy")

# ---------------------------
# 10. Searching packages (from terminal)
# ---------------------------
# pip search flask
print("Search package (deprecated in new pip, use PyPI website): pip search <package>")
