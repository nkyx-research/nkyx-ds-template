# NKYX data science template

## Features

* [x] `Python` based
* [x] Use `pdm-backend` as build system
* [x] Use `pdm` as project dependency management system
* [x] Local package is installable to allow sharing
* [x] Settings for VS code are also synced
* [x] Built in `jupyter`, `ipywidgets`, and `voila` support via dev dependencies
* [x] Built in `streamlit` support via dev dependencies
* [x] Built in `dvc` support
* [x] Make the template repo itself is a functional environment and can also be used as a template via copier
  * Better than using copier and cookiecutter templates!
* [x] Post init can help setup `git` environment, and run the first `pdm update` for you, these are all done automatically!
* [x] Use `scm` to single source project version
* [ ] Make torch installation work via pdm torch plugin
* [ ] CI workflows for the created project
  * [ ] Run tests
  * [ ] Build packages
  * [ ] Build & deploy static doc site
* [ ] CI workflows for checking the template repo itself
  * [ ] Test creating a new project
  * [ ] Test updating an existing project via `copier`
* [ ] Support updating a project if the template evolves
* [ ] Support `pytest-cov`
* [ ] Support documentation site via `MKDocs` or single page site

## Usage

0. Prerequisite: Install `python` (of course!), `pdm`, `copier` and `dvc` into your global environment or your `python` global environment

    * Install `copier` into `pdm` as well

        ```bash
        > pdm self add copier
        ```

1. Init a new repo using and following command

    ```bash
    > cd [project_root_path] && pdm init --copier gh:qutang/nkyx-ds-template --UNSAFE
    ```

    or use `copier`

    ```bash
    > copier copy --trust gh:qutang/nkyx-ds-template [project_root_path]
    ```

2. You are all set and good to go!

## References

1. voila: <https://voila.readthedocs.io/en/stable/using.html>
2. jupyter: <https://jupyter.org/>
3. ipywidgets: <https://ipywidgets.readthedocs.io/en/stable/>
4. streamlit: <https://streamlit.io/>
5. pdm: <https://pdm-project.org/latest/>
6. copier: <https://copier.readthedocs.io/>
7. dvc: <https://dvc.org/>
8. 

## Recommended python packages to boost productivity

1. rich: <https://rich.readthedocs.io/en/latest/>
