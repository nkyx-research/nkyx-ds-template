"""
This is used by the template to run after pdm init, no need to edit and you can safely delete after init
"""

import os
from typing import Any

import toml

if __name__ == "__main__":
    with open(file="pyproject.toml", mode="r", encoding="utf-8") as f:
        pyproject: dict[str, Any] = toml.load(f=f)

    if "version" in pyproject["project"]:
        del pyproject["project"]["version"]
    pyproject["project"]["requires-python"] = ">=3.9,!=3.9.7,<3.13"

    with open(file="pyproject.toml", mode="w", encoding="utf-8") as f:
        toml.dump(o=pyproject, f=f)

    os.remove(path="LICENSE")
