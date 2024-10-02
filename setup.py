import os
import sys

from setuptools import setup

# Package meta-data.
NAME = "PoBExporter"
DESCRIPTION = "Python library to generate Path of Building exports directly from PoE API without running PoB headless"
URL = "https://github.com/Liberatorist/PoBExporter"
EMAIL = ""
AUTHOR = "Liberatorist"
REQUIRES_PYTHON = ">=3.11.0"
VERSION = "3.25.14"

# What packages are required for this module to be executed?
REQUIRED = []

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}
data_files = []
for file in os.listdir("PoBExporter/poe_data"):
    # not packing all stat translations for now
    data_files.append(os.path.join("PoBExporter/poe_data", file))
directory = "/".join(sys.prefix.split("/")[:-2]) + "/PoBExporter/poe_data"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=["PoBExporter._create_export", "PoBExporter._item",
                "PoBExporter._passive_encode", "PoBExporter._schema", "PoBExporter._fetch"],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    license="proprietary",

    data_files=[
        (directory, data_files),
    ]

)
