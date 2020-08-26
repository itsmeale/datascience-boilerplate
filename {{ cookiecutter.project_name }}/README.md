{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------
```
├── data
│   ├── external                 -- folder with features from other databases (if any)
│   ├── interim                  -- intermediate data (pre-processed)
│   ├── processed                -- processed data (features to be used)
│   └── raw                      -- raw data
├── references                   -- domain knowledge reference material
├── models                       -- storage of models
├── notebooks                    -- storage of experimental notebooks
├── reports                      -- data visualizations and other project outputs (storytelling)
│   └── figures
├── setup.py                     -- setup file for the module to be installable
├── src                          -- folder where the scripts are stored
│   ├── features                 -- feature engineering scripts
│   └── models                   -- model training scripts
├── README.md                    -- description of what the project consists of, how to reproduce it and how to contribute
├── params.yml                   -- file with all parameters used in the project, to facilitate documentation and reproduction
└── Pipfile
```

## How to install
To install run
```
$ pipenv install
```

## How to run
...

## How to contribute
Install all project dependencies (prod and dev)
```
$ pipenv install
$ pipenv install --dev
```

Create your own branch, do your contribution and certifies that the code is complaint with the code standards:
```
$ pipenv run isort-check
$ pipenv run isort-fmt
$ pipenv run fmt
$ pipenv run lint
```
Now, open the pull request and enjoy code review :)