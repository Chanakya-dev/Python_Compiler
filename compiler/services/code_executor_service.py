# app/services/code_executor_service.py
import subprocess
import sys

def execute_code(code: str) -> str:
    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()  # .strip() to remove any trailing newlines
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing code: {e.stderr}")
