

def check_syntax(file_path: str) -> bool:
    """checks if the given file "compiles" or not. that is, whether or not
    the given file has syntax errors

    Parameters
    ----------
    file_path: str
        the path to the file on system
    
    Returns
    -------
        bool
            a boolean value to indicate whether or not the file compiled
            True for compile pass, False for compile fail.
    """
    
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
        compile(source_code, file_path, "exec")
        return True
    except (SyntaxError, TypeError) as e:
        print("Compilation error:", str(e))
        return False
