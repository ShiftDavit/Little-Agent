from google.genai import types
from config import CONTENT_READ_LIMIT

functions = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="list_files",
            description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "directory": types.Schema(
                        type=types.Type.STRING,
                        description="Directory path to list files from, relative to the working directory",
                    ),
                },
            ),
        ),

        types.FunctionDeclaration(
            name="get_file_content",
            description=f"""
                Reads file contents of a specified file with a path relative to the working directory,
                returning the file at most {CONTENT_READ_LIMIT} characters of content as a string
            """,
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="File path to read from, relative to the working directory",
                    ),
                },
                required=["file_path"]
            ),
        ),

        types.FunctionDeclaration(
            name="run_python",
            description="Runs specified python file with a path relative to the working directory, returning the outputs of the subprocess",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the python file to execute, relative to the working directory",
                    ),

                    "args": types.Schema(
                        type=types.Type.ARRAY,
                        description="Optional list of arguments to pass to the python program",
                        items=types.Schema(
                            type=types.Type.STRING
                        )
                    ),
                },
                required=["file_path"]
            ),
        ),
    
        types.FunctionDeclaration(
            name="write_file",
            description="Writes text content to a specified file within the working directory (overwriting if the file exists)",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the file to write, relative to the working directory",
                    ),
                    "content": types.Schema(
                        type=types.Type.STRING,
                        description="Text content to write to the file",
                    ),
                },
                required=["file_path", "content"],
            ),
        ),
    ]
)