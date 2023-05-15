# generating the trial_expected_output for python modules
to generate trial_expected_output, **the marker must first create a memo** of the assignment. the files should then be put in the `solution` directory in the `generated_expected` directory.

then, (unfortunately for now) the marker must:\
* modify `generate_expected.py` \
    line 10: to set the target file (just the name.py) \
    line 13 to add inputs for this target file

**note: the inputs used in line 13 must be the same as those that will be used in `marking_scheme.json`** \

**repeat this for every file that will be marked in the solution**



then:
in your terminal from root project directory, run:
```shell
sudo python3 setup.py develop
```
on some systems it's:
```shell
sudo python setup.py develop
```
* run `generate_expected.py` and a plain text file with name of the module will be produced in the root  directory of the project: \
* copy the contents into `marking_scheme.json` for this trial.
* copy the inputs into `marking_scheme.json` for this trial