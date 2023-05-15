import json
import os
import platform
from typing import List, Dict, Tuple
from src.directories import get_all_files_in_dir, get_student_numbers
from src.program_executor import run_program
from src.report import compare_output, report
from src.check_modules import check_function_existence
from src.check_syntax import check_syntax

def get_trials(json_data: Dict[str, Dict]) -> Tuple[List[str], List[str], Dict[str, int]]:
    """get the trial inputs for a question. 

    Parameters
    ----------
    json_data: Dict[str, Dict]
        dictionary with all the marking data
    
    Returns
    -------
    List[str]
        a list conataining all trial inputs
    List[str]
        a list containing the expected outputs for the trial inputs
    Dict[str, int]
        a dictionary with the functions expected to have been defined with their assosciated marks
    """

    trial_inputs = []
    expected_outputs = []
    expected_functions = json_data['function_names']

    trial_data = json_data['trials']
    trial_data = trial_data.values()

    for each_trial in trial_data:
        trial_inputs.append(each_trial['trial_input'])
        expected_outputs.append(each_trial['trial_expected_output'])
    
    return trial_inputs, expected_outputs, expected_functions


def totalise_function_marks(student_functions: List[str], func_dict: Dict[str, int]) -> int:
    """calculates the marks for the functions the student has defined

    Parameters
    ----------
    student_functions: List[str]
        a list containing all the functions the student has defined in a module
    func_dict: Dict[str, int]
        a dictionary with the functions expected to have been defined with their assosciated marks
    
    Returns
    -------
    int
        the total marks for the defined functions
    """

    mark = 0
    
    for func in student_functions:
        if func in func_dict.keys():
            mark += func_dict[func]
    return mark


def run_trial(each_program: str, trials: List[str], path_to_each_student: str,\
                marking_file: Dict, trial_outputs: List[str], delimeter: str) -> int:
    """runs the given program with the given trial inputs

    Parameters
    ----------
    each_program: str
        name of the file
    trials: List[str]
        list containing the inputs for this trial
    path_to_each_student: str
        the path to this student's assignment folder on system
    marking_file: Dict
        dictionary with all the marking data
    trial_outputs: List[str]
        the expected outputs for the given trial inputs
    delimeter: str
        the separator for directories
        expected to be "/" for *nix systems and "\\" (backslash) for Windows
    
    Returns
    -------
    int
        the mark for this trial (0 or full mark)
    """

    mark = 0
    for each_trial in range(len(trials)):
        trial_number = each_trial + 1
        trial_name = f"trial_{trial_number}"
        trial_mark = marking_file[each_program]['trials'][trial_name]['mark']

        result = run_program(f"{path_to_each_student}{delimeter}{each_program}.py", trials[each_trial])
        
        if compare_output(result, trial_outputs[each_trial]):
            mark += trial_mark
            report("trial passed", trial_mark, path_to_each_student, delimeter)
        else:
            message = f"expected output: \n{trial_outputs[each_trial]}\n\nyour output: \n{result}\n\n"
            message = message.replace('\t', '')
            report(message, 0, path_to_each_student, delimeter)
        
    return mark
