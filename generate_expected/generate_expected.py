
from src.program_executor import run_program
import platform, os

def main():
    DIR_DELIMETER = '/'
    if platform.system() == "Windows":
        DIR_DELIMETER = '\\'
    
    target_module = "margin.py"
    relative_path_to_solution_file = f"{os.getcwd()}{DIR_DELIMETER}generate_expected{DIR_DELIMETER}solution{DIR_DELIMETER}{target_module}"
    
    trial_input = ["1000","10"]
    result = run_program(relative_path_to_solution_file, trial_input)
    raw = repr(result)
    with open(f"{target_module}.txt", 'a') as expected:
        expected.write(raw)

if __name__ == '__main__':
    main()
