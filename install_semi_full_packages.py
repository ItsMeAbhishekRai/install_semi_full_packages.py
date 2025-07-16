"""
install_semi_full_packages.py
------------------------------
This script installs a balanced set of essential Python packages for developers, students, and automation enthusiasts.

✅ Categories Covered:
- Core Utilities
- Development Tools
- Data Handling
- Web Development
- Database Integration
- Automation & Scripting
- System & Networking Tools
- Security Utilities
- File Format Handling
- Jupyter & Teaching Tools
- NLP & Voice Libraries
- AI & Chatbot Integration

Usage (Windows/macOS/Linux):
----------------------------
1. Make sure Python is installed (check with: python --version)
2. Save this script locally.
3. Open a terminal or command prompt in the script directory.
4. Run the script using:
   python install_semi_full_packages.py

Note: It's recommended to use a virtual environment before installation.
"""

import subprocess
import sys

# List of essential packages
packages = [
    # Core Utilities
    'pip', 'setuptools', 'wheel', 'virtualenv', 'ipython', 'python-dotenv',
    'rich', 'loguru', 'colorama', 'tabulate', 'tqdm',
    'black', 'flake8', 'pylint', 'mypy', 'pre-commit', 'pytest',
    'pandas', 'openpyxl', 'csvkit', 'jsonlines',
    'flask', 'django', 'fastapi', 'jinja2',
    'requests', 'httpx', 'beautifulsoup4', 'lxml', 'urllib3',
    'sqlalchemy', 'pymongo', 'psycopg2-binary', 'tinydb', 'mysql-connector-python',
    'pyautogui', 'keyboard', 'schedule', 'pyperclip', 'watchdog',
    'psutil', 'platformdirs', 'socketio', 'websockets', 'flask-socketio',
    'cryptography', 'pycryptodome', 'passlib', 'bcrypt', 'pyjwt',
    'python-docx', 'python-pptx', 'pypdf',
    'jupyterlab', 'notebook', 'nbconvert', 'pygments', 'manim',
    'nltk', 'textblob', 'speechrecognition', 'pyttsx3',
    'transformers', 'openai', 'langchain'
]

def install_packages(pkg_list):
    for pkg in pkg_list:
        print(f"🔧 Installing: {pkg}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install: {pkg}")

if __name__ == "__main__":
    print("🚀 Starting installation of semi-full Python development environment...\n")
    install_packages(packages)
    print("\n✅ Installation process complete!")
