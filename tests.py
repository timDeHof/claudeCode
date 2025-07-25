from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    working_dir = "calculator"
    
    # "read the contents of main.py"
    print("Test 1: read the contents of main.py")
    result = get_file_content(working_dir, 'main.py')
    print(result)
    print()
    
    # "write 'hello' to main.txt"
    print("Test 2: write 'hello' to main.txt")
    result = write_file(working_dir, 'main.txt', 'hello')
    print(result)
    print()
    
    # "run main.py"
    print("Test 3: run main.py")
    result = run_python_file(working_dir, 'main.py')
    print(result)
    print()
    
    # "list the contents of the pkg directory"
    print("Test 4: list the contents of the pkg directory")
    result = get_files_info(working_dir, 'pkg')
    print(result)
    print()

if __name__ == "__main__":
    test()
