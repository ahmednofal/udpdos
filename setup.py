#!/usr/bin/env python
import setuptools
import io

fh = io.open("README.md", mode="r", encoding="utf-8")
long_description = fh.read()

tool_name="udpdos"
version_num = "0.0.1"
author_name = "Hedi Nasr"
setuptools.setup(name=tool_name,
        version=version_num,
        author=author_name,
        description=long_description,
        long_description_content_type="text/markdown",
        url="https://gist.github.com/Ananasr/e05f3286b6ab94ec2c5431e64832c13e",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
        scripts = [
                'core/udpdos'
            ],
)
