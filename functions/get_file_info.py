import os

def get_file_info(working_directory: str, directory: str = ".") -> str:
    workdir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(workdir_abs, directory))
    try:
        valid_target = os.path.commonpath([workdir_abs, target_dir]) == workdir_abs
        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except ValueError:
        return f'Error: Bad path'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    return f'Success: "{directory}" is within the working directory'

