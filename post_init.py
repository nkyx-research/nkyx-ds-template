import argparse
import json
import os
import shutil
from glob import glob


def replace_filenames(old_name, new_name, dry_run=True) -> None:
    filepaths: list[str] = glob(pathname=f"./**/{old_name}", recursive=True)
    for p in filepaths:
        new_p: str = p.replace(old_name, new_name)
        print(f"renaming: {p} to {new_p}")
        if not dry_run:
            if not os.path.exists(path=new_p):
                os.rename(src=p, dst=new_p)
            else:
                shutil.rmtree(p, ignore_errors=True)


def replace_content(old_str, new_str, dry_run=True) -> None:
    filepaths: list[str] = [
        "./scripts/hello_world.py",
        "./tests/test_methods.py",
        "./pyproject.toml",
    ]

    for p in filepaths:
        if not os.path.exists(p):
            continue
        print(f"replace content in {p}: {old_str} to {new_str}")
        if not dry_run:
            with open(file=p, mode="r+", encoding="utf-8") as f:
                content: str = f.read()
                content = content.replace(old_str, new_str)
                f.seek(0)
                f.write(content)
                f.truncate()


def post_init(configs, dry_run=True) -> None:
    namespace_name = configs["namespace"].lower().replace(" ", "_").replace("-", "_")
    package_name = configs["project_name"].lower().replace(" ", "_").replace("-", "_")
    replace_filenames(
        old_name="nkyx",
        new_name=namespace_name,
        dry_run=dry_run,
    )

    replace_filenames(
        old_name="ds-template",
        new_name=configs["project_name"],
        dry_run=dry_run,
    )

    replace_filenames(
        old_name="ds_template",
        new_name=package_name,
        dry_run=dry_run,
    )

    replace_content(old_str="nkyx", new_str=namespace_name, dry_run=dry_run)

    replace_content(
        old_str="ds-template", new_str=configs["project_name"], dry_run=dry_run
    )

    replace_content(old_str="ds_template", new_str=package_name, dry_run=dry_run)

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


if __name__ == "__main__":
    default: str = json.dumps(
        obj={
            "namespace_name": "nkyx",
            "project_name": "test-ds-template",
            "author": "Qu Tang",
            "email": "qu.tang@outlook.com",
            "description": "test ds template",
            "home_page": "https://qutang.dev",
            "repo_url": "https://github.com/qutang/test-pdm",
        }
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("--configs", type=str, default=default)
    parser.add_argument("--dry-run", action="store_true", required=False)

    args: dict[str, str] = vars(parser.parse_args())

    if args["dry_run"]:
        print("In dry run mode")

    args["configs"] = args["configs"].replace("'", '"')
    args["configs"] = json.loads(args["configs"])

    print(args["configs"])

    post_init(
        configs=args["configs"],
        dry_run=bool(args["dry_run"]),
    )
