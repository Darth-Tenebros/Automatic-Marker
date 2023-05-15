import subprocess
import sys
from typing import Union, List


def run_program(file_path: str, input_data: Union[List[str], None] = None) -> str:
    """runs a given program and returns the output.
    should the program run for more than 5 seconds, it is terminated, an exception is thrown
    and a string is returned

    Parameters
    ----------
    file_path: str
        the path to the file on system
    input_data: List[str], optional
        list containing the input data to be passed into the program as it executes.
        should the list be not passed in, the program is assumed to not require input
    
    Returns
    -------
    str
        the result of executing the program
    """

    try:
        if input_data:
            process = subprocess.Popen([sys.executable, file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input='\n'.join(input_data))
            result = stdout.strip()
        else:
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=5).stdout.strip()

        return result
    except subprocess.TimeoutExpired:
        return "Timeout occurred."
    except Exception as e:
        return str(e)
