import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    """
    Returns the content of a file.

    Args:
        working_directory (str): The current working directory.
        file_path (str): The path to the file, relative to the working directory.

    Returns:
        str: The content of the file or an error message if the file is outside
             the working directory or not a regular file.
    """
    # Get the absolute path of the file
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # Get the absolute path of the working directory
    abs_working_dir = os.path.abspath(working_directory)

    # Check if the file path is within the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Check if the path exists and is a regular file
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # If the file is within the working directory and is a regular file, read and return its content
    with open(abs_file_path, 'r') as f:
        content = f.read(10001)  # Read up to 10001 chars to check if file is longer

        if len(content) > 10000:
            return content[:10000] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
