import os
import subprocess

PROCESS_TIMEOUT_SEC = 30

def run_python(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        workdir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(workdir_abs, file_path))
        valid_target = os.path.commonpath([workdir_abs, target_path]) == workdir_abs
        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        _, file_extension = os.path.splitext(target_path)
        if file_extension != '.py':
            return f'Error: "{file_path}" is not a Python file'

        # Passed validations
        command: list[str] = ["python", target_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=workdir_abs,
            capture_output=True,
            text=True,
            timeout=PROCESS_TIMEOUT_SEC
        )

        output = ""
        if result.returncode != 0:
            output += "\nProcess exited with code X"
        if result.stdout==""==result.stderr:
            output += "\nNo output produced"
        else:
            output += f"\nSTDOUT: {result.stdout}"
            output += f"\nSTDERR: {result.stderr}"

        return output

    except TimeoutError:
            return "Error: Function call timed out!"
        
    except Exception as e:
        return f"Error: Executing python file - {e}"