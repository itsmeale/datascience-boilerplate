# Data science boilerplate

A boilerplate made with cookiecutter to help the start of the development of data science projects.

## How to start
```
$ pip install cookiecutter
$ cookiecutter https://github.com/itsmeale/datascience-boilerplate
```

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
├── Dockerfile                    -- Describes the docker image.
├── .dockerign                    -- Describes assets to be ignore by docker.
├── params.yml                    -- file with all parameters used in the project, to facilitate documentation and reproduction
└── pyproject.toml                -- file that specify all code dependencies
```