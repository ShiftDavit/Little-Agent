import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        workdir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(workdir_abs, file_path))
        valid_target = os.path.commonpath([workdir_abs, target_path]) == workdir_abs
        if not valid_target:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Passed validations

        with open(target_path, "r") as f:
            content = f.read(config.CONTENT_READ_LIMIT)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.CONTENT_READ_LIMIT} characters]'

            return content
        
    except Exception as e:
        return f"Error: {e}"