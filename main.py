from typing import List, Dict, Tuple

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

