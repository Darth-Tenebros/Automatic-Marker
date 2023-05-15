import ast
from typing import List, Union


def check_function_existence(file_path: str, function_names: List[str]) -> Union[List[str], str]:
    """checks if the the expected functions for this assignment module
    are defined in the given file

    Parameters
    ----------
    file_path: str
        the path to the file on system
    function_names: List[str]
        a list of the functions that the student is expected to have defined in given file
    
    Returns
    -------
    List[str] | str
        returns a list of all the functions that are in functions_names and in the given file as well
        should the file not be found, a string is returned instead
    """

    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
        tree = ast.parse(source_code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        functions_found = []
        for function_name in function_names:
            if function_name in functions:
                functions_found.append(function_name)
        return functions_found
    except IOError:
        return "File '{}' not found.".format(file_path)
