# NKYX data science template

## Features

1. `Python` based
2. Use `pdm-backend` as build system
3. Use `pdm` as project dependency management system
4. As simple as possible
5. Local package is installable to allow sharing
6. Settings for VS code are also synced
7. Built in `jupyter`, `ipywidgets`, and `voila` support via dev dependencies
8. Built in `streamlit` support via dev dependencies

## Usage

1. Create a new repo based on this template via github's website or github CLI

    ```bash
    > gh repo create [project_name] --template qutang/nkyx-ds-template
    ```

2. Run post_init script from root project directory

    ```bash
    > python post_init.py [project_name] --package_name [package_name]
    ```

3. Revise `pyproject.toml` to fit your need
4. Run `git init` and then `pdm update` to sync packages up to date

## References

1. voila: <https://voila.readthedocs.io/en/stable/using.html>
2. jupyter: <https://jupyter.org/>
3. ipywidgets: <https://ipywidgets.readthedocs.io/en/stable/>
4. streamlit: <https://streamlit.io/>
5. pdm: <https://pdm-project.org/latest/>

## Recommended python packages to boost productivity

1. rich: <https://rich.readthedocs.io/en/latest/>
