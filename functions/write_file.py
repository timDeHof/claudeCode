import os
from google.genai import types

def write_file(working_directory, file_path, content):
    """
    Writes content to a file in the specified working directory.

    Args:
        working_directory (str): The base directory where the file will be written.
        file_path (str): The relative path of the file to be written.
        content (str): The content to be written to the file.

    Returns:
        None

    Raises:
        ValueError: If the working_directory or file_path is empty or invalid.
        IOError: If there's an error writing to the file.

    Example:
        write_file("/home/user", "test.txt", "Hello World")
        # This will write "Hello World" to /home/user/test.txt
    """

    if not working_directory or not file_path:
        return "Error: Working directory and file path must not be empty."

    full_path = os.path.join(working_directory, file_path)

    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except OSError as e:
        return f'Error: {str(e)}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the specified working directory. Creates the if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
