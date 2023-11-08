"""
This is used by the template to run after pdm init, no need to edit and you can safely delete after init
"""

import configparser
import os

if __name__ == "__main__":
    pyproject = configparser.ConfigParser(allow_no_value=True, strict=False)
    pyproject.read(filenames="pyproject.toml", encoding="utf-8")

    pyproject.remove_section(section="tool.pdm.scripts.post_init")
    pyproject.remove_option(section="project", option="version")
    pyproject.set(
        section="project", option="requires-python", value=">=3.9,!=3.9.7,<3.13"
    )

    with open(file="pyproject.toml", mode="w", encoding="utf-8") as f:
        pyproject.write(fp=f)

    os.remove(path="LICENSE")
