from google.genai import types

list_files_schema = types.FunctionDeclaration(
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
)

functions = types.Tool(
    function_declarations=[
        list_files_schema
    ]
)