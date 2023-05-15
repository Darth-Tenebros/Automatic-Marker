# Automatic-Marker

marking python assignments is a tedious job, this is a tool that we imagined to make that task easier. inspired by the [automatic marker](http://dl.cs.uct.ac.za/projects/automark/index.html) from [UCT's department of computer science](https://internal.cs.uct.ac.za/tech/automarker.html), we built what we think is a suitable tool to do the same job for [INF1002/INF1102](https://sit.uct.ac.za/our-degrees-undergraduates-bbussc-degrees/bachelor-commerce-specialising-information-systems#INF1002F/S) in the department of information systems.

## Note:
this automatic marker has a focus on the correctness of output by student submissions, it does not (at this time) support exhaustive testing for individual functions


# Marking
**there is a branch: `tutorial-branch` with a fully configured example**
instructions on setup of the AM to mark an assignment
### setting up the `marking_scheme.json`
each file expected to be in an assignment will be defined in `marking_scheme.json` as follows:
```json
{
    "<name of the file without '.py' extension>": {
        "file_names": [
            "<name of the same file with '.py' extension>"
        ],
        "function_names": {
            "<function expected to be defined in file>": <mark for function def as int>
        },
        "trials": {
            "trial_1" : {
                "trial_input": <comma separated list of inputs for ta trial, inputs must be in order>,
                "trial_expected_output": <string showing the expected output when the student's submission is ran using the <trial input>>,
                "mark": <mark for passing this trial (output same as trial_expected_output) >
            }
        }
    }
}
```

if there are more modules, they are defined as above in the same manner in the same json file separated by commas.

to generate the trial_expected_output [see](/generate_expected/README.md)

each student's submission should be in a folder with named with the student's student_number and all submissions should then be put in the `assignments directory`.

**make sure to delete the .gitkeep file in the assignments folder!!**

after all setup is done, find `main.py` in the root directory of this project and run it. reports will be produced in each student's folder.

# Note:
this project has been programmed to work in both windows and *nix systems but at this time it has only been tested on *nix systems

# Contributers

 <table>
    <tr>
        <td>
            <img src="https://avatars.githubusercontent.com/u/70268186?s=400&u=a19f63ed9bd01a5c9635fbc2e86bc5f573eca89e&v=4" alt="thifhidzi" width="150" height="150">
        </td>
        <td>
            <img src="https://media.licdn.com/dms/image/D5603AQFmEUmpTJepPA/profile-displayphoto-shrink_800_800/0/1676369570781?e=1689811200&v=beta&t=ZO2UB0u0-nE5kfh0cisfkDNBYLwwf9eQjrNhzcSbKDY" alt="yolisa" width="150" height="150=">
        </td>
    </tr>
    <tr>
        <td>Thifhidzi Rammbuda</td>
        <td>Yolisa Pingilili</td>
    </tr>
    <tr>
        <td><a href="https://www.linkedin.com/in/rammbudat">LinkedIn</a></td>
        <td><a href="https://www.linkedin.com/in/yolisa-pingilili-19148b210/">LinkedIn</a></td>
    </tr>
    <tr>
        <td><a href="https://github.com/RTEE001">Github</a></td>
        <td><a href="https://github.com/Darth-Tenebros">Github</a></td>
    </tr>
 </table>
 