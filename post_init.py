import argparse
import json
import os
from codecs import ignore_errors
from glob import glob


def replace_filenames(old_name, project_name, dry_run=True) -> None:
    filepaths: list[str] = glob(pathname=f"./**/{old_name}", recursive=True)
    for p in filepaths:
        new_p: str = p.replace(old_name, project_name)
        print(f"renaming: {p} to {new_p}")
        if not dry_run:
            os.rename(src=p, dst=new_p)


def replace_content(old_str, new_str, dry_run=True) -> None:
    filepaths: list[str] = [
        "./scripts/hello_world.py",
        "./tests/test_methods.py",
        "./pyproject.toml",
    ]

    for p in filepaths:
        print(f"replace content in {p}: {old_str} to {new_str}")
        if not dry_run:
            with open(file=p, mode="r+", encoding="utf-8") as f:
                content: str = f.read()
                content = content.replace(old_str, new_str)
                f.seek(0)
                f.write(content)
                f.truncate()


def replace_file(filepath: str, new_content: str, dry_run=True) -> None:
    print(f"replace file {filepath} with {new_content}")
    if not dry_run:
        with open(file=filepath, mode="w", encoding="utf-8") as f:
            f.write(new_content)


def post_init(configs, dry_run=True) -> None:
    package_name = configs["project_name"].lower().replace(" ", "_").replace("-", "_")
    replace_filenames(
        old_name="nkyx_ds_template",
        project_name=package_name,
        dry_run=dry_run,
    )

    replace_filenames(
        old_name="nkyx-ds-template",
        project_name=configs["project_name"],
        dry_run=dry_run,
    )

    replace_content(
        old_str="nkyx-ds-template", new_str=configs["project_name"], dry_run=dry_run
    )

    replace_content(old_str="nkyx_ds_template", new_str=package_name, dry_run=dry_run)

    replace_content(old_str="{{ author }}", new_str=configs["author"], dry_run=dry_run)

    replace_content(old_str="{{ email }}", new_str=configs["email"], dry_run=dry_run)

    replace_content(
        old_str="{{ description }}", new_str=configs["description"], dry_run=dry_run
    )

    replace_content(
        old_str="{{ home_page }}", new_str=configs["home_page"], dry_run=dry_run
    )

    replace_content(
        old_str="{{ repo_url }}", new_str=configs["repo_url"], dry_run=dry_run
    )

    readme_template: str = f"""
# {configs["project_name"].capitalize()}

## References

1. voila: https://voila.readthedocs.io/en/stable/using.html
2. jupyter: https://jupyter.org/
3. ipywidgets: https://ipywidgets.readthedocs.io/en/stable/
4. streamlit: https://streamlit.io/
5. pdm: https://pdm-project.org/latest/

## Recommended python packages to boost productivity

1. rich: https://rich.readthedocs.io/en/latest/
"""

    replace_file(filepath="./README.md", new_content=readme_template, dry_run=dry_run)


if __name__ == "__main__":
    default: str = json.dumps(
        {
            "project_name": "test-pdm",
            "author": "Qu Tang",
            "email": "qu.tang@outlook.com",
            "description": "test pdm",
            "home_page": "https://qutang.dev",
            "repo_url": "https://github.com/qutang/test-pdm",
        }
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--configs", type=str, required=True)
    parser.add_argument("--dry-run", action="store_true", required=False)

    args: dict[str, str] = vars(parser.parse_args())

    if args["dry_run"]:
        print("In dry run mode")

    args["configs"] = args["configs"].replace("'", '"')
    args["configs"] = json.loads(args["configs"])

    print(args["configs"])

    post_init(
        args["configs"],
        dry_run=bool(args["dry_run"]),
    )
