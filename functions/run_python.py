import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    if not working_directory or not file_path:
        return "Error: Working directory and file path must not be empty."

    full_path = os.path.join(working_directory, file_path)

    # Check if file exists
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    # Check if .py extension
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    # Check if path is within working directory
    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Execute the file
    try:
        result = subprocess.run(
            ['python3', full_path] + args,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        # Format output
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not output:
            return "No output produced."
        return "\n".join(output)
    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"
