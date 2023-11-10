import argparse
import os
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


def setup_env() -> None:
    os.system(command="git init")
    os.system(command="git branch -m main")
    os.system(command="pdm update")
    os.system("pdm run test")


def post_init(new_project_name: str, new_package_name, dry_run=True) -> None:
    replace_filenames(
        old_name="nkyx_ds_template", project_name=new_package_name, dry_run=dry_run
    )

    replace_filenames(
        old_name="nkyx-ds-template", project_name=new_project_name, dry_run=dry_run
    )

    replace_content(
        old_str="nkyx-ds-template", new_str=new_project_name, dry_run=dry_run
    )

    replace_content(
        old_str="nkyx_ds_template", new_str=new_package_name, dry_run=dry_run
    )

    readme_template: str = f"""
# {new_project_name.capitalize()}

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

    setup_env()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", type=str)
    parser.add_argument("--package_name", type=str, required=False)
    parser.add_argument("--dry-run", action="store_true", required=False)

    args: dict[str, str] = vars(parser.parse_args())

    if args["dry_run"]:
        print("In dry run mode")

    if args["package_name"] is None:
        args["package_name"] = (
            args["project_name"].lower().replace(" ", "_").replace("-", "_")
        )

    print(f"New project name: {args['project_name']}")
    print(f"New package name: {args['package_name']}")

    post_init(
        new_project_name=args["project_name"],
        new_package_name=args["package_name"],
        dry_run=bool(args["dry_run"]),
    )
