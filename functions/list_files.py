import os

# Working directory is the directory the llm cannot step out of
# via ../../...
def list_files(working_directory: str, directory: str = ".") -> str:
    try:
        workdir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(workdir_abs, directory))
        valid_target = os.path.commonpath([workdir_abs, target_dir]) == workdir_abs
        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Passed validations

        info: str = ""
        for c in os.listdir(target_dir):
            path = os.path.join(target_dir, c)
            isDir = os.path.isdir(path)
            size = os.path.getsize(path)
            info += f"- {c}: file_size={size} bytes, is_dir={isDir}\n"
        
        return info[:-1]
    except Exception as e:
        return f"Error: {e}"
