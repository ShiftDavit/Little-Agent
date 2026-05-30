from google.genai import types
from config import CONTENT_READ_LIMIT
from collections.abc import Callable

from get_file_content import get_file_content
from list_files import list_files
from run_python import run_python
from write_file import write_file

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

function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "list_files": list_files,
    "run_python": run_python,
    "write_file": write_file,
}

def call_function(function_call: types.FunctionCall, verbose: bool = False) -> types.Content:
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    name = function_call.name or "" # in case of None
    func = function_map[name]
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name,
                    response={"error": f"Unknown function: {name}"},
                )
            ],
        )
    
    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"] = "./calculator"

    result = func(**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name,
                response={"result": result},
            )
        ],
    )
