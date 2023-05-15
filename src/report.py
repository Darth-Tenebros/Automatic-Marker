

def report(message: str, mark: int, dir: str, delimeter: str) -> None:
    """writes a given message and mark to a plain text file

    Parameters
    ----------
    message: str
        the message to be written to a text file
    mark: int
        the mark assosciated with the message
    delimeter: str
        the separator for directories
        expected to be "/" for *nix systems and "\\" (backslash) for Windows
        
    Returns
    -------
        None
    """

    with open(dir+f"{delimeter}student_output.txt", 'a') as student_output_file:
        student_output_file.write('\n' + message + '\n')
        student_output_file.write(str(mark) + '\n')


def compare_output(actual_output: str, expected_output: str) -> bool:
    """compare two strings

    Parameters
    ----------
    actual_output: str
    expected_output: str

    Returns
    -------
    bool

    """
    
    return actual_output == expected_output
