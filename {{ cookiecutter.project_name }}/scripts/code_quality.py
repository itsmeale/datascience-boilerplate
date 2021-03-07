import os


def check_import_order():
    os.system("isort --check ./{{ cookiecutter.project_name }}/ --gitignore --dont-follow-links --verbose")


def check_code_formatting():
    os.system("black --check ./{{ cookiecutter.project_name }}/ --exclude __init__.py --verbose")


def sort_import_order():
    os.system("isort --check ./{{ cookiecutter.project_name }}/ ./tests/ --gitignore --dont-follow-links --verbose")


def do_code_formatting():
    os.system("black --check ./{{ cookiecutter.project_name }}/ ./tests/ --exclude __init__.py --verbose")


def linter():
    os.system("pylama ./{{ cookiecutter.project_name }}/ ./tests/")


def run_tests():
    os.system("pytest ./tests/ --verbose --color=yes --code-highlight=yes")


def check_code_quality():
    check_import_order()
    check_code_formatting()
    linter()
    run_tests()


def code_formatting():
    sort_import_order()
    do_code_formatting()
