"""
This is used by the template to run after pdm init, no need to edit and you can safely delete after init
"""

import os
import sys

try:
    import toml
except:
    os.system(command="pip install -U toml")
    sys.exit(0)


if __name__ == "__main__":
    with open(file="pyproject.toml", mode="r", encoding="utf-8") as f:
        pyproject = toml.load(f)

    del pyproject["tool"]["pdm"]["scripts"]["post_init"]
    if "version" in pyproject["project"]:
        del pyproject["project"]["version"]
    pyproject["project"]["requires-python"] = ">=3.9,!=3.9.7,<3.13"

    with open(file="pyproject.toml", mode="w", encoding="utf-8") as f:
        toml.dump(pyproject, f)

    os.remove(path="LICENSE")
