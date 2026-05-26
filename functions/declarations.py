from google.genai import types

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
                        description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
                    ),
                },
            ),
        ),

        types.FunctionDeclaration(
            name="get_file_content",
            description="Reads file contents of a specified file relative to the working directory, returning the file content as a string",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="File path to read from, relative to the working directory (default is the working directory itself)",
                    ),
                },
            ),
        ),
    ]
)