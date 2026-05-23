import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        workdir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(workdir_abs, file_path))
        valid_target = os.path.commonpath([workdir_abs, target_path]) == workdir_abs
        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Passed validations

        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"