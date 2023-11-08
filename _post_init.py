"""
This is used by the template to run after pdm init, no need to edit and you can safely delete after init
"""

import os

if __name__ == "__main__":
    script = """
import toml

with open(file="pyproject.toml", mode="r", encoding="utf-8") as f:
    pyproject = toml.load(f)

del pyproject["tool"]["pdm"]["scripts"]["post_init"]
if "version" in pyproject["project"]:
    del pyproject["project"]["version"]
pyproject["project"]["requires-python"] = ">=3.9,!=3.9.7,<3.13"

with open(file="pyproject.toml", mode="w", encoding="utf-8") as f:
    toml.dump(pyproject, f)


    """
    with open(file=".post_init.py", mode="w", encoding="utf-8") as f:
        f.write(script)

    os.system(command="git init")
    os.system(command="pdm venv create -v -f")
    os.system(command="pdm run pip install -U toml")
    os.system(command="pdm run python .post_init.py")
    os.remove(path=".post_init.py")
    os.remove(path="LICENSE")
