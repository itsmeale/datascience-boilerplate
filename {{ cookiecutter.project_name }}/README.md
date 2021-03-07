{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------
```
├── data
│   ├── external                  -- folder with features from other databases (if any)
│   ├── interim                   -- intermediate data (pre-processed)
│   ├── processed                 -- processed data (features to be used)
│   └── raw                       -- raw data
├── references                    -- domain knowledge reference material
├── models                        -- storage of models
├── notebooks                     -- storage of experimental notebooks
├── reports                       -- data visualizations and other project outputs (storytelling)
│   └── figures
├── setup.py                      -- setup file for the module to be installable
├── {{cookiecutter.project_name}} -- folder where the scripts are stored
│   ├── features                  -- feature engineering scripts
│   └── models                    -- model training scripts
├── tests                         -- folder with test scripts
├── scripts                       -- folder with bash scripts used for setup the project
├── README.md                     -- description of what the project consists of, how to reproduce it and how to contribute
├── params.yml                    -- file with all parameters used in the project, to facilitate documentation and reproduction
└── pyproject.toml                -- file that specify all code dependencies
```

## How to install
To install run
```
$ scripts/setup_env
```
After installing you could access the virtual enviroment with `poetry shell`

## How to run
...

## How to contribute
Install all project dependencies (prod and dev)
```
$ poetry install
```

Create your own branch, do your contribution and certifies that the code is complaint with the code standards:
```
$ poetry run check-code-quality
```
Now, open the pull request and enjoy code review :)