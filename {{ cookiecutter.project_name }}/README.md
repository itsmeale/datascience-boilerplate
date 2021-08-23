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
│   ├── extraction                -- code to obtain data
│   ├── featuers                  -- feature engineering scripts
│   ├── models                    -- model training scripts
│   └── pipelines                 -- python scripts to reproduce the project from start to end                    
├── tests                         -- folder with test scripts
├── scripts                       -- folder with bash scripts used for setup the project
├── README.md                     -- description of what the project consists of, how to reproduce it and how to contribute
├── Dockerfile                    -- Describes the docker image.
├── .dockerignore                 -- Describes assets to be ignore by docker.
├── params.yml                    -- file with all parameters used in the project, to facilitate documentation and reproduction
└── pyproject.toml                -- file that specify all code dependencies
```

## How to install
To install run
```
$ poetry install
```
After installing you could access the virtual enviroment with `poetry shell` \
Create a github repository and add the remote origin to do yout project version control.

## How to run
...

## How to contribute
Install all project dependencies (prod and dev)
```
$ poetry install
```

Create your own branch, do your contribution and certifies that the code is complaint with the code standards:
```
$ poetry run fmt-check
$ poetry run isort-check
$ poetry run linter
$ poetry run tests
```
Now, open the pull request and enjoy code review :)