import os
import glob
from typing import List


def get_all_files_in_dir(root_dir: str, student_number: str, delimeter: str) -> List[str]:
    """gets all the file (names) in a given directory.

    Parameters
    ----------
    root_dir: str
        the direcory from "/" to wherever this project may be stored
    student_number: str
        the student number represents the name of the folder, all assignments should be 
        submitted in folders named with student numbers.
    delimeter: str
        the separator for directories
        expected to be "/" for *nix systems and "\\" (backslash) for Windows
    
    Returns
    -------
    List[str]
        a list containing all the file names in the goven directory
    """

    files = []
    dir = f"{root_dir}{delimeter}{student_number}"
    file: List[str] = glob.glob(dir+f"{delimeter}*.py")
    for each_file in file:
        files.append(each_file[each_file.rfind("/")+1:])
    return files


def get_student_numbers(directory: str) -> List[str]:
    """retrive all the student numbers in the given directory. submitted folders
    should be named with student numbers.

    Parameters
    ----------
    directory: str
        the directory to traverse

    Returns
    -------
    List[str]
        a list with all the student numbers (folder names)
    """

    student_numbers = []

    for directory in os.listdir(directory):
        student_numbers.append(directory)
    return student_numbers
